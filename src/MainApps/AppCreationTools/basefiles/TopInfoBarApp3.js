import React from "react";
import classes from '../../CommonAppUtilities/TopInfoBar.module.css';
import TopInfoBarInstructor from '../../CommonAppUtilities/TopInfoBarInstructor';
import TopInfoBarButton from '../../CommonAppUtilities/TopInfoBarButton.js';
import { useNavigate } from 'react-router-dom';


const  TopInfoBarApp3 =(props) =>  {

   let history = useNavigate();

   const moveToApp1=()=>{
   history.push('/messages/app1');
   }

   const moveToApp2=()=>{
   history.push('/messages/app2');
   }










  return (

  <div className={classes.topInfoBar}>

       <TopInfoBarInstructor/>
      
       <TopInfoBarButton  onPress={moveToApp1}  buttonName={'App1'}/>

       <TopInfoBarButton  onPress={moveToApp2} buttonName={'App2'}/>

       <TopInfoBarButton styles={props.styles}  buttonName={'App3'}/>
	  




  </div>

);	
}

export default TopInfoBarApp3;
