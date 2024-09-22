import React, { useState } from 'react';

const sendValue = (te, amt) => {
    const payload = { team: te,
        amount: amt
     };

    fetch('/api/get_tax', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
  };



function GetTax() {
    const [hovered, setHovered] = useState(false);

    const transfer = {
        color: 'white',
        backgroundColor: hovered ? 'orangered' : 'orange',
        border: hovered ? 'outset 10px white' : 'outset 10px orangered',
        height: '70px',
        width: '200px',
        fontSize: '40px',
        transition: 'background-color 0.3s, border-color 0.3s'
    };

    const handleMouseEnter = () => {
        setHovered(true);
    };

    const handleMouseLeave = () => {
        setHovered(false);
    };

    const Taxprotocol = () => {
        var amount = prompt("Enter the Tax Amount");
        var team = prompt("Enter the Team Number");
        // alert(value);
        sendValue(team, amount);
    };

    return (
       <button
           style={transfer}
           onClick={Taxprotocol}
           onMouseEnter={handleMouseEnter}
           onMouseLeave={handleMouseLeave}
       >
           Tax
       </button>
    );
}

export default GetTax;