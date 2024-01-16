git pull
git submodule update
pushd taelgar
git checkout main
git pull
popd
pushd taelgarverse-site-generator
git checkout main
git pull
popd
python run.py
git add .
git commit -m "Autobuild website"
pushd taelgar
git reset --hard
popd 