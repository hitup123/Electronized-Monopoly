import React from "react";  

import PlayerCardTeam from "./playerCardTeam";
import car from '../Images/car.webp';
import horse from '../Images/horse.avif';
import cannon from '../Images/cannon.png';
import hat from '../Images/hat.png';
import dog from '../Images/dog.png';
import wheelbarrow from '../Images/wheelbarrow.png';
import dustbin from '../Images/dustbin.webp';
import ship from '../Images/ship.webp';
import shoe from '../Images/shoe.png';
import iron from '../Images/iron.png';

function Team()
{
    const teamplate = {
        padding: '10px',
        backgroundColor: 'green',
        display: 'inline-block',
        height: 'fit-content',
        width: 'fit-content',
        display: 'grid',
        gridTemplateRows: '50% 40% 10%', 
    }

    const playericonplate = {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'center',
        backgroundColor: 'rgb(255,255,255,0.5)',
        height: '400px',
        width: '400px',
        gridRows: '1/2',
        gap: '10px',
    }

    const moneyplate= {
        gridRows: '2/3',
        width: '100%',
        backgroundColor: 'orange',
        height: '40%',
        opacity: '0.5',
    }

    return (
        <div style={teamplate}>
            
            <div style={playericonplate}>
                <PlayerCardTeam imageUrl={car}></PlayerCardTeam>
                <PlayerCardTeam imageUrl={shoe}></PlayerCardTeam>
            </div>
            <div style={moneyplate}></div>

        </div>
    )
}

export default Team;