import React from "react";
import classes from '../../CommonAppUtilities/TopInfoBar.module.css';
import TopInfoBarInstructor from '../../CommonAppUtilities/TopInfoBarInstructor';
import TopInfoBarButton from '../../CommonAppUtilities/TopInfoBarButton.js';
import { useHistory } from 'react-router-dom';


const  TopInfoBarApp2 =(props) =>  {

   let history = useHistory();

   const moveToApp1=()=>{
   history.push('/messages/app1');
   }

   const moveToApp3=()=>{
   history.push('/messages/app3');
   }










  return (

  <div className={classes.topInfoBar}>

       <TopInfoBarInstructor/>
      
       <TopInfoBarButton  onPress={moveToApp1}  buttonName={'App1'}/>

       <TopInfoBarButton  styles={props.styles} buttonName={'App2'}/>

       <TopInfoBarButton onPress={moveToApp3}   buttonName={'App3'}/>
	  




  </div>

);	
}

export default TopInfoBarApp2;
