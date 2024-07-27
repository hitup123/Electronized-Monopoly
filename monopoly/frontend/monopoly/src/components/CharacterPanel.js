import React from "react";

function charselect(event, togglePressed) {
    togglePressed();
    const obj = event.currentTarget;
    const img = obj.querySelector('img');
    const indicator = obj.querySelector('div');

    const isPressed = obj.getAttribute('data-pressed') === 'true';

    if (isPressed) {
        // Unpressed state
        obj.style.border = '5px outset';
        obj.style.borderRadius = '100%';
        obj.style.boxShadow = '';
        obj.style.transform = '';
        obj.setAttribute('data-pressed', 'false');
        indicator.style.backgroundColor = 'white';
        img.style.opacity = '1';
    } else {
        // Pressed state
        obj.style.border = '5px inset';
        obj.style.borderRadius = '100%';
        obj.style.boxShadow = 'inset 0 0 10px rgba(0, 0, 0, 0.5)';
        obj.style.transform = 'translateY(2px)';
        obj.setAttribute('data-pressed', 'true');
        indicator.style.backgroundColor = 'green';
        img.style.opacity = '0.8';
    }
}

function CharacterPanel({ name, imageURL, show, isPressed, togglePressed, team, handleTeamChange }) {
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
        height: '10px',
        width: '10px',
        borderRadius: '100%',
        position: 'relative',
        left: '50%',
        transform: 'translate(-50%, -300%)',
        backgroundColor: isPressed ? 'green' : 'white'
    };

    const teamselect = {
        display: show === 'teams' ? 'block' : 'none',
        position: 'relative',
        left: '50%',
        translate: '-50% 20%',
        backgroundColor: '#C5FF95',
        color: '#8576FF',
        fontSize: '15px',
        border: 'groove 5px #CDFADB',
        fontWeight: '700',
        fontFamily: 'DM Sans, sans-serif',

    };

    return (
        <div style={panelcss} onClick={(e) => charselect(e, togglePressed)} data-pressed={isPressed ? 'true' : 'false'}>
            <div style={indicator}></div>
            <img alt="image" src={imageURL} style={image} />
            <select style={teamselect} value={team} onChange={handleTeamChange}>
                <option value="team1">TEAM 1</option>
                <option value="team2">TEAM 2</option>
                <option value="team3">TEAM 3</option>
                <option value="team4">TEAM 4</option>
                <option value="team5">TEAM 5</option>
                <option value="team6">TEAM 6</option>
                <option value="team7">TEAM 7</option>
            </select>
        </div>
    );
}

export default CharacterPanel;
