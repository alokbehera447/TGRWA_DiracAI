import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarSchool=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> Country: </div>

    <div className={classes.firstName}> {props.data.country}</div>



</div>
);


}
export default UnitBarSchool;
