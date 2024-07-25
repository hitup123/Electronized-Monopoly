import React from "react";

function CharacterPanel({imageURL})
{
    const panelcss = {
        backgroundColor: 'rgb(255, 255, 255, 0.5)',
        height: '95%',
        width: '110px',
        borderRadius: '100%',
        padding: '5px',
        margin: '5px',
        border: '5px outset '
    };

    const image = {
        height: '95%',
        width: 'auto',
        position: 'relative',
        left: '50%',
        translate: '-50% 0%'
    }

    return (
        <div style={panelcss}>
            <img alt="image" src={imageURL} style={image} />
        </div>
    );
}

export default CharacterPanel