import React, { useState,useEffect } from 'react';
import classes from './ContentDivUserProfile.module.css';
import ProfileImageSec from './ProfileImageSec/ProfileImageSec';
//import ProfileInformationAndSetting from './ProfileInformationAndSetting';
import {getuser} from '../../../CommonApps/AllAPICalls';

import ProfileUnitBlock from './ProfileUnitBlock';


const ContentDivUserProfile=(props)=>{




const [data, setData ] = useState({
	educationDegrees:[],
	achievements:[],


});

const [userData, userDataUpdated]=useState(false);



useEffect(() =>{

   getuser({setData});
   userDataUpdated(false);

  },[userData]);







return (

<div className={classes.contentDivUserProfile}>
  	
  <ProfileImageSec  userData={props.userData} rerender={props.rerender}/>
  
  <ProfileUnitBlock data={data}  userDataUpdated={userDataUpdated}/>
  
</div>

);

}


export default ContentDivUserProfile;
