#!/usr/bin/env bash
set -euo pipefail

# Stage matching Bootstrap 4.6.2 and Bootswatch 4.6.2 Sass before Jekyll builds.
# The repository retains the original 4.3.1 Sass as a fallback for local development.
# This script only replaces the two Sass vendor directories in the CI workspace.
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

download_package() {
  local package="$1" url="$2"
  mkdir -p "$tmp/$package"
  curl --fail --location --silent --show-error --retry 3 --proto '=https' --tlsv1.2 "$url" -o "$tmp/$package.tgz"
  tar -xzf "$tmp/$package.tgz" -C "$tmp/$package"
  test -f "$tmp/$package/package/package.json"
}

download_package bootstrap "https://registry.npmjs.org/bootstrap/-/bootstrap-4.6.2.tgz"
download_package bootswatch "https://registry.npmjs.org/bootswatch/-/bootswatch-4.6.2.tgz"

node - "$tmp" <<'NODE'
const fs = require('fs');
const root = process.argv[2];
for (const name of ['bootstrap', 'bootswatch']) {
  const pkg = JSON.parse(fs.readFileSync(root + '/' + name + '/package/package.json', 'utf8'));
  if (pkg.version !== '4.6.2') throw new Error(name + ' version mismatch: ' + pkg.version);
}
NODE

test -f "$tmp/bootstrap/package/scss/bootstrap.scss"
test -f "$tmp/bootswatch/package/dist/united/_variables.scss"
test -f "$tmp/bootswatch/package/dist/united/_bootswatch.scss"

rm -rf _sass/bootstrap/scss
mkdir -p _sass/bootstrap
cp -a "$tmp/bootstrap/package/scss" _sass/bootstrap/scss
rm -rf _sass/bootswatch/dist
mkdir -p _sass/bootswatch
cp -a "$tmp/bootswatch/package/dist" _sass/bootswatch/dist

echo "Staged Bootstrap 4.6.2 and Bootswatch 4.6.2 Sass."
