import React from 'react';

import classes from './UnitBar.module.css';

const UnitBar=(props)=>{



return (

<div className={classes.unitBar}>


 {props.title}	

</div>
);


}
export default UnitBar;
