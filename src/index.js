import _ from 'lodash';

import React from 'react';
import ReactDOM from 'react-dom';
import {
    BrowserRouter as Router,
    Link,
    Route,
    Switch
} from 'react-router-dom';

let baseURL = window.baseURL;

import Home from './home';

const About = () => (
    <div>
        <h1>About</h1>
    </div>
);

const Child = ({match}) => (
    <div>
        <h3>ID: {match.params.id}</h3>
    </div>
);

const Main = () => (
  <Router basename={baseURL}>
    <div>
      <h2>Accounts</h2>
      <ul>
        <li><Link to="/">Default</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><a href={baseURL+"/home"}>Home</a></li>
        <li><a href={baseURL+"/test"}>Test Directory</a></li>
        <li><Link to="/Exercises">Exercises</Link></li>
        <li><Link to="/Skills">Skills</Link></li>
        <li><Link to="/Courses">Courses</Link></li>
      </ul>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="/:id" component={Child} />
      </Switch>
    </div>
  </Router>
);

ReactDOM.render(<Main />, document.getElementById('container'));
