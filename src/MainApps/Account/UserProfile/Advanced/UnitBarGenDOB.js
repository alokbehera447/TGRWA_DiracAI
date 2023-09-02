import React from 'react';

import classes from './UnitBarGenDOB.module.css';

const UnitBarGenDOB=(props)=>{



return (

	
	
<div className={classes.unitBarGenDOB}>

    
    <div className={classes.genderDiv}> <b>GENDER:</b> <i> {props.data.gender}   </i> </div>

    <div className={classes.dobDiv}> <b>DOB: </b> <i> {props.data.dateofbirth} </i></div>
   


</div>
);


}
export default UnitBarGenDOB;
