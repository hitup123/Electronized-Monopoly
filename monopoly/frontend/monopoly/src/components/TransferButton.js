import React from "react";

function TransferButton()
{
    const transfer = {
        color: 'white',
        backgroundColor: 'orange',
        border: 'outset 10px orangered',
        height: '70px',
        width: '200px',
        fontSize: '40px'
    }
    return (
       <button style={transfer}>Transfer</button>
    );
}

export default TransferButton;