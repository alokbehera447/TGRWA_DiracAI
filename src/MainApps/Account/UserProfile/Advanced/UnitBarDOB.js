import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarUsername=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> <b>Date of birth :</b> </div>

    <div className={classes.firstName}> {props.data.dateofbirth}</div>



</div>
);


}
export default UnitBarUsername;
