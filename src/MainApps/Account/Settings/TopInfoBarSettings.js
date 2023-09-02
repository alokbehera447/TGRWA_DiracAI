import React from 'react';
import classes from '../Common/TopInfoBar.module.css';
import TopInfoBarInstructor from '../Common/TopInfoBarInstructor';
import TopInfoBarButton from '../Common/TopInfoBarButton.js';
import { useHistory } from 'react-router-dom';

const  TopInfoBarSettings =(props) =>  {

let history = useHistory();	


const moveToProfile=()=>{

  history.push('/account/userprofile');

}

const moveToCourses=()=>{

  history.push('/account/courses');

}





return (



<div className={classes.topInfoBar}>
       {/*
       <TopInfoBarInstructor/>

       <TopInfoBarButton onPress={moveToProfile}  buttonName={'Profile'}/>

       <TopInfoBarButton  styles={props.styles} buttonName={'Settings'}/>
       */}




</div>



);




}


export default TopInfoBarSettings;
