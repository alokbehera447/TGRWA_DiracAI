import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarTitle=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> Title: </div>

    <div className={classes.firstName}> {props.data.usertitle}</div>



</div>
);


}
export default UnitBarTitle;
