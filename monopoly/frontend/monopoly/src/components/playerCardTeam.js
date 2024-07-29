import React from 'react';



function PlayerCardTeam({imageUrl}) {

  const PlayerCard = {
    backgroundColor: "grey",
    height: 'fit-content',
    width: 'fit-content',
    border: 'orange 2px solid',
    display: 'grid',
    gridTemplateRows: '60% 40%',    

  }

  const image = {
    height: 'auto',
    width: '150px',
    gridRow: '1/2',

  }

  const propertyplate = {
    gridRow: '2/3',
    padding: '10px',
  }

  return (
    <div style={PlayerCard}>

    <img src={imageUrl} style={image} ></img>

    <div style={propertyplate}>
        <ul>
            <li>Pall Mall</li>
            <li>Pall Mall</li>
            <li>Pall Mall</li>
            <li>Pall Mall</li>
        </ul>
        
    </div>
      
      
    </div>
  );
}

export default PlayerCardTeam;
