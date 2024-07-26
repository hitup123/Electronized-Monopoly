import React from "react";

function charselect(event) {
    const obj = event.currentTarget;
    const img = obj.children[0]; // Access the first child element (the img)

    const isPressed = obj.getAttribute('data-pressed') === 'true';

    const child = obj.children[0];

    if (isPressed) {
        // Unpressed state
        obj.style.border = '5px outset';
        obj.style.borderRadius = '100%';
        obj.style.boxShadow = '';
        obj.style.transform = '';
        obj.setAttribute('data-pressed', 'false');
        child.style.backgroundColor = 'white';


        // Example of accessing the img child to reset any changes
        img.style.opacity = '1'; // Reset any changes made to the img
    } else {
        // Pressed state
        obj.style.border = '5px inset';
        obj.style.borderRadius = '100%';
        obj.style.boxShadow = 'inset 0 0 10px rgba(0, 0, 0, 0.5)';
        obj.style.transform = 'translateY(2px)';
        obj.setAttribute('data-pressed', 'true');

        // Example of accessing the img child to make changes
        img.style.opacity = '0.8'; // Change opacity of the img when pressed
        child.style.backgroundColor = 'green';
    }
}

function CharacterPanel({ imageURL }) {
    const panelcss = {
        backgroundColor: 'rgba(255, 255, 255, 0.5)',
        height: '95%',
        width: '110px',
        borderRadius: '100%',
        padding: '5px',
        margin: '5px',
        border: '5px outset',
        transition: 'all 0.1s ease'
    };

    const image = {
        height: '95%',
        width: 'auto',
        position: 'relative',
        left: '50%',
        transform: 'translateX(-50%)'
    };

    const indicator = {
        height: '5px',
        width: '5px',
        borderRadius: '100%',
        position: 'relative',
        left: '50%',
        translate: '-50% -500%',
        backgroundColor: 'white'
    }

    return (
        <div style={panelcss} onClick={charselect} data-pressed="false">
            <div style={indicator}></div>
            <img alt="image" src={imageURL} style={image} />
        </div>
    );
}

export default CharacterPanel;
