import React from 'react';
import './Page.css'

import Team from '../components/Team';
import TransferButton from '../components/TransferButton';

const jsonpacket = {
  'players': ['cat', 'horse', 'cannon' ]
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

  const buttonplate = {
    gridRows: '2/3',
    backgroundColor: 'darkgrey',
    borderTop: 'outset 5px orangered'
  }

  return (
    <div id='page' style={landingpage}>

    <Team></Team>

      <div style={buttonplate}>
        <TransferButton />
      </div>
      

    </div>
  );
}

export default HomePage;
