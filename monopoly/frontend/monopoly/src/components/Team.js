import React from "react";  

import PlayerCardTeam from "./playerCardTeam";
import Property from "./Property";

function PlayerCardTeamObject({icon})
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
    
    console.log(icon);

    const iconobj = icon.map((element) => {
        return (<>
            <PlayerCardTeam imageUrl={element.ico}></PlayerCardTeam>
</>
        );
    });

    return <div style={playericonplate}>{iconobj}</div>
}

function Team({balance, status, icons})
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
    console.log(icons);

    return (
        <div style={teamplate}>
            
            <PlayerCardTeamObject icon={icons}></PlayerCardTeamObject>

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
                <p>{status}</p>
            </div>



        </div>
    )
}

export default Team;