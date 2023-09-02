import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarFirstName=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> First Name: </div>

    <div className={classes.firstName}> {props.data.firstname}</div>



</div>
);


}
export default UnitBarFirstName;
