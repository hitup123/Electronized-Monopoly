import React, { useState, useEffect, useContext } from 'react';
import './Page.css';
import Team from '../components/Team';
import TransferButton from '../components/TransferButton';
import EventPanel from '../components/EventPanel';
import GoToJail from '../components/Jail';
import GetTax from '../components/Tax';
import { DataContext, LogContext } from '../App';

const TeamObjects = ({ data }) => {
  const teamsplatter = {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    gap: '20px',
    padding: '20px'
  };
  // console.log("data:",data);
  const teams = data 
  ? Object.keys(data).filter(key => key.startsWith('team')).map(key => {
      const players = Array.isArray(data[key][0]) && data[key][0].length > 0
        ? data[key][0].map(item => ({ ico: require(`../Images/${item}.png`) }))
        : [];  // Fallback to an empty array if data[key][0] is not an array

      return {
        player: players,
        stat: data[key][2],
        balance: data[key][1],
        property: data[key][4] // You can populate property if needed
      };
    })
  : [];
    // console.log("teams",teams)
  const teamobj = teams
  .filter(element => element.player.length > 0)  // Filter out teams with empty players
  .map((element, index) => (
    <Team 
      key={index} 
      balance={element.balance} 
      status={element.stat} 
      icons={element.player}
      property={element.property.split("_").map(pro => ({ pro }))} 
      // property={[
      //   {
      //       pro : 'Vine Street'
      //   },
      //   {
      //       pro : 'Strand'
      //   },
      //   {
      //     pro: 'Whitehall'
      //   }
    // ]/*element.property*/} 
    />
  ));

  return <div style={teamsplatter}>{teamobj}</div>;
};

const EventPop = ({ newLog }) => {
  const [Pops, setPops] = useState([]); // State to manage logs/events

  useEffect(() => {
    if (newLog) {
      const id = Date.now(); // Unique ID for each log
      setPops(prevPops => [...prevPops, { ...newLog, id }]);

      // Set a timeout to remove the log after 2 seconds
      const timer = setTimeout(() => {
        setPops(prevPops => prevPops.filter(pop => pop.id !== id));
      }, 5000);

      // Cleanup the timeout
      return () => clearTimeout(timer);
    }
  }, [newLog]);

  return (
    <>
      {Pops.map(log => (
        <EventPanel key={log.id} eventType={log.action} msg={log.msg} teamname={log.team1} money={log.money} />
      ))}
    </>
  );
};

const LogScreen = ({ newLog }) => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    if (newLog) {
      // console.log("LOG");
      // console.log(newLog.msg);
      setLogs(prevLogs => [...prevLogs, newLog]);
    }
  }, [newLog]);

  const logscreen = {
    gridColumns: '2/3',
    backgroundColor: 'blue',
    borderTop: 'inset 5px orangered', 
    borderLeft: 'ridge 20px grey', 
    padding: '10px',
    color: 'white',
    overflow: 'scroll'
  };

  return (
    <div style={logscreen}>
      {logs.map((log, index) => (
        <p key={index}>
          <span className="material-symbols-outlined">arrow_right</span>
          {log.msg}
        </p>
      ))}
    </div>
  );
};

function HomePage() {
  const contextData = useContext(DataContext);
  const contextLog = useContext(LogContext);
  const json_packet = contextData;
  const log_json = contextLog; // Using newLog for consistency

  const landingpage = {
    display: 'grid',
    gridTemplateRows: '70% 30%',
    overflow: 'hidden'
  };

  const playercardpanel = {
    gridRows: '1/2',
    backgroundColor: 'grey',
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center'
  };

  const userinterface = {
    gridRows: '2/3',
    display: 'grid',
    gridTemplateColumns: '60% 40%',
    borderTop: 'outset 10px orangered',
  };

  const buttonplate = {
    backgroundColor: 'darkgrey', 
    gridColumns: '1/2',
    padding: '10px',
  };

  return (
    <div id='page' style={landingpage}>
      <TeamObjects data={json_packet} />
      <EventPop newLog={log_json} /> 
      <div style={userinterface}>
        <div style={buttonplate}>
          <TransferButton />
          <GoToJail />
          <GetTax />
        </div>
        <LogScreen newLog={log_json} />
      </div>
    </div>
  );
}

export default HomePage;
