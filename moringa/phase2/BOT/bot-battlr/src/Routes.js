import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import App from './App';
//import BotDetails from './BotDetails';
const MainRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route exact path="/" component={App} />
        <Route path="/
        bots/:botId" component={Route} />
      </Routes>
    </Router>
  );
};

export default MainRoutes;