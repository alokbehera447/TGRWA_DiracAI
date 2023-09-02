import React,{useState} from 'react';
import classes from './UnitAboutIcon.module.css';

//import {MdContactMail} from 'react-icons/md';

import {BsTrophyFill} from 'react-icons/bs';

import CreateAchievementForm from './Forms/CreateAchievementForm';




const UnitAboutIcon=(props)=>{


const [showAddAchievementForm, setShowAddAchievementForm]= useState(false);




const showFormHandler=()=>{

setShowAddAchievementForm(true);
}


const closeFormHandler=()=>{
setShowAddAchievementForm(false);

}



return (

<div className={classes.unitAboutIcon}>

   <div> <BsTrophyFill className={classes.aboutIcon}/> <i>SKILLS AND ACHIEVEMENTS</i> </div>
  
  <button className={classes.editButtonAbout} onClick={showFormHandler}>+Add </button>

   { showAddAchievementForm && <CreateAchievementForm onPress={closeFormHandler} userData={props.userData}/>}


</div>
);


}
export default UnitAboutIcon;
