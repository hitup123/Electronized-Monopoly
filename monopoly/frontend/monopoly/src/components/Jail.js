import React, { useState } from 'react';

const sendValue = (x) => {
    const payload = { value: x };

    fetch('/api/gojail', {
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



function GoToJail() {
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

    const jailprotocol = () => {
        var value = prompt("Enter the Team Number");
        // alert(value);
        sendValue(value)
    };

    return (
       <button
           style={transfer}
           onClick={jailprotocol}
           onMouseEnter={handleMouseEnter}
           onMouseLeave={handleMouseLeave}>
           Jail
       </button>
    );
}

export default GoToJail;