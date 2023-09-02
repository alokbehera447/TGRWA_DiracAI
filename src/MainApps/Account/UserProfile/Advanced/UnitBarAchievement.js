import React from 'react';
import classes from './UnitBarInstDegree.module.css';
import {BsTrash} from 'react-icons/bs'

import {deleteedudegree} from '../../../../CommonApps/AllAPICalls';




const UnitBarInstDegree = (props)=>{




const deleteEduDegreeHandler=()=>{

//let edudegreeid = props.achievementId;


//deleteedudegree({edudegreeid});

//window.location.reload(false);	

}




return (

<div className={classes.unitBarInstDegree}>


    
   <div className={classes.degreeInfoall}>

      <div className={classes.InstLogo}> 
         <img src={props.logo}  className={classes.logoImage} alt="logo1"/>
      </div>

     <div className={classes.InstInfo}> 

      <div className={classes.InstInfo__degree}>
	<b>{props.achievementname}</b>
      </div>


      <div className={classes.InstInfo__duration}>
	{props.duration}
      </div>




       <div className={classes.InstInfo__location}>
        Transcripts: 
      </div>

       <div className={classes.InstInfo__location}>
        Certificates:
      </div>

    </div>

  </div>



   <button className={classes.deleteDegree} onClick={deleteEduDegreeHandler}>
      <BsTrash/>

   </button>

</div>
);


}
export default UnitBarInstDegree;
