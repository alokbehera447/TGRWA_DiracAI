import React,{useState} from 'react';
import classes from './UnitAboutIcon.module.css';
import {FaGraduationCap} from 'react-icons/fa';

import EduDegreeForm from './Forms/EduDegreeForm'


const UnitAboutIcon=()=>{


const [showAddForm, setShowAddForm] = useState(false);




  const showFormHandler=()=>{
     setShowAddForm(true);
  }

  const closeFormHandler=()=>{
     setShowAddForm(false);
  }







return (

<div className={classes.unitAboutIcon}>

   <div> <FaGraduationCap className={classes.aboutIcon}/> <i>EDUCATION</i> </div>  
   <button className={classes.editButtonAbout} onClick={showFormHandler}> +Add </button>

   { 

	showAddForm && <EduDegreeForm onPress={closeFormHandler}/>

   }





</div>
);


}
export default UnitAboutIcon;
