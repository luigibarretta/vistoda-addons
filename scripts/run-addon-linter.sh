#!/usr/bin/env bash
set -euo pipefail

readonly LINTER_COMMIT="f995494fd84fae6310d23617e66d0e37de4f14eb"
readonly LINTER_ARCHIVE_SHA256="fd968eee76bde70e1c86dc57e74db2ee346fe3ce431fa319dc44e30ae15d66cf"

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
work_dir="$(mktemp -d)"
trap 'rm -rf -- "${work_dir}"' EXIT
archive="${work_dir}/addon-linter.tar.gz"

curl -fsSL "https://github.com/frenck/action-addon-linter/archive/${LINTER_COMMIT}.tar.gz" -o "${archive}"
printf '%s  %s\n' "${LINTER_ARCHIVE_SHA256}" "${archive}" | sha256sum --check -
tar -xzf "${archive}" -C "${work_dir}"

linter_root="$(find "${work_dir}" -mindepth 1 -maxdepth 1 -type d -name 'action-*' -print -quit)"
if [[ -z "${linter_root}" || ! -f "${linter_root}/src/lint.py" ]]; then
  echo "Pinned Home Assistant add-on linter archive has an unexpected layout" >&2
  exit 1
fi

python3 -m venv "${work_dir}/venv"
"${work_dir}/venv/bin/python" -m pip install --disable-pip-version-check --no-compile \
  --requirement "${linter_root}/src/requirements.txt"

python3 - "${linter_root}/src/lint.py" "${work_dir}/lint.py" <<'PY'
from pathlib import Path
import sys

source = Path(sys.argv[1]).read_text(encoding="utf-8")
for schema in ("config.schema.json", "build.schema.json"):
    old = f'open("/{schema}")'
    if source.count(old) != 1:
        raise SystemExit(f"unexpected upstream schema lookup for {schema}")
    source = source.replace(old, f'open(Path(__file__).with_name("{schema}"))')
Path(sys.argv[2]).write_text(source, encoding="utf-8")
PY

install -m 0644 "${linter_root}/src/config.schema.json" "${work_dir}/config.schema.json"
install -m 0644 "${linter_root}/src/build.schema.json" "${work_dir}/build.schema.json"

apps=("$@")
if (("${#apps[@]}" == 0)); then
  apps=(vistoda_blink vistoda_ezviz vistoda_ring)
fi
for app in "${apps[@]}"; do
  env INPUT_PATH="${repo_root}/${app}" INPUT_COMMUNITY=false \
    "${work_dir}/venv/bin/python" "${work_dir}/lint.py"
done
