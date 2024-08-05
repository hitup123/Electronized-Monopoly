import React from "react";  

import PlayerCardTeam from "./playerCardTeam";
import Property from "./Property";

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

function PlayerCardTeamObject()
{
    const playericonplate = {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'center',
        backgroundColor: 'rgb(255,255,255,0.5)',
        gridRows: '1/2',
        gap: '10px',
        alignItems: 'center',
    }
    const icons =[
        {
            p1: car,
            p2: iron
        },
        {
            p1: horse,
            p2: cannon
        },
        {
            p1: hat,
            p2: ship
        }
    ];

    const iconobj = icons.map((element) => {
        return (<>
            <PlayerCardTeam imageUrl={element.p1}></PlayerCardTeam>
            <PlayerCardTeam imageUrl={element.p2}></PlayerCardTeam></>
        );
    });

    return <div style={playericonplate}>{iconobj}</div>
}

function Team({balance})
{
    const teamplate = {
        padding: '5px',
        backgroundColor: 'darkgrey', 
        minHeight: '300px', 
        height: 'fit-content',
        width: 'fit-content',
        display: 'grid',
        gridTemplateRows: '40% 15% 35% 10%', 
        borderRadius: '5px', 
    }

    

    const moneyplate= {
        gridRows: '2/3',
        width: '100%',
        height: '100%',
        backgroundColor: 'orange',
        opacity: '0.5',
        textAlign: 'center',
        color: 'rgb(255,255,255,1)',
        fontSize: '30px' 
    }

    const propertyplate = {
        gridRows: '3/4',
        display: 'flex',
        justifyContent: 'flex-start',
        flexDirection: 'row',
        flexWrap: 'wrap',
        padding: '5px',
    }

    const teamstatus = {
        gridRows: '4/5',
        backgroundColor: 'lightgreen',
        height: '100%',
        color: 'white', 
        textAlign: 'center',
        fontWeight: '700',  

    }

    return (
        <div style={teamplate}>
            
            <PlayerCardTeamObject></PlayerCardTeamObject>

            <div style={moneyplate}>
                <p>{balance}</p>
            </div>

            <div style={propertyplate}>
                <Property propertyname ="Old Kent Road"></Property>
                <Property propertyname ="Mayfair"></Property>
                <Property propertyname ="Pall Mall"></Property>
                <Property propertyname ="Bond Street"></Property>
                <Property propertyname ="Whitehall"></Property>
            </div>

            <div style={teamstatus}>
                <p>PLAYING</p>
            </div>



        </div>
    )
}

export default Team;