import React from 'react';
import classes from './SideNavBarButton.module.css';





const SideNavBarButton = (props) =>{

   const TheIcon = props.icon;





   return(

      <button onClick={props.onPress} className={classes.sideNavBarButton} style={props.buttonColor}> 
	   <TheIcon className={classes.dashIcon}/> 
	   <span className={classes.buttonText}>{props.name}</span> 
      </button>




   );


}

export default SideNavBarButton;
