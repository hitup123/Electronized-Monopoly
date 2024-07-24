import React from "react";

function CharacterPanel({imageURL})
{
    const panelcss = {
        backgroundColor: 'rgb(255, 255, 255, 0.5)',
        height: '95%',
        width: '110px',
        borderRadius: '50px',
        display: 'inline-block'
    };

    const image = {
        height: '95%',
        width: 'auto'
    }

    return (
        <div style={panelcss}>
            <img alt="image" src={imageURL} style={image} />
        </div>
    );
}

export default CharacterPanel