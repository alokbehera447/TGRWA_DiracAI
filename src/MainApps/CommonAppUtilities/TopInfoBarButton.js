import React from "react";
import classes from './TopInfoBarButton.module.css';





const TopInfoBarButton = (props)=>  {




return (

<div onClick={props.onPress}  style={props.styles}  className={classes.topInfoBar__profilebtn}> {props.buttonName}  </div>


);

}



export default TopInfoBarButton;

