Nov 28, 2017

make sure you are working off the latest info from github.

git pull

make sure you activate the virtualenv first.

 source activate py3

then you can run the jupyter notebook:

 jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser

then you can commmit your changes

git add .
git commit -m "updated with work"
git push origin master 
