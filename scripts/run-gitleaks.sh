#!/usr/bin/env bash
set -euo pipefail

readonly GITLEAKS_VERSION="8.24.3"
readonly GITLEAKS_ARCHIVE_SHA256="9991e0b2903da4c8f6122b5c3186448b927a5da4deef1fe45271c3793f4ee29c"

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
