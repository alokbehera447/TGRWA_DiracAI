import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarCity=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> City: </div>

    <div className={classes.firstName}> {props.data.city}</div>



</div>
);


}
export default UnitBarCity;
