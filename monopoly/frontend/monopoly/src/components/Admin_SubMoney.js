import React, { useState } from 'react';

const sendValue = (te, mon) => {
    const payload = { 
        team: te,
        amount: mon
     };

    fetch('/api/admin_submoney', {
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



function Admin_SubMoney() {
    const [hovered, setHovered] = useState(false);

    const transfer = {
        color: 'white',
        backgroundColor: hovered ? 'orangered' : 'orange',
        border: hovered ? 'double 10px white' : 'outset 10px orangered',
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

    const submoneyprotocol = () => {
        var amount = prompt("Enter the Amount");
        var team = prompt("Enter the Team Number");
        // alert(value);
        sendValue(team, amount);
    };

    return (
       <button
           style={transfer}
           onClick={submoneyprotocol}
           onMouseEnter={handleMouseEnter}
           onMouseLeave={handleMouseLeave}
       >
           Subtract
       </button>
    );
}

export default Admin_SubMoney;