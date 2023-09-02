import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarFirstName=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> <b>Last Name:</b> </div>

    <div className={classes.firstName}> {props.data.lastname}</div>



</div>
);


}
export default UnitBarFirstName;
