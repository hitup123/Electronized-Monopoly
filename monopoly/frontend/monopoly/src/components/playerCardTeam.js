import React from 'react';



function PlayerCardTeam({imageUrl}) {

  const PlayerCard = {
    backgroundColor: "grey",
    height: 'fit-content',
    width: 'fit-content',
    border: 'orange 2px solid',
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',


  }

  const image = {
    height: '100px',
    width: 'auto',
    gridRow: '1/2',

  }

  return (
    <div style={PlayerCard}>

      <img src={imageUrl} style={image} ></img>
      
      
    </div>
  );
}

export default PlayerCardTeam;
