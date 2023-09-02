import React from 'react';
import classes from './TopInfoBarUserProfile.module.css';
//import TopInfoBarInstructor from '../Common/TopInfoBarInstructor';
import TopInfoBarButton from '../Common/TopInfoBarButton.js';
import TopInfoBarInstructor from '../../CommonAppUtilities/TopInfoBarInstructor';
import { useHistory } from 'react-router-dom';


const  TopInfoBarUserProfile =(props) =>  {

let history = useHistory();	







return (



<div className={classes.topInfoBar}>
       
	{ props.selectedCourse !==null && props.selectedCourse.length >0 &&
       <TopInfoBarInstructor selectedCourse={props.selectedCourse}/>
        }

       { props.selectedCourse ===null &&
        <div className={classes.topInfoBar__instructor}>
          <i className={classes.topInfoBar__time}>
               diracAI
          </i>
        </div>
        }

 



</div>



);




}


export default TopInfoBarUserProfile;
