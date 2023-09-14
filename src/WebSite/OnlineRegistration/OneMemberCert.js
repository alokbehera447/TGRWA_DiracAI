import React,{useState, useEffect, CSSProperties} from "react";
//import classes from './OnlineRegistrationHome.module.css';

import classes from './OneMemberCert.module.css';

import Logo from './LogoTGRWA.png';


const OneMemberCert=(props)=>{



console.log("one member: ", props.oneMember);


return  <div className={classes.FormMainDiv}>


      <div className={classes.FormMainDiv_inner}>

           <div className={classes.titleBlock}>
                
                <div className={classes.logo}>  
		  <img src={Logo} className={classes.imageLogo}/> 
		</div>

		<div className={classes.InstTitle}>
		     <div className={classes.mainTitle}><b> {"Trident Galaxy Residents' Welfare Association"}</b> </div>
		     <div className={classes.tagTitle}> Regd. No. : 2586-62/2019-2020 </div>
		</div>
           </div>

           <div className={classes.descriptionRole}> Membership declaration </div>		

	   <div className={classes.textContent}> 
		I wish to be a member of the Trident Galaxy Residents' Welfare Association. Please enroll me as a member of Trident Galaxy Residents' Welfare Association with Regd. no. 2586-62/2019-2020. I am willing to contribute Rs. 500/- as one-time membership fee. I promise to abide by the laws of association 
	   </div>	

   		
           <div className={classes.OneInfoBlock}  >

               <img src={props.oneMember.photoFile} className={classes.imageDiv}/>            
               <div className={classes.InfoDiv}>
		    <div className={classes.info_subdiv}> <i>Name: </i> {props.oneMember.name} </div>
		    <div className={classes.info_subdiv}> <i>Email: </i> ***</div>
		    <div className={classes.info_subdiv}> <i>Phone:</i> ***</div>
		    <div className={classes.info_subdiv}> <i>Address:</i> {props.oneMember.address} </div>
		    <div className={classes.info_subdiv}> Trident Galaxy Apartments </div>
		    <div className={classes.info_subdiv}> K-3, Kalinga Nagar </div>
		    <div className={classes.info_subdiv}> Ghatikia, Bhubaneswar </div>
		    <div className={classes.info_subdiv}> Odisha-751003 </div>
	       </div>

           </div>


           <div className={classes.OneInfoBlock} >

             <div className={classes.sigDiv}>Member Signature:</div> 
	     <img src={props.oneMember.signatureFile} className={classes.signatureImage}/> 

           </div>

    </div>		

    </div>











}


export default OneMemberCert;


