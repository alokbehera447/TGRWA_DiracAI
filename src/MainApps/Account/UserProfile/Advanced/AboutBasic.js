import React from "react";
import classes from './AboutBasic.module.css';


import UnitBar from './UnitBar';
import UnitBarFirstName from './UnitBarFirstName';
import UnitBarLastName from './UnitBarLastName';
import UnitBarRole from './UnitBarRole';
import UnitBarEMail from './UnitBarEMail';
import UnitBarUsername from './UnitBarUsername';

import UnitBarTitle from './UnitBarTitle';

import UnitBarClass from './UnitBarClass';
import UnitBarSchool from './UnitBarSchool';
import UnitBarCity from './UnitBarCity';
import UnitBarState from './UnitBarState';
import UnitBarCountry from './UnitBarCountry';
import UnitBarIDDoc from './UnitBarIDDoc';

import UnitBarDOB from './UnitBarDOB';



import UnitBarGenDOB from './UnitBarGenDOB';
import UnitBarGender from './UnitBarGender';
import UnitBarPosiEmail from './UnitBarPosiEmail';


import UnitAboutIcon from './UnitAboutIcon';
import UnitEducationIcon from './UnitEducationIcon';
import UnitContactIcon from './UnitContactIcon';
import UnitSkillIcon from './UnitSkillIcon';


import UnitBarInstDegree from './UnitBarInstDegree';
import UnitBarAddress from './UnitBarAddress';




import UnitBarAchievement from './UnitBarAchievement';

import UnitAddressIcon from './UnitAddressIcon';



const AboutBasic=(props)=>{

//console.log("props.data: ", props.data);


return (


<div className={classes.about_Basic}>	

	

    <UnitBar/>
    <UnitAboutIcon  userDataUpdated={props.userDataUpdated}/>

  


    <div className={classes.aboutInfoContainer}>



        <div className={classes.InfoBoxLeft}>
           <UnitBarTitle data={props.data} />

            <UnitBarFirstName data={props.data} />

            <UnitBarLastName data={props.data} />

            <UnitBarRole data={props.data} />


	    <UnitBarGender data={props.data} />

            <UnitBarEMail data={props.data} />

            <UnitBarUsername data={props.data} />


           <UnitBarDOB data={props.data}/>

	</div>


        <div className={classes.InfoBoxRight}>


          <UnitBarClass data={props.data} />

          <UnitBarSchool data={props.data} />


          <UnitBarCity data={props.data}/>

	  <UnitBarState data={props.data} />

	  <UnitBarCountry data={props.data} />


          <UnitBarIDDoc  docType={"Office ID"} data={props.data.officeId_doc} idtype={"officeid"} />

	  <UnitBarIDDoc docType={"Govt ID"} data={props.data.govtId1_doc} idtype={"govtid1"} />

	  <UnitBarIDDoc docType={"Date of birth Cert."} data={props.data.dobCert_doc} idtype={"dobdoc"} />

        </div>





    </div>


    <UnitBar/>


  <UnitEducationIcon/>	


     <div className={classes.aboutInfoContainer}>

         <div className={classes.InfoBoxLeft}>



                  {
                    props.data.educationDegrees.map((degree, index)=>{

	            return  <UnitBarInstDegree  key={index}
			         degreeId={degree.id}
			         degree={degree.degreename.name} 
                                 institute={degree.institute.name} 
                                 duration={degree.startDate+" - "+degree.endDate} 
                                 place={degree.institute.city+", "+degree.institute.country}
                                 logo={degree.institute.instlogo}
                                 />





		    })



		  }



         </div>

     </div>


   <UnitBar/>

  <UnitAddressIcon  userData={props.data}/>


   <div className={classes.aboutInfoContainer}>

         <div className={classes.InfoBoxLeft}>

          

               {
                    props.data.addresses.map((address, index)=>{

                    return  <UnitBarAddress addType={"Permanent: "}
			                  key={index}
			                  address={address}
				    />





                    })

              }









        </div>
   </div>


   <UnitBar/>

   <UnitSkillIcon userData={props.data}/>

   <div className={classes.aboutInfoContainer}>

     <div className={classes.InfoBoxLeft}>

 
              {
                    props.data.achievements.map((achievement, index)=>{

                    return  <UnitBarAchievement  key={index}
                                 achievementId={achievement.id}
                                 achievementname={achievement.name}
                                 duration={achievement.startDate+" - "+achievement.endDate}
                                 logo={props.data.profile_image}
                                 />





                    })

              }


     </div>	  

   </div>




</div>	

);


}


export default AboutBasic;
