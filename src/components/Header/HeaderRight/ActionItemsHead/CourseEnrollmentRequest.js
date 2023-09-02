import React,{useState, CSSProperties} from 'react';
import OutsideAlerter from "../UserHead/OutsideAlerter";
import classes from './CourseEnrollmentRequest.module.css';
import {putcourseenroll} from '../../../../CommonApps/AllAPICalls';
import FadeLoader from "react-spinners/BeatLoader";
import OneRequest from "./OneRequest";

const override: CSSProperties = {
  display: "block",
  margin: "0 auto",
  borderColor: "red",
  fontSize:"10px",
};




const CourseEnrollmentRequest=(props)=>{






return (

<OutsideAlerter setDropDown={props.setDropDown}>

<div className={classes.courseEnrollmentRequest}>

        <div className={classes.allRequests}>  

      { props.userData.id !==null && props.userData.courseenrollment_requests.length===0 &&
      
        <div className={classes.oneRequest} style={{color:'grey'}}> There are no active action items </div>
      }



       { props.userData.id !==null && props.userData.courseenrollment_requests.map((request,index)=>{



	    return <OneRequest key={index} 
	                       request={request}
	                       rerender={props.rerender}
		               />   

         })

      }




        </div>   


</div>

</OutsideAlerter>




);

}

export default CourseEnrollmentRequest;
