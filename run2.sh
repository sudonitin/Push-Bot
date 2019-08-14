git init
git remote add origin https://github.com/globefire/Goals.git
git pull origin master
python ./app.py
git add .
git commit -m "a new commit"
git push origin master