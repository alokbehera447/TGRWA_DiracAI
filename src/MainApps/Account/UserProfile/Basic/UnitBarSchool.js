import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarSchool=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> School/College: </div>

    <div className={classes.firstName}> {props.data.institute}</div>



</div>
);


}
export default UnitBarSchool;
