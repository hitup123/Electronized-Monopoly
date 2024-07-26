import React, { useState } from "react";

function charselect(event) {
    const obj = event.currentTarget;
    const isPressed = obj.getAttribute('data-pressed') === 'true';
    const statusled = obj.children[1];

    if (isPressed) {
        // Unpressed state
        obj.style.border = '5px outset';
        obj.style.borderRadius = '100%';
        obj.style.boxShadow = '';
        obj.style.transform = '';
        obj.setAttribute('data-pressed', 'false');
        statusled.style.backgroundColor = 'white';
    } else {
        // Pressed state
        obj.style.border = '5px inset';
        obj.style.borderRadius = '100%';
        obj.style.boxShadow = 'inset 0 0 10px rgba(0, 0, 0, 0.5)';
        obj.style.transform = 'translateY(2px)';
        obj.setAttribute('data-pressed', 'true');
        statusled.style.backgroundColor = 'green';

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
        border: 'outset grey 1px',
        borderRadius: '100%',
        position: 'relative',
        left: '50%',
        top: '-120%',
        translate: '-50%'
    }

    return (
        <div style={panelcss} onClick={charselect} data-pressed="false">
            <img alt="image" src={imageURL} style={image} />
            <div style={indicator}></div>
        </div>
    );
}

export default CharacterPanel;
