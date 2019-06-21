# Requirements

* python 2.7
* virtualenv

# Activate Python virtualenv

virtualenv .venv
virtualenv .venv --python=python2.7

source .venv/bin/activate

# install python requirements

pip install -r requirements.txt


# Activate Node.js virtualenv

nodeenv .nenv

source .nenv/bin/activate

# install node requirements

npm install -g yarn

yarn install

# build UI

npm run build
npm run build-dev
npm run watch

# create config

app/config.py.example
