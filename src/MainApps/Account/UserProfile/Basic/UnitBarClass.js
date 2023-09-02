import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarClass=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> Class: </div>

    <div className={classes.firstName}> {props.data.position}</div>



</div>
);


}
export default UnitBarClass;
