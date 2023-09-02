import React from 'react';

import classes from './UnitBarFirstName.module.css';

const UnitBarFirstName=(props)=>{



return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> Role: </div>

    <div className={classes.firstName} style={{color:"green"}}> <b>
	{props.data.usertype ===1 && "Teacher"}
	{props.data.usertype ===2 && "Student"}
	{props.data.usertype ===3 && "Manager"}
	{props.data.usertype ===4 && "Employee"}


	</b></div>



</div>
);


}
export default UnitBarFirstName;
