import React from 'react';


import classes from './UserProfileContentFriends.module.css';

import UnitBar from '../Basic/UnitBar'
import UnitFriendsIcon from './UnitFriendsIcon';

import AllFriends from './AllFriends';



const UserProfileContentFriends =(props)=>{



  console.log("userData: ", props.userData);

return (

<div className={classes.userProfileContentGrades}>

    	
    <UnitFriendsIcon userData={props.userData}/>

    <AllFriends userData={props.userData}/>
    

</div>
);	

}


export default UserProfileContentFriends;
