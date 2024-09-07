import React from 'react';
import './EventPanel.css';

import CommunityEvent from './Events/CommunityEvent';
import ChanceEvent from './Events/ChanceEvent';
import BuyProperty from './Events/BuyProperty';

function EventPanel({ eventType, one, two, three }) { // eventType is received as a prop

    let content;

    if (eventType == 'community') {
        content = <CommunityEvent />;
    } 
    else if(eventType == 'chance')
    {
        content = <ChanceEvent />;
    }
    else if(eventType == 'buy')
    {
        content = <BuyProperty  action = {eventType} message={one}/>;
    }

    return (
        <div id="eventpanel">
            {content}
        </div>
    );
}

export default EventPanel;
