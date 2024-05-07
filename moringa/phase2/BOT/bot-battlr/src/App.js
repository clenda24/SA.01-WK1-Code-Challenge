import React from 'react';
import MainRoutes from './Routes';
import BotCollection from './BotCollection';

const App = () => {
 // const bots = []
  return (
    <div>
      <h1>Bot Battlr</h1>
      <BotCollection/>
      <MainRoutes />
    </div>
  );
};
export default App;