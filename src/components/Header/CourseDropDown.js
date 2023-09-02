import React,{useEffect} from 'react';
import classes from './CourseDropDown.module.css';
//import { FaGraduationCap,FaRegUser } from "react-icons/fa";
//import { FiSettings,FiHelpCircle,FiLogOut } from "react-icons/fi";
//import { useHistory } from 'react-router-dom';
//import OutsideAlerter from "./HeaderRight/UserHead/OutsideAlerter";


const UserHeadDropDown = (props) =>{

   //console.log("rerendering drop down");


    const courseSwitchHandler = (courseId)=>{
       localStorage.setItem('preferredCourseId', courseId);
       window.location.reload(false);
    }


   let selectedCourseId = localStorage.getItem('preferredCourseId');

   useEffect(()=>{


   },[selectedCourseId]);


  let buttonStyle2={backgroundColor:"#b8d1ff",
    color:"var(--themeColor)"};

  let buttonStyle1={backgroundColor:"#F0F0F0",
    color:"grey"};	


  //console.log("selectedCourseId", typeof selectedCourseId)



return (


    <div className={classes.DropDown} >

       <div className={classes.topGapBox}> Select a course </div>


       {
            props.dashboardCourses.map((course, index)=>{


                    return  <button className={classes.courseBox} 
		                    onClick={()=>courseSwitchHandler(course.id)} 
		                    key={index}
		                    style={Number(selectedCourseId) === course.id? buttonStyle2 : buttonStyle1}
			    > 
			           <b className={classes.courseNameBox}> {course.courseShortName}</b>
		                   <b className={classes.courseCodeBox}>{course.courseGlobalCode}</b>
			    </button>

            })
       }


       {
           props.dashboardCourses.length===0 && <div style={{color: 'grey'}}> No courses available!</div>

       }





    </div>	




);

}


export default UserHeadDropDown;

