import React, { useState } from 'react';
import './Page.css';
import icon from '../Images/monoplyHeading.png';
import CharacterPanel from '../components/CharacterPanel';

import car from '../Images/car.webp';
import horse from '../Images/horse.avif';
import cannon from '../Images/cannon.png';
import hat from '../Images/hat.png';
import dog from '../Images/dog.png';
import wheelbarrow from '../Images/wheelbarrow.png';
import dustbin from '../Images/dustbin.webp';
import ship from '../Images/ship.webp';
import shoe from '../Images/shoe.png';
import iron from '../Images/iron.png';

let gamemodes;

function sendjson(characterStates) {
  const jsonpacket = {
    GameMode: gamemodes,
    Characters: characterStates.map(({ name, isPressed, team }) => ({
      name,
      isPressed,
      team,
    })),
  };
  console.log(jsonpacket); // This line is just for testing
}

function LandingPage() {
  const [show, setShow] = useState('individual');
  const [characterStates, setCharacterStates] = useState([
    { name: 'Cannon', imageURL: cannon, isPressed: false, team: 'team1' },
    { name: 'Car', imageURL: car, isPressed: false, team: 'team1' },
    { name: 'Dog', imageURL: dog, isPressed: false, team: 'team1' },
    { name: 'Dustbin', imageURL: dustbin, isPressed: false, team: 'team1' },
    { name: 'Hat', imageURL: hat, isPressed: false, team: 'team1' },
    { name: 'Horse', imageURL: horse, isPressed: false, team: 'team1' },
    { name: 'Wheelbarrow', imageURL: wheelbarrow, isPressed: false, team: 'team1' },
    { name: 'Ship', imageURL: ship, isPressed: false, team: 'team1' },
    { name: 'Shoe', imageURL: shoe, isPressed: false, team: 'team1' },
    { name: 'Iron', imageURL: iron, isPressed: false, team: 'team1' },
  ]);

  const changemode = (event) => {
    setShow(event.target.value);
    gamemodes = event.target.value === 'teams' ? 1 : 0;
  };

  const togglePressed = (index) => {
    setCharacterStates((prevStates) =>
      prevStates.map((state, i) =>
        i === index ? { ...state, isPressed: !state.isPressed } : state
      )
    );
  };

  const handleTeamChange = (index, newTeam) => {
    setCharacterStates((prevStates) =>
      prevStates.map((state, i) =>
        i === index ? { ...state, team: newTeam } : state
      )
    );
  };

  const landingcss = {
    backgroundColor: '#D6EFD8',
    display: 'grid',
    gridTemplateRows: '40% 20% 20% 20%',
  };

  const selectionpanelcss = {
    height: '100px',
    width: '100%',
    display: 'flex',
    flexDirection: 'row',
    flexWrap: 'nowrap',
    justifyContent: 'center',
    gridRow: '3/4',
  };

  const playmode = {
    height: '100px',
    width: '100%',
    gridRow: '2/3',
  };

  const dropdown = {
    position: 'relative',
    left: '50%',
    transform: 'translateX(-50%)',
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
  };

  const playbutton = {
    gridRow: '4/5',
    height: '50px',
    width: '250px',
    border: 'outset #059212 4px',
    backgroundImage: 'radial-gradient(circle, #9CDBA6 10%, #50B498 90%)',
    position: 'relative',
    left: '50%',
    translate:  '-50% 50%',
    fontFamily: 'DM Sans, sans-serif',
    fontOpticalSizing: 'auto',
    fontWeight: '1000',
    fontStyle: 'normal',
    fontSize: '20px',
    color: '#DEF9C4',
  };

  return (
    <div id="page" style={landingcss}>
      <img
        alt="monopoly heading"
        src={icon}
        style={{
          width: '700px',
          height: 'auto',
          position: 'relative',
          left: '50%',
          transform: 'translateX(-50%)',
          gridRow: '1/2',
        }}
      />

      <div style={playmode}>
        <select style={dropdown} name="mode" onChange={changemode}>
          <option value="individual">INDIVIDUAL</option>
          <option value="teams">TEAMS</option>
        </select>
      </div>

      <div id="character_selection_panel" style={selectionpanelcss}>
        {characterStates.map((character, index) => (
          <CharacterPanel
            key={index}
            name={character.name}
            imageURL={character.imageURL}
            show={show}
            isPressed={character.isPressed}
            togglePressed={() => togglePressed(index)}
            team={character.team}
            handleTeamChange={(event) =>
              handleTeamChange(index, event.target.value)
            }
          />
        ))}
      </div>

      <button style={playbutton} onClick={() => sendjson(characterStates)}>
        PLAY
      </button>
    </div>
  );
}

export default LandingPage;
