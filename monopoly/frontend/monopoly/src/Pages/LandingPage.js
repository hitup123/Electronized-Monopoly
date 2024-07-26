import React from 'react';
import './Page.css'
import icon from '../Images/monoplyHeading.png';
import CharacterPanel from '../components/CharacterPanel';

import car  from '../Images/car.webp';
import horse from '../Images/horse.avif';
import cannon from '../Images/cannon.png';
import hat from '../Images/hat.png';
import dog from '../Images/dog.png';
import wheelbarrow from '../Images/wheelbarrow.png';
import dustbin from '../Images/dustbin.webp';
import ship from '../Images/ship.webp';
import iron from '../Images/iron.png';
import shoe from '../Images/shoe.png';



function LandingPage() {

    const landingcss = {
      backgroundColor: '#D6EFD8',
      display: 'grid',
      gridTemplateRows: '50% 50%'
    };

    const selectionpanelcss = {
        height: '100px',
        width: '100%',
        display: 'flex',
        flexDirection: 'row',
        flexWrap: 'no-wrap',
        justifyContent: 'center'
    };
  
    return (
      <div id="page" style={landingcss}>
        <img alt="monopoly heading" src={icon} style={{ width: '700px', height: 'auto', position: 'relative', left: '50%', translate: '-50% 10%'}} />

        <div id='character_selection_panel' style={selectionpanelcss}>
            <CharacterPanel imageURL={cannon} />
            <CharacterPanel imageURL={car} />
            <CharacterPanel imageURL={dog} />
            <CharacterPanel imageURL={dustbin} />
            <CharacterPanel imageURL={hat} />
            <CharacterPanel imageURL={horse} />
            <CharacterPanel imageURL={wheelbarrow} />
            <CharacterPanel imageURL={ship} />
            <CharacterPanel imageURL={shoe} />
            <CharacterPanel imageURL={iron} />
        </div>
      </div>
    );
  }

export default LandingPage;
