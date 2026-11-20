#!/usr/bin/env bash
set -euo pipefail

# Download fixed upstream versions into the built Pages artifact.
# This avoids external script/style requests from visitors' browsers.
mkdir -p _site/assets/js/vendor _site/assets/css/vendor

fetch() {
  local url="$1" destination="$2"
  curl --fail --location --silent --show-error --retry 3 --retry-delay 2 --proto '=https' --tlsv1.2 "$url" -o "$destination"
  test -s "$destination"
  echo "Downloaded $(basename "$destination"): $(wc -c < "$destination") bytes"
  sha256sum "$destination"
}

fetch "https://unpkg.com/simple-jekyll-search@1.10.0/dest/simple-jekyll-search.min.js" "_site/assets/js/vendor/simple-jekyll-search.min.js"
fetch "https://cdn.jsdelivr.net/npm/swiper@12.2.0/swiper-bundle.min.js" "_site/assets/js/vendor/swiper-bundle.min.js"
fetch "https://cdn.jsdelivr.net/npm/swiper@12.2.0/swiper-bundle.min.css" "_site/assets/css/vendor/swiper-bundle.min.css"

# Bootstrap 4.6.2 official bundle includes Popper.js 1.16.1.
# Verify the upstream-published SRI digest before including it in the Pages artifact.
bootstrap_bundle="_site/assets/js/vendor/bootstrap-4.6.2.bundle.min.js"
fetch "https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" "$bootstrap_bundle"
expected_sha384="Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct"
actual_sha384="$(openssl dgst -sha384 -binary "$bootstrap_bundle" | openssl base64 -A)"
if [[ "$actual_sha384" != "$expected_sha384" ]]; then
  echo "Bootstrap bundle SHA-384 mismatch; refusing to deploy" >&2
  exit 1
fi
echo "Bootstrap 4.6.2 bundle SHA-384 verified"
