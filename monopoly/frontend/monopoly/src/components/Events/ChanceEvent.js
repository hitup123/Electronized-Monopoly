import React from "react";

function ChanceEvent()
{
    const card = {
        backgroundColor: "rgb(0, 0, 0, 0.5)",
        height: '90%',
        width: '90%',
        position: 'relative',
        left: '50%',
        top: '50%',
        translate: '-50% -50%',
        textAlign: 'center',
    }


    return (<>
        <div style={card}>
            <h2>CHANCE</h2>
            <p>Pay 20 Euro</p>
        </div>
    </>)
}

export default ChanceEvent;