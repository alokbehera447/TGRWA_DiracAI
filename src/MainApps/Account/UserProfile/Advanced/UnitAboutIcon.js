import React,{useState} from 'react';
import classes from './UnitAboutIcon.module.css';
import {FaUserCircle} from 'react-icons/fa';
import AboutEditForm from './AboutEditForm';


const UnitAboutIcon=(props)=>{


const [editForm,showEditForm]=useState(false);




const aboutEditFormHandler =()=>{


showEditForm(true);

}

const closeAboutFormHandler=()=>{

showEditForm(false);

}



return (

<div className={classes.unitAboutIcon}>


	{ editForm && <AboutEditForm onPress={closeAboutFormHandler} userDataUpdated={props.userDataUpdated}/>}


   <div> <FaUserCircle className={classes.aboutIcon}/> <i>ABOUT</i> </div>
  
   <button onClick={aboutEditFormHandler} className={classes.editButtonAbout}>edit </button>
</div>
);


}
export default UnitAboutIcon;
