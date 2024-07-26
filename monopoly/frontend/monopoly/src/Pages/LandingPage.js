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
      gridTemplateRows: '40% 20% 20% 20%'
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
      textAlign: 'center',
      fontSize: '30px',
      backgroundImage: 'linear-gradient(0deg, #B40014 10%, #CE000F 90%)',
      border: '4px solid #2E2E33',
      boxShadow: 'inset 0px 10px 30px rgba(255, 255, 255, 0.3)',
      fontFamily: 'DM Sans, sans-serif',
      fontOpticalSizing: 'auto',
      fontWeight: '1000',
      fontStyle: 'normal',
      color: 'white',
    }

    const playbutton = {
      gridRow: '4/5',
      height: '50px',
      width: '250px',
      border: 'outset #059212 4px',
      backgroundImage: 'radial-gradient(circle, #9CDBA6 10%, #50B498 90%)',
      position: 'relative',
      left: '50%',
      translate: '-50%',
      fontFamily: 'DM Sans, sans-serif',
      fontOpticalSizing: 'auto',
      fontWeight: '1000',
      fontStyle: 'normal',
      fontSize: '20px',
      color: '#DEF9C4'
    }
  
    return (
      <div id="page" style={landingcss}>
        <img alt="monopoly heading" src={icon} style={{ width: '700px', height: 'auto', position: 'relative', left: '50%', translate: '-50% 10%', gridRow: '1/2'}} />


        <div style={playmode}>
          <select style={dropdown} name='mode'>
            <option value='individual'>INDIVIDUAL</option>
            <option value='teams'>TEAMS</option>
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

        <button style={playbutton}>PLAY</button> 
      </div>
    );
  }

export default LandingPage;
