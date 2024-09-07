import React from "react";


function BuyProperty({action, message}) 
{
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


    return <>
        <div style={card}>
            <h2>{action}</h2>
            <p>{message}</p>
        </div> 
        </>
}

export default BuyProperty;
