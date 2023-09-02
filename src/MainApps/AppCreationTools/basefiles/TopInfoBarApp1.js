import React from "react";
import classes from '../../CommonAppUtilities/TopInfoBar.module.css';
import TopInfoBarInstructor from '../../CommonAppUtilities/TopInfoBarInstructor';
import TopInfoBarButton from '../../CommonAppUtilities/TopInfoBarButton.js';
import { useHistory } from 'react-router-dom';


const  TopInfoBarApp1 =(props) =>  {

   let history = useHistory();

   const moveToApp2=()=>{
   history.push('/messages/app2');
   }

   const moveToApp3=()=>{
   history.push('/messages/app3');
   }










  return (

  <div className={classes.topInfoBar}>

       <TopInfoBarInstructor/>
      
       <TopInfoBarButton  styles={props.styles}  buttonName={'App1'}/>

       <TopInfoBarButton  onPress={moveToApp2} buttonName={'App2'}/>

       <TopInfoBarButton onPress={moveToApp3}   buttonName={'App3'}/>
	  




  </div>

);	
}

export default TopInfoBarApp1;
