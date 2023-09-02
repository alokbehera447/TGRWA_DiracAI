import React from "react";
import classes from './AboutBasic.module.css';


import UnitBar from './UnitBar';
import UnitBarFirstName from './UnitBarFirstName';
import UnitBarLastName from './UnitBarLastName';
import UnitBarRole from './UnitBarRole';
import UnitBarEMail from './UnitBarEMail';

import UnitBarClass from './UnitBarClass';
import UnitBarSchool from './UnitBarSchool';
import UnitBarCity from './UnitBarCity';
import UnitBarState from './UnitBarState';
import UnitBarCountry from './UnitBarCountry';
import UnitBarTitle from './UnitBarTitle';


import UnitBarGenDOB from './UnitBarGenDOB';
import UnitBarGender from './UnitBarGender';
import UnitBarPosiEmail from './UnitBarPosiEmail';


import UnitAboutIcon from './UnitAboutIcon';
import UnitEducationIcon from './UnitEducationIcon';
import UnitContactIcon from './UnitContactIcon';
import UnitBarInstDegree from './UnitBarInstDegree';




import UnitBarAchievement from './UnitBarAchievement';

import UnitSkillIcon from '../Advanced/UnitSkillIcon';



const AboutBasic=(props)=>{


   console.log("props.data.educationDegrees: ", props.data.educationDegrees);

   const dateformat=(date)=>{

    let date_=String(date);
   
    if (date_ !==null){

        let year=date_.split("-").at(0);
        let month=date_.split("-").at(1);
        let day= date_.split("-").at(2);
  
	let monthMap = {"01":"Jan", "02":"Feb","03":"March",
		"04":"April","05":"May","06":"Jun","07":"July",
		"08":"Sept","09":"Oct","10":"Oct",  "11":"Nov","12":"Dec"}    
        let monthName= monthMap[month];   
 
	let reObj = monthName+" "+year;    

      return reObj;

      }



     return "N/A"


   }





return (


<div className={classes.about_Basic}>	

   	
    	

    <UnitBar/>
    <UnitAboutIcon  userDataUpdated={props.userDataUpdated}/>

  


    <div className={classes.aboutInfoContainer}>



        <div className={classes.InfoBoxLeft}>

	    <UnitBarTitle data={props.data} />
            <UnitBarFirstName data={props.data} />

            <UnitBarLastName data={props.data} />
            {/*
            <UnitBarRole data={props.data} />
            */}

	    <UnitBarGender data={props.data} />

            <UnitBarEMail data={props.data} />

	</div>


        <div className={classes.InfoBoxRight}>

          {/*
          <UnitBarClass data={props.data} />
           */}
          <UnitBarSchool data={props.data} />


          <UnitBarCity data={props.data} />

	  <UnitBarState data={props.data} />

	  <UnitBarCountry data={props.data} />


        </div>



	
	


    </div>


    <UnitBar/>


  <UnitEducationIcon/>	


     <div className={classes.aboutInfoContainer}>

         <div className={classes.InfoBoxLeft}>


                 { props.data.educationDegrees.length > 0 &&
                    props.data.educationDegrees.map((degree, index)=>{

                    let startdate_= degree.startDate;
		    let startDate_=dateformat(startdate_);	    
                    let enddate_= degree.endDate;
                    let endDate_=dateformat(enddate_);



                    return  <UnitBarInstDegree  key={index}
                                 degree={ degree.degreename !=null ? degree.degreename.name:"N/A"}
                                 institute={ degree.institute !=null? degree.institute.name:"N/A"}
                                 duration={startDate_ +" - "+ endDate_}
                                 place={ degree.institute !=null ? degree.institute.city+", "+degree.institute.country:"N/A"}
                                 logo={ degree.institute !=null ? degree.institute.instlogo: "N/A"}
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
