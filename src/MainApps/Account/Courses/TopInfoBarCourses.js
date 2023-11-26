import React from 'react';
import classes from '../Common/TopInfoBar.module.css';
import TopInfoBarInstructor from '../Common/TopInfoBarInstructor';
import TopInfoBarButton from '../Common/TopInfoBarButton.js';
import { useNavigate } from 'react-router-dom';

const  TopInfoBarCourses =(props) =>  {

let history = useNavigate();	


const moveToProfile=()=>{

  history.push('/account/userprofile');

}

const moveToSettings=()=>{

  history.push('/account/settings');

}





return (



<div className={classes.topInfoBar}>

       <TopInfoBarInstructor/>

       <TopInfoBarButton onPress={moveToProfile}  buttonName={'Profile'}/>

       <TopInfoBarButton  onPress={moveToSettings} buttonName={'Settings'}/>

       <TopInfoBarButton  styles={props.styles}    buttonName={'Courses'}/>




</div>



);




}


export default TopInfoBarCourses;
