import React from 'react';
import classes from './UserHeadDropDown.module.css';
import { FaRegUser } from "react-icons/fa";
import { FiSettings,FiHelpCircle,FiLogOut } from "react-icons/fi";
import { useHistory } from 'react-router-dom';
import OutsideAlerter from "./OutsideAlerter";
import {Logout} from '../../../../CommonApps/Logout';


const UserHeadDropDown = (props) =>{


 let history = useHistory();






 const logoutHandler =()=>{


   Logout();

 }


  const ProfileHandler =()=>{
    props.clickItem();
    history.push('/app/account/userprofile');
  }


  const settingsHandler =()=>{
    props.clickItem();
    history.push('/app/account/settings');
  }


 const coursesHandler =()=>{
   props.clickItem();
   history.push('/account/courses');	
 }

 const helpCentreHandler =()=>{
   props.clickItem();
 }




return (

<OutsideAlerter setDropDown={props.setDropDown}>

<div className={classes.DropDown} >
  <i className={classes.profile} onClick={ProfileHandler} > <FaRegUser className={classes.icons}/>Profile</i>
	{/*
  <i onClick={settingsHandler}> <FiSettings className={classes.icons}/>Settings </i>
  	
  <i onClick={coursesHandler}> <FaGraduationCap className={classes.icons}/>Courses</i>
  
  <i onClick={helpCentreHandler}> <FiHelpCircle className={classes.icons}  />Help Center</i>
  */}
  <i className={classes.logout}  onClick={logoutHandler}><FiLogOut className={classes.icons}  />Logout</i>

</div>	


</OutsideAlerter>


);

}


export default UserHeadDropDown;

