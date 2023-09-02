import React from 'react';
import classes from './UserProfileContentBasic.module.css';
import AboutBasic from './AboutBasic';



const UserProfileContentBasic =(props)=>{



return (

<div className={classes.userProfileContentBasic}>
	

<AboutBasic data={props.data} userDataUpdated={props.userDataUpdated}/>





</div>
);	

}


export default UserProfileContentBasic;
