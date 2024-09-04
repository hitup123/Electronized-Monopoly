import React from 'react';
import './Page.css'
import { useContext } from 'react';
import { useEffect, useState } from 'react';

// import car from '../Images/car.png';
// import horse from '../Images/horse.png';
// import cannon from '../Images/cannon.png';
// import hat from '../Images/hat.png';
// import dog from '../Images/dog.png';
// import wheelbarrow from '../Images/wheelbarrow.png';
// import dustbin from '../Images/dustbin.png';
// import ship from '../Images/ship.png';
// import shoe from '../Images/shoe.png';
// import iron from '../Images/iron.png';
import { DataContext } from '../App';
import { LogContext } from '../App';
import Team from '../components/Team';
import TransferButton from '../components/TransferButton';
import EventPanel from '../components/EventPanel';
import { useState } from 'react';
import { useEffect } from 'react';
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



function TeamObjects({data})
{
  const teamsplatter = {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    gap: '20px',
    padding: '20px'
  }

  // const teams = [
  //   {
  //     player: [
  //       {
  //         ico: hat
  //       },
  //       {
  //         ico: dog
  //       }
  //     ],
  //     stat: 'playing',
  //     balance: '3925',
  //     property: [
  //       {
  //         pro: 'Pall Mall'
  //       },
  //       {
  //         pro: 'Whitehall'
  //       },
  //       {
  //         pro: 'Mayfair'
  //       },
  //       {
  //         pro: 'Vine Street'
  //       }
  //     ] ,
  //   },
  //   {
  //     player: [
  //       {
  //         ico: horse
  //       },
  //       {
  //         ico: iron
  //       }
  //     ],
  //     stat: 'jail',
  //     balance: '8543',
  //     property: [
  //       {
  //         pro: 'Bow Street'
  //       },
  //       {
  //         pro: 'Euston Road'
  //       },
  //       {
  //         pro: 'Regent Street'
  //       }
  //     ]
  //   }
  // ];
  console.log("data ",data)
  // const teams = data ? Object.keys(data).filter(key => key.startsWith('team')).map(key => ({
  //   player: data[key][0].map(item => ({ ico: require(`../Images/${item}.png`) })),
  //   stat: data[key][2],
  //   balance: data[key][1],
  //   property: [] // You can populate property if needed
  // })) : [];

  const teams = data 
  ? Object.keys(data).filter(key => key.startsWith('team')).map(key => {
      const players = Array.isArray(data[key][0]) && data[key][0].length > 0
        ? data[key][0].map(item => ({ ico: require(`../Images/${item}.png`) }))
        : [];  // Fallback to an empty array if data[key][0] is not an array

      return {
        player: players,
        stat: data[key][2],
        balance: data[key][1],
        property: [] // You can populate property if needed
      };
    })
  : [];


  console.log("teams",teams)
  const teamobj = teams
  .filter(element => element.player.length > 0)  // Filter out teams with empty players
  .map((element, index) => (
    <Team 
      key={index} 
      balance={element.balance} 
      status={element.stat} 
      icons={element.player} 
      property={element.property} 
    />
  ));


  return <div style={teamsplatter}>{teamobj}</div>
}

const LogScreen = ({ newLog }) => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    if (newLog) {
      setLogs(prevLogs => [...prevLogs, newLog]);
    }
  }, [newLog]);

  return (
    <div style={{ backgroundColor: '#f8f8f8', padding: '10px', borderRadius: '5px', overflow: 'scroll' }}>
      {logs.map((log, index) => (
        <p key={index}>
          <span className="material-symbols-outlined">arrow_right</span>
          {log}
        </p>
      ))}
    </div>
  );
};

function HomePage() {
  const contextData = useContext(DataContext);
  const contextLog = useContext(LogContext);
  const json_packet = contextData;
  const log_json = contextLog;//NEW LOG
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

      <TeamObjects data={json_packet}></TeamObjects>
      <EventPanel />

    

    <div style={userinterface}>

      <div style={buttonplate}>
        <TransferButton />      </div>

      {/* <div style={logscreen}>
        <p><span class="material-symbols-outlined">arrow_right</span>Property Sold to Player 1</p>
        <p><span class="material-symbols-outlined">arrow_right</span>Player 3 is Bankrupt</p>
        <p><span class="material-symbols-outlined">arrow_right</span>Player 2 builds house on Pall Mall</p>
        <p><span class="material-symbols-outlined">arrow_right</span>Player 5 pays rent to Player 2</p>
      </div> */}

      <LogScreen newLog={log_json}/>
    </div>
      
      

    </div>
  );
}

export default HomePage;
