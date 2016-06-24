#!/bin/sh

cd /home/bindel/work/scan-seminar/
git pull origin
jekyll build
cd _site
rc=$(mktemp)

{
    echo "open https://static-webdav.kproxy.cornell.edu/cse" 
    find "." -type d | xargs -I{} echo 'mkcol scan/'{}
    find "." -type f \
    -exec echo 'cd scan/'$(dirname {}) \; \
    -exec echo 'lcd '$(dirname {}) \; \
    -exec echo 'mput '$(basename {}) \; \
    -exec echo 'cd -' \; \
    -exec echo 'lcd /home/bindel/work/scan-seminar/_site' \;
    echo "quit";
} > "$rc";

cadaver -r "$rc" "$@" 
rm -f "$rc"
echo "Finished upload"
