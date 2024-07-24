import React from 'react';



function PlayerCard({imageUrl}) {

  const PlayerCard = {
    backgroundColor: "green",
    height: '400px',
    width: '250px',
    borderRadius: '30px',
    border: 'black 2px solid'
  }

  const image = {
    height: '170px',
    width: 'auto'
  }

  return (
    <div style={PlayerCard}>
      <img src={imageUrl} style={image} ></img>
    </div>
  );
}

export default PlayerCard;
