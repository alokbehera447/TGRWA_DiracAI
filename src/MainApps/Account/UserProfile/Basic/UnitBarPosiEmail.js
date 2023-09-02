import React from 'react';

import classes from './UnitBarGenDOB.module.css';

const UnitBarGenDOB=(props)=>{



return (

<div className={classes.unitBarGenDOB}>


    <div className={classes.genderDiv}> <b>Current Position:</b> <i> {props.data.position} </i> </div>

    <div className={classes.dobDiv}> <b>Email: </b> <i> {props.data.email} </i></div>



</div>
);


}
export default UnitBarGenDOB;
