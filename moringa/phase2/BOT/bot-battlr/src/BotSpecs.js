import React from 'react';
import { useParams } from 'react-router-dom';

function BotSpecs() {
  const history = useHistory();
  const { botId } = useParams();
  return (
    <div className="bot-specs">
      <h2>Bot Specs</h2>
      <button onClick={() => history.push('/')}>Back to List</button>
      <button onClick={() => console.log(`Enlisting bot ${botId}`)}>Enlist Bot</button>
    </div>
  );
}
export default BotSpecs;