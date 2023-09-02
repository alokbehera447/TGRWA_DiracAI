import React from 'react';

import classes from './UserProfileSwitchBarButton.module.css';

const UserProfileSwitchBarButton =(props)=>{


return (


<div className={classes.userProfileSwitchBarButton} style={props.style} onClick={props.onPress}>

	{props.title}	
 
</div>


);

}

export default UserProfileSwitchBarButton;


