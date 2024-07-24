import React from 'react';
import './Page.css'
import icon from '../Images/monoplyHeading.png';
import CharacterPanel from '../components/CharacterPanel';
import car  from '../Images/car.webp';
import horse from '../Images/horse.png';
import cannon from '../Images/cannon.png';
import hat from '../Images/hat.webp';



function LandingPage() {

    const landingcss = {
      backgroundColor: '#F0F567',
      textAlign: 'center', // Center the text and image
    };

    const selectionpanelcss = {
        backgroundColor: '#E8E821',
        height: '100px',
        width: '40%',
        borderRadius: '50px',
        border: 'solid 5px gold'
    };
  
    return (
      <div id="page" style={landingcss}>
        <img alt="monopoly heading" src={icon} style={{ width: '700px', height: 'auto', position: 'relative', top: '50px'}} />

        <div id='character_selection_panel' style={selectionpanelcss}>
            <CharacterPanel imageURL={horse} />
            <CharacterPanel imageURL={cannon} />
            <CharacterPanel imageURL={car} />
            <CharacterPanel imageURL={hat} />
        </div>
      </div>
    );
  }

export default LandingPage;
