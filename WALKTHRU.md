# Environment

## Requirements

* python 2.7
* virtualenv

## Virtual Environment Setup

### Install VirtualENV with brew
```
brew install virtualenv
```

### Install Virtual env with pip
```
pip install --user virtualenv
```

### Initialize virtualenv
```
virtualenv .venv
```

```
virtualenv .venv --python=python3
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

### Initialize nodeenv and utilize existing python venv
```
nodeenv -p
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
 mkdir -p /home/user/mysite/{public_html/{css,js,images},logs}
* client
```
mkdir -p src
```

# Client Side
## Event Layer
* Event Interface
* Event Handler
## View Layer
* View Interface
* View Handler
* Data Client
## Data Layer
* Data Interface
* Data Handler
* Resource Client
## Resource Layers
* Resource Interface
* Resource Handler
* Resource Client

# Server Side
## API Layer
* API Interface
* API Handler
* Data Client
## Data Layer
* Data Interface
* Data Handler
* Resource Clien
## Resource Layers
* Resource Interface
* Resource Handler

### References
* [Flask flaskr](http://flask.pocoo.org/docs/0.12/tutorial/)
* [Application Factories](http://flask.pocoo.org/docs/0.12/patterns/appfactories/)
* [Testing Flask Applications](http://flask.pocoo.org/docs/0.12/testing/#testing)

[What are NPM, Yarn, Babel, and Webpack; and how to properly use them?](https://medium.com/front-end-hacking/what-are-npm-yarn-babel-and-webpack-and-how-to-properly-use-them-d835a758f987)

