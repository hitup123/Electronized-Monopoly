import React from 'react';



function playerCardIndividual({imageUrl}) {

  const PlayerCard = {
    backgroundColor: "grey",
    height: '400px',
    width: '300px',
    border: 'orange 2px solid',
    display: 'grid',
    gridTemplateRows: '50% 20% 20%',
    gridTemplateColumns: '20% 20% 20% 20% 20%'


  }

  const image = {
    height: 'auto',
    width: '100%',
  }
    
  const imageplate = {
    backgroundColor: 'white',
    gridColumn: '2/6',

  }

  const charname = {
    color: 'white',
    backgroundColor: 'orange',
    textAlign: 'center',    
    gridColumn: '1 / 2',
    gridRow: '1/2',
    writingMode: 'vertical-lr',
    fontSize: '30px',
    fontWeight: '500'
  } 

  const moneyplate = {
      backgroundColor: 'orangered',
      gridColumn: '1/6',
      gridRow: '2/3',
      textAlign: 'center'

  }

  const money = {
    color: 'white',
    fontSize: '40px',
    textAlign: 'center',
    fontWeight: '600'
  }

  const propertyplate = {
    display: 'flex',
    padding: '5px'
  }

  return (
    <div style={PlayerCard}>

      <p style={charname}>CAR</p>
      <div style={imageplate}>
        <img src={imageUrl} style={image} ></img>
      </div>

      <div style={moneyplate}>
        <p style={money}>1500</p>
      </div>

      <div style={propertyplate}>
        
      </div>
      
      
    </div>
  );
}

export default playerCardIndividual;
