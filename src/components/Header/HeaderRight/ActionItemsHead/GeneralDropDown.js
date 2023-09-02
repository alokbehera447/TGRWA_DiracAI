import React from 'react';
import classes from './GeneralDropDown.module.css';
//import { FaGraduationCap,FaRegUser } from "react-icons/fa";
//import { FiSettings,FiHelpCircle,FiLogOut } from "react-icons/fi";
//import { useHistory } from 'react-router-dom';
import OutsideAlerter from "../UserHead/OutsideAlerter";


const UserHeadDropDown = (props) =>{



    const ProfileHandler =()=>{
    }






return (

  <OutsideAlerter setDropDown={props.setDropDown}>

    <div className={classes.DropDown} >
       <div className={classes.courseSelectText} > <b> Select a Course</b></div>	
        <button className={classes.courseBox} onClick={ProfileHandler}> <b> Physics-I : 100006</b></button>
        <button className={classes.courseBox} onClick={ProfileHandler}> <b> Physics-I : 100006</b></button>
        <button className={classes.courseBox} onClick={ProfileHandler}> <b> Physics-I : 100006</b></button>
        <button className={classes.courseBox} onClick={ProfileHandler}> <b> Physics-I : 100006</b></button>

    </div>	

 </OutsideAlerter>


);

}


export default UserHeadDropDown;

