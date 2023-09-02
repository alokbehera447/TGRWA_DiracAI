import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarGender=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> <b>Gender:</b> </div>

    <div className={classes.firstName}> {props.data.gender}</div>



</div>
);


}
export default UnitBarGender;
