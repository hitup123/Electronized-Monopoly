import React from 'react';
import './EventPanel.css';

function EventPanel({ eventType, msg, teamname, money }) { // eventType is received as a prop

    let content;

    const card = {
        backgroundColor: "rgb(255, 255, 255, 0.8)",
        height: '90%',
        width: '90%',
        position: 'relative',
        left: '50%',
        top: '50%',
        translate: '-50% -50%',
        textAlign: 'center',
    }

    if (eventType == 'community') 
    {
        content = "COMMUNITY CARD";
    } 
    else if(eventType == 'chance')
    {
        content = "CHANCE CARD";
    }
    else if(eventType == 'buy' || eventType == "buyingfailed")
    {
        content = "BUYING PROPERTY";
    }
    else if(eventType == 'sell')
    {
        content = "SELLING PROPERTY";
    }
    else if(eventType == 'auction')
    {
        content = "AUCTION";
    }
    else if(eventType == "build")
    {
        content = "BUILDING HOUSES AND HOTELS";
    }
    else if(eventType == "rent")
    {
        content = "RENT";
    }
    else if(eventType == "mortgage" || eventType == "unmortgage")
    {
        content = "MORTGAGE";
    }
    else if(eventType == "bankrupt")
    {
        content = "BANKRUPTCY";
    }
    else
    {
        content = "EVENT";
    }
    
    return (
        <div id="eventpanel">
            <div style={card}>
                <h2>{content}</h2>
                <p>{msg}</p>
            </div> 
        </div>
    );
}

export default EventPanel;
