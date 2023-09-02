import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarEMail=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> <b>Email:</b> </div>

    <div className={classes.firstName}> {props.data.username}</div>



</div>
);


}
export default UnitBarEMail;
