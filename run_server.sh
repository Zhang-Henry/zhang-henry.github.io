#!/usr/bin/env bash
set -euo pipefail

if [ -d /usr/local/opt/ruby/bin ]; then
  export PATH="/usr/local/opt/ruby/bin:$PATH"
fi

bundle exec jekyll serve --livereload
