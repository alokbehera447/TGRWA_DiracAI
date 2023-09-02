import React from 'react';

import {w3cwebsocket as W3CWebSocket } from 'websocket';




const CentralSocketConnection = () =>{

  let  client = new W3CWebSocket('wss://td7ru13iq4.execute-api.ca-central-1.amazonaws.com/production');

  client.onopen=()=>{
     console.log("Websocket gets connected");

   }
  


return (client)


}

export default CentralSocketConnection;

