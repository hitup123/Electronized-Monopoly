import React from 'react';
import './EventPanel.css';

import CommunityEvent from './Events/CommunityEvent';
import ChanceEvent from './Events/ChanceEvent';

function EventPanel({ eventType }) { // eventType is received as a prop

    let content;

    if (eventType) {
        content = <CommunityEvent />;
    } else {
        content = <ChanceEvent />;
    }

    return (
        <div id="eventpanel">
            {content}
        </div>
    );
}

export default EventPanel;
