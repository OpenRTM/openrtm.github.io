#!/bin/bash


#python3 ~/jekyll_workdir/openrtm_test/bin/pukiwiki_to_md9_old.py
python3 /home/openrtm/jekyll_workdir/openrtm_test/bin/pukiwiki_to_md9_old.py
cat output.md >>index.md
#python3 ~/jekyll_workdir/openrtm_test/bin/dl_image3_fixed.py --start_url https://openrtm.org/openrtm/ja/node/"$1"
python3 /home/openrtm/jekyll_workdir/openrtm_test/bin/dl_image3_fixed.py --start_url https://openrtm.org/openrtm/ja/node/"$1"

rm logo.png ja.png en.png share_save_171_16.png

sed -i 's/width="100%;"/width="60%;"/g' index.md
