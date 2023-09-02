import React from "react";

import classes from './TopTitleBar.module.css';




const TopTitleBar=(props)=>{


return (

<div className={classes.topTitleBar}>

<i className={classes.topTitleBar__Text}><b>{props.title} </b></i>

</div>

);

}


export default TopTitleBar;
