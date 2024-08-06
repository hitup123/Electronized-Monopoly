import React from 'react';
import './Page.css'

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


import Team from '../components/Team';
import TransferButton from '../components/TransferButton';

const jsonpacket = {
  'team1': [['cannon', 'car', 'shoe'],1500,'playing'],
  'team2': [['dustbin', 'iron'], 1234, 'jail'],
  'team3': [['ship', 'horse'], 789, 'bankrupt'],
  'team4':[],
  'team5':[],
  'team6':[],
  'team7':[],
  'log': 'I am Bankrupt',
}



function TeamObjects()
{
  const teamsplatter = {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    gap: '20px',
    padding: '20px'
  }

  const teams = [
    {
      player: [
        {
          ico: hat
        },
        {
          ico: dog
        }
      ],
      stat: 'playing',
      balance: '3925',
      property: [
        {
          pro: 'Pall Mall'
        },
        {
          pro: 'Whitehall'
        },
        {
          pro: 'Mayfair'
        },
        {
          pro: 'Vine Street'
        }
      ] ,
    },
    {
      player: [
        {
          ico: horse
        },
        {
          ico: iron
        }
      ],
      stat: 'jail',
      balance: '8543',
      property: [
        {
          pro: 'Bow Street'
        },
        {
          pro: 'Euston Road'
        },
        {
          pro: 'Regent Street'
        }
      ]
    }
  ];

  const teamobj = teams.map((element) => {
    return (
      <Team balance={element.balance} status={element.stat} icons={element.player} property={element.property }></Team>
    )
  });

  return <div style={teamsplatter}>{teamobj}</div>
}

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

  const userinterface = {
    gridRows: '2/3',
    display: 'grid',
    gridTemplateColumns: '60% 40%',
    borderTop: 'outset 10px orangered',
  }
  const buttonplate = {
    backgroundColor: 'darkgrey', 
    gridColumns: '1/2',
    padding: '10px',
  }

  const logscreen = {
    gridColumns: '2/3',
    backgroundColor: 'blue',
    borderTop: 'inset 5px orangered', 
    borderLeft: 'ridge 20px grey', 
    padding: '10px',
    color: 'white',
  }


  return (
    <div id='page' style={landingpage}>

      <TeamObjects></TeamObjects>

    

    <div style={userinterface}>

      <div style={buttonplate}>
        <TransferButton />      </div>

      <div style={logscreen}>
        <p><span class="material-symbols-outlined">arrow_right</span>Property Sold to Player 1</p>
        <p><span class="material-symbols-outlined">arrow_right</span>Player 3 is Bankrupt</p>
        <p><span class="material-symbols-outlined">arrow_right</span>Player 2 builds house on Pall Mall</p>
        <p><span class="material-symbols-outlined">arrow_right</span>Player 5 pays rent to Player 2</p>
      </div>
    </div>
      
      

    </div>
  );
}

export default HomePage;
