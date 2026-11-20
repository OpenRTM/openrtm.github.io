# frozen_string_literal: true
# Wrap the original OpenRTM logo in a square SVG viewport without distortion.
# Embedding the PNG is important: browsers may reject external image references
# inside SVG favicons.
require "base64"
require "fileutils"

source = "assets/rtm_images/rtm_logo.png"
destination = "_site/assets/rtm_images/favicon.svg"
image_data = Base64.strict_encode64(File.binread(source))
svg = <<~SVG
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
    <image x="0" y="0" width="64" height="64"
           preserveAspectRatio="xMidYMid meet"
           href="data:image/png;base64,#{image_data}"/>
  </svg>
SVG
FileUtils.mkdir_p(File.dirname(destination))
File.write(destination, svg)
