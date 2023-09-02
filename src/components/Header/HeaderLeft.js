import React,{useState} from 'react'; 
import classes from './HeaderLeft.module.css';
import {BsList} from 'react-icons/bs';
import CourseDropDown from './CourseDropDown';
import { useHistory } from "react-router-dom";

import {IoMdArrowRoundBack } from 'react-icons/io';


import {SiRedux} from 'react-icons/si';



function HeaderLeft(props){

    let history = useHistory();
    const [courseDropDown, setCourseDropDown]=useState(false);


    const showCourses=()=>{
       setCourseDropDown(true);
    }


    const hideCourses=()=>{
      setCourseDropDown(false);
    }


   const dashClickHandler=()=>{
   
   history.push("../../dashboard/general/courses");	   

   }


   const backToDashboard=()=>{
     localStorage.removeItem('preferredCourseId');
     history.push('../../dashboard/general/courses');



   }	







return (

 <div className={classes.headerLeft} > 


      { localStorage.getItem('preferredCourseId') !=null && 
      <button type="button" className={classes.backButton} onClick={backToDashboard}> <IoMdArrowRoundBack className={classes.BackIcon}/> </button>
      }



       <div className={classes.logoText}>
	  <b>Di</b> 
	  <div className={classes.styleBar}> </div>
       </div>
       

      <button className={classes.ExpConButton} onClick={props.onPress}> 
	  <BsList className={classes.ExpConIcon} />
      </button>	

     <div >
        Admin console
     </div>

  </div>

);


}

export default HeaderLeft;

