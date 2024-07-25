import React from 'react';
import './Page.css'
import PlayerCard from '../components/playerCard';
import car  from '../Images/car.webp';
import horse from '../Images/horse.avif';
import cannon from '../Images/cannon.png';
import hat from '../Images/hat.png';
import TransferButton from '../components/TransferButton';

function HomePage() {

  const landingpage = {
    display: 'grid',
    gridTemplateRows: '70% 30%',
    overflow: 'hidden'
  }

  const playercardpanel = {
    gridRows: '1/2',
    backgroundColor: 'grey',
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center'
  }

  const buttonplate = {
    gridRows: '2/3',
    backgroundColor: 'darkgrey',
    borderTop: 'outset 5px orangered'
  }

  return (
    <div id='page' style={landingpage}>
      <div style={playercardpanel}>
      <PlayerCard imageUrl={car}/>
      </div>
      <div style={buttonplate}>
        <TransferButton />

      </div>
      

    </div>
  );
}

export default HomePage;
