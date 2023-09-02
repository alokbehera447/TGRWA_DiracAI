import React,{useState, useEffect, CSSProperties} from "react";
import classes from './OnlineRegistrationHome.module.css';
import Logo from './LogoTGRWA.png';
import {getallregistrants} from '../../CommonApps/AllAPICalls';

import OneMemberCert from "./OneMemberCert";


const ViewAllRegistrants=()=>{


  const [registrants, getRegistrants] = useState(null);



  useEffect(()=>{


   getallregistrants({getRegistrants});



  },[]);


  console.log("registrants: ", registrants); 


   return <>

          <div className={classes.viewMemberPageHeader}> <h3>Members of Trident Galaxy Residents' Association</h3>  </div>

	<div className={classes.ViewAllMembersParent} >

       { registrants !==null && registrants.map((oneMember, index)=>{

        return  <OneMemberCert key={index} oneMember={oneMember}/>

       })    

      }


     </div>
    </>

}


export default ViewAllRegistrants;
