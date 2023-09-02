import React from 'react';
import classes from './SideNavBarButtonDashboard.module.css';

//import {Typography,Button} from '@material-ui/core';



const SideNavBarButton = (props) =>{

   const TheIcon = props.icon;






   return(

       <div className={classes.mainButtonContainer}>

       
        <button onClick={props.onPress} className={classes.sideNavBarButton} style={props.buttonColor}> 
	   {TheIcon !==null &&  <TheIcon className={classes.dashIcon} style={{color:props.buttonColor.color}}/>} 
	   <span className={classes.buttonText} style={{color:props.buttonColor.color,marginLeft:'calc( 0.13 * var(--headerHeight) )'}}> 	      
	      {props.name}	      
	   </span>  
        </button>


     </div>

   );


}

export default SideNavBarButton;
