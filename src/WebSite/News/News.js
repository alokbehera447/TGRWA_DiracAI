import { useEffect, useState, useRef } from "react";

import BlogAndNewsBlock from "./BlogAndNewsBlock";
import OneFriend from "../../MainApps/Account/UserProfile/Friends/OneFriend";
import OneNewsBlock from "./OneNewsBlock";
import classes from "./News.module.css";

import imageNews1 from '../Home/newsImage1.png';
import imageNews2 from '../Home/newsImage2.jpeg';
import imageNews3 from './News3.png';

import imageNews4 from './News4.png';



const News = (props) => {
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


  let title3="Flat Owners Don't Forfeit Right To Claim Amenities Promised By ...";
  let description3="The Supreme Court has observed that that flat-owners, who are often forced by the circumstances to take possession of apartments even if the amenities promised by the builder are not provided, do not forfeit their right to claim such services from the builder.A bench comprising Justices S Ravindra ...";
  let link3="https://www.livelaw.in/top-stories/flat-owners-dont-forfeit-right-to-claim-amenities-promised-by-builder-by-taking-possession-of-apartments-supreme-court-221199";


  let title4="Bhubaneswar to get Anand Van on 90 acre by end of year";
  let description4="BHUBANESWAR: The state capital will soon get an urban forest on over 90 acre land where residents could go on trail, cycling and trekking and get closure to the nature.The urban forest is being planned to be created by the city forest division with the help of Odisha Mining Corporation (OMC) and Bhubaneswar..";
  let link4="https://www.newindianexpress.com/cities/bhubaneswar/2023/jan/14/bhubaneswar-to-get-anand-van-on-90-acre-by-end-of-year-2537813.html";





  return (
    <div className={classes.parentContainer}>
      <div className={classes.latest}>
        <div className={classes.latestTitle}>NEWS</div>
        <div className={classes.latestsubTitle}>Latest News</div>
      </div>

      <div className={classes.newsContainer}>
         <OneNewsBlock  title={title1} description={description1} link={link1} image={imageNews1}/>
         <OneNewsBlock  title={title2} description={description2} link={link2} image ={imageNews2}/>
         <OneNewsBlock  title={title3} description={description3} link={link3} image={imageNews3}/>
        <OneNewsBlock  title={title4} description={description4} link={link4} image ={imageNews4}/>
      </div>
    </div>
  );
};

export default News;
