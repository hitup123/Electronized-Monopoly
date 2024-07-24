import React from 'react';
import './Page.css'
import PlayerCard from '../components/playerCard';
import car  from '../Images/car.webp';
import horse from '../Images/horse.png';
import cannon from '../Images/cannon.png';
import hat from '../Images/hat.webp';

function HomePage() {
  return (
    <div id='page'>
      <PlayerCard imageUrl={car}/>
      <PlayerCard imageUrl={horse}/>
      <PlayerCard imageUrl={cannon}/>
    </div>
  );
}

export default HomePage;
