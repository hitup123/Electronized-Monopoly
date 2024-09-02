import React, { useEffect, useRef } from 'react';
import ReactDOM from 'react-dom';
import './EventPanel.css';

import CommunityEvent from './Events/CommunityEvent';
import ChanceEvent from './Events/ChanceEvent';

function EventPanel() {
    const iframeRef = useRef(null);

    useEffect(() => {
        const iframeDoc = iframeRef.current.contentDocument || iframeRef.current.contentWindow.document;
        iframeDoc.open();
        iframeDoc.write('<!DOCTYPE html><html><head><style></style></head><body><div id="iframe-root"></div></body></html>');
        iframeDoc.close();

        // Here you can render any React component inside the iframe
        var eventType;

        if(eventType)
        {
            ReactDOM.render(<CommunityEvent />, iframeDoc.getElementById('iframe-root'));
        }
        else
        {
            ReactDOM.render(<ChanceEvent />, iframeDoc.getElementById('iframe-root'));
        }
    }, []);

    return (
        <div id="eventpanel">
            <iframe ref={iframeRef} title="Event Panel" width="100%" height="400px" frameBorder="0"></iframe>
        </div>
    );
}

export default EventPanel;
