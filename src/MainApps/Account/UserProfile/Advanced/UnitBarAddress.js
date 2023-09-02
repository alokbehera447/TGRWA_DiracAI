import React from 'react';
import classes from './UnitBarInstDegree.module.css';
import {BsTrash} from 'react-icons/bs'






const UnitBarInstDegree = (props)=>{



return (

<div className={classes.unitBarInstDegree}>


  <div className={classes.addMainContainer}>

   <div className={classes.addressType}> <h3>{props.address.addressType} </h3>  </div>	


   <div className={classes.InstLogo}> 
   {/*    <img src={address1}  className={classes.logoImage} alt="logo2"/>*/}

   </div>

   <div className={classes.InstInfo}> 

      <div className={classes.InstInfo__degree}>
	<b> {props.address.houseno+", "+props.address.streetno}</b>
      </div>

      


    <div className={classes.InstInfo__degree}>
        <b> {props.address.district} {props.address.pincode}</b>
    </div>
	

     <div className={classes.InstInfo__degree}>
        <b> {props.address.state+", "+props.address.country}</b> 
      </div>



       <div className={classes.InstInfo__location}>
        Address Proof Doc: Uploaded 
      </div>

   </div>

 </div>


   <button className={classes.deleteDegree}> 

     <BsTrash/>
  </button>	


</div>
);


}
export default UnitBarInstDegree;
