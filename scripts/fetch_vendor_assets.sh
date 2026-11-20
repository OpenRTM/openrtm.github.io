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
