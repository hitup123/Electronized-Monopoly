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
import shoe from '../Images/shoe.png';
import iron from '../Images/iron.png';


function LandingPage() {

    const landingcss = {
      backgroundColor: '#D6EFD8',
      display: 'grid',
      gridTemplateRows: '50% 20% 30%'
    };

    const selectionpanelcss = {
        height: '100px',
        width: '100%',
        display: 'flex',
        flexDirection: 'row',
        flexWrap: 'no-wrap',
        justifyContent: 'center',
        gridRow: '3/4'

    };

    const playmode = {
        height: '100px',
        width: '100%',
        gridRow: '2/3',
    }

    const dropdown = {
      position: 'relative',
      left: '50%',
      translate: '-50%',
      height: '60%',
      width: '20%',
      borderRadius: '100px',
      textAlign: 'center',
      fontSize: '30px'
    }
  
    return (
      <div id="page" style={landingcss}>
        <img alt="monopoly heading" src={icon} style={{ width: '700px', height: 'auto', position: 'relative', left: '50%', translate: '-50% 10%', gridRow: '1/2'}} />


        <div style={playmode}>
          <select style={dropdown} name='mode'>
            <option value='individual'>Individual</option>
            <option value='teams'>Teams</option>
          </select>
    
        </div>
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
