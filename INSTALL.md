# Requirements

* python 3.6
* virtualenv

# Activate Python virtualenv

python -m venv .venv

source .venv/bin/activate

# Copy venv activate_this file

cp activate_this.py .venv/bin/activate_this.py

# install python requirements

pip install -r requirements.txt

# Activate Node.js virtualenv

nodeenv -p .venv

# install node requirements

npm install -g yarn

yarn install

# build UI

npm run build
npm run build-dev
npm run watch

# create config

app/config.py.example

# Shallow clone
git clone REPO --depth=1

# update clone

git pull --depth=1
git gc --prune=all

# install backend in edit mode
 pip install -e nexus

# run 
 FLASK_ENV=development FLASK_APP=nexus flask run
