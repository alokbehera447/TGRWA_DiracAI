import React from "react";
import classes from "./ProfileUnitBlock.module.css";
//import ProfileImage from "./ProfileImage";
//import ProfileImageInfo from "./ProfileImageInfo";

import ProfileInformationAndSetting from './ProfileInformationAndSetting';


const ProfileUnitBlock = (props)=>{



return (

<div className={classes.profileImageSec}>

        
	<ProfileInformationAndSetting data={props.data}  userDataUpdated={props.userDataUpdated}/>
	  {/*
	    <div className={classes.profileImageSec__pseudo}>
               <ProfileImage data={props.data} />
               <ProfileImageInfo data={props.data}/>
            </div>
	 */}
</div>

);

}

export default ProfileUnitBlock;






