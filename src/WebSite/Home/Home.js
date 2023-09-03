import { useEffect, useState, useRef } from "react";

import classes from "./Home.module.css";
import IntroductionBlock from "./IntroductionBlock";
import CenterColumnLeftRightGrid from "./CenterColumnLeftRightGrid";
import Testimonial from "./Testimonial";
import Pricing from "./Pricing";
import FAQ from "./FAQ";
import TeamBlock from "./TeamBlock";
import Appointment from "./Apointment";
import BlogAndNewsBlock from "./BlogAndNewsBlock";
import LeftImageRightText from "./LeftImageRightText";
import OneNewsBlock from "../News/OneNewsBlock";

import innerDiv from '../Website.module.css';





import imageNews1 from './newsImage1.png';
import imageNews2 from './newsImage2.jpeg';








function Home(props) {
  const isMounted = useRef(false);

  useEffect(() => {
    isMounted.current = true;
    props.passMountInfo(true);

    return () => {
      isMounted.current = false;
      props.passMountInfo(false);
    };
  }, [props]);



  let title1="Odisha Govt Notifies New Law For Apartment Ownership";
  let description1="Bhubaneswar: The Odisha government has brought into force a new law to protect ownership of an individual apartment in a building with an undivided interest in common areas and facilities. Governor Ganeshi Lal recently promulgated an ordinance for the purpose.";
  let link1="https://odishabytes.com/odisha-govt-notifies-new-law-for-apartment-ownership-check-details/"	

  let title2="Resident, property owners can't be denied membership of RWA";

  let description2="No resident or property owners of any society can be denied membership of the Residents Welfare Association (RWA), Haryana Agriculture Minister JP Dalal said during the district grievance committee meeting in Gurugram on Tuesday.";

 let link2="https://economictimes.indiatimes.com/news/india/resident-property-owners-cant-be-denied-membership-of-rwa-haryana-agri-minister/articleshow/101928392.cms";






  return (
    <div className={classes.homeParent}>
   
    

   
    <div className={classes.panImageBkg}>	  
         <IntroductionBlock />
    </div>
   
    

    <div className={innerDiv.innerDiv}>	  

     	  
      <CenterColumnLeftRightGrid />
      <LeftImageRightText />

          	  
      <Testimonial />
  
      	  
      <TeamBlock />
      <Appointment />

      	  
      <div className={classes.latest}>
        <div className={classes.latestTitle}>NEWS</div>
        <div className={classes.latestsubTitle}>Latest News</div>
      </div>

      <div className={classes.newsBlock}>
        <OneNewsBlock  title={title1} description={description1} link={link1} image={imageNews1}/>
        <OneNewsBlock  title={title2} description={description2} link={link2} image ={imageNews2}/>
      </div>

      <BlogAndNewsBlock />
      <FAQ /> 
 
     

    </div>	  

   


      
    </div>
  );
}

export default Home;
