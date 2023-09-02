import React from 'react';
import classes from './UnitBarInstDegree.module.css';





const UnitBarInstDegree = (props)=>{



return (

<div className={classes.unitBarInstDegree}>


   <div className={classes.InstLogo}> 
    <img src={props.logo}  className={classes.logoImage} />

   </div>

   <div className={classes.InstInfo}> 

      <div className={classes.InstInfo__degree}>
	<b>{props.degree}</b>
      </div>

      <div className={classes.InstInfo__instName}>
	{props.institute}
      </div>

      <div className={classes.InstInfo__duration}>
	{props.duration}
      </div>


      <div className={classes.InstInfo__location}>
	{props.place}
      </div>



   </div>



</div>
);


}
export default UnitBarInstDegree;
