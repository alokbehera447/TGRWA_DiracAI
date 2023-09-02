import React,{useState,useEffect} from "react";
import classes from './TopInfoBarInstructor.module.css';
import {getuserbyId} from '../../CommonApps/AllAPICalls';


const TopInfoBarInstructor = ( props) => {

//const [userData, setUserData]=useState({
//	usertitle: "",
//	firstname:" N/A ",
//	lastname:""
//
//});


//  useEffect(()=>{
//    if(props.selectedCourse.length>0){	
//       let userId=props.selectedCourse[0].teacher;
//       getuserbyId({userId, setUserData});
//    }
//
//  },[props.selectedCourse]);


 // console.log("course: ", props.selectedCourse[0]);




return (


  <div className={classes.topInfoBar__instructor}> 
	
	<i className={classes.topInfoBar__instructorName}>
        
	  Instructor:  { props.selectedCourse !==null ?
			  props.selectedCourse[0].teacher.firstname+" "+props.selectedCourse[0].teacher.lastname : "N/A"
		       } 
	
	</i>
	
  </div>


);	



}


export default TopInfoBarInstructor;

