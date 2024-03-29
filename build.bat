git pull
cd taelgar
git reset --hard
cd ..
git submodule update --remote --rebase
python taelgar-utils/website/build_mkdocs_site.py
