import React from 'react';
import classes from './SideNavBarButtonQMeeting.module.css';





const SideNavBarButton = (props) =>{

   const TheIcon = props.icon;








   return(

       <div className={classes.mainButtonContainer}>


        <button onClick={props.onPress} className={classes.sideNavBarButton} style={props.buttonColor}> 
	   {/*TheIcon !==null &&  <TheIcon className={classes.dashIcon} style={{color:props.buttonColor.color}}/>*/} 
	   <span className={classes.buttonText} style={{color:props.buttonColor.color}}> 
	         <b>{props.name}</b>
	   </span>  
        </button>

     </div>

   );


}

export default SideNavBarButton;
