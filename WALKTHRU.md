# Environment

## Requirements

* python 2.7
* virtualenv

## Virtual Environment Setup

### Install VirtualENV
```
brew install virtualenv
```

### Initialize virtualenv
```
virtualenv .venv
```

```
virtualenv .venv --python=python2.7
```

### Activate virtualenv environment
```
source .venv/bin/activate
```

### Install nodedev
For NodeJS support
```
pip install nodeenv
```

### Initialize nodeenv
```
nodeenv .nenv
```

### Activate nodeenv environment
```
nodeenv .nenv/bin/activate
```

### Initialize NPM Package Management system
```
npm init
```

### Install Yarn NPM Manager
```
npm install -g yarn
```


## Package installation

### Install Python Packages
```
pip install Flask
pip install Flask-SQLAlchemy
```

### Install NPM development dependency packages via yarn
```
yarn add --dev webpack babel-core babel-loader babel-preset-react babel-preset-es2015 node-sass css-loader sass-loader style-loader
```

### Install NPM dependency packages via yarn
```
yarn add PACKAGE
```

### Create Directories
* server
```
mkdir -p nexus
```

* client
```
mkdir -p src
```

# Server Side
## Backend (model layer)
## Frontend (view layer)

# Client Side
## Backend (model layer)
## Frontend (view layer)

### References
* [Flask flaskr](http://flask.pocoo.org/docs/0.12/tutorial/)
* [Application Factories](http://flask.pocoo.org/docs/0.12/patterns/appfactories/)
* [Testing Flask Applications](http://flask.pocoo.org/docs/0.12/testing/#testing)

[What are NPM, Yarn, Babel, and Webpack; and how to properly use them?](https://medium.com/front-end-hacking/what-are-npm-yarn-babel-and-webpack-and-how-to-properly-use-them-d835a758f987)