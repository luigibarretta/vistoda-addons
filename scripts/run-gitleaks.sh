#!/usr/bin/env bash
set -euo pipefail

readonly GITLEAKS_VERSION="8.30.1"
readonly GITLEAKS_ARCHIVE_SHA256="551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb"

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ "$(uname -s)" != "Linux" || "$(uname -m)" != "x86_64" ]]; then
  echo "The pinned Gitleaks runner currently supports Linux x86_64 only" >&2
  exit 2
fi

work_dir="$(mktemp -d)"
trap 'rm -rf -- "${work_dir}"' EXIT
archive="${work_dir}/gitleaks.tar.gz"

curl -fsSL "https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/gitleaks_${GITLEAKS_VERSION}_linux_x64.tar.gz" -o "${archive}"
printf '%s  %s\n' "${GITLEAKS_ARCHIVE_SHA256}" "${archive}" | sha256sum --check -
tar -xzf "${archive}" -C "${work_dir}" gitleaks

env \
  GIT_CONFIG_COUNT=1 \
  GIT_CONFIG_KEY_0=safe.directory \
  GIT_CONFIG_VALUE_0="${repo_root}" \
  "${work_dir}/gitleaks" git --no-banner --redact "${repo_root}"
