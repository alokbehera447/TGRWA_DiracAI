import React from "react";
import classes from "./ProfileImageSec.module.css";
import ProfileImage from "./ProfileImage";
import ProfileImageInfo from "./ProfileImageInfo";



import {BsYoutube,BsLinkedin, BsTwitter} from 'react-icons/bs';
	




const ProfileImageSec = (props)=>{



return (

<div className={classes.profileImageSec}>



      <div className={classes.unitColumn}>
	
	<div className={classes.profileImageSec__pseudo}>


            <ProfileImage userData={props.userData} rerender={props.rerender}/>
	    
            <ProfileImageInfo userData={props.userData}/>
             
        </div>
        
     </div>


     {/*
     <div className={classes.unitColumn}>

       <div className={classes.innerColumn}>

         <div className={classes.ProfileInfo2_titleBar}> <i><h3>Links And Highlights</h3></i> </div>

 
            <div className={classes.yourlinks}>  
	        <BsYoutube className={classes.youtubeLink}/> 
	        <BsLinkedin className={classes.linkedInLink}/> 
	        <BsTwitter className={classes.twitterLink}/>  
	   </div> 



 

         </div>	

     </div>
     */}



</div>

);

}

export default ProfileImageSec;






