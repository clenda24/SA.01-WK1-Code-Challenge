import React from 'react';
import BotCard from './BotCard';

function BotList({ bots }) {
  return (
    <div className="bot-section">
        <div>
            <h2>Bot List</h2>
            <div>
                {bots.map(bot => (
                    <BotCard {...bot}/>
                ))}
            </div>
        </div>

    </div>
  );
}

export default BotList;