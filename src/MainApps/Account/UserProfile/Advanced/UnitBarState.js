import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarState=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> State: </div>

    <div className={classes.firstName}> {props.data.state} </div>



</div>
);


}
export default UnitBarState;
