import classes from "./CenterColumnLeftRightGrid.module.css";
import bookAppointment from "./g_affordable (copy).png";
import centerPic from "./center_img.jpg";
import SecondBlockImage from "./SecondBlockImage2.png";
import LogoWatchDog from "./g_Real_estate.png";
import Enthusiast from "./g_community_development.png";
import Defender from "./g_consumer_right.png";
import Policy from "./g_policy_Reform_efforts.png";


import icon1 from './icon1.png';
import icon2 from './icon2.png';
import icon3 from './icon3.png';
import icon4 from './icon4.png';
import icon5 from './icon5.png';
import icon6 from './icon6.png';




import Block2Image from "./Block2_v2.jpg";

import Transparency from "./g_Transperency_Crusader.png";

import { HiPresentationChartBar } from "react-icons/hi";

function CenterColumnLeftRightGrid() {
  return (
    <div className={classes.centerImageLeftRightGrid}>
      <div className={classes.title}>About</div>
      <div className={classes.subTitle}>Our Endeavors</div>

      <div className={classes.serviceSection}>
        <div className={classes.leftSideContent}>
          <div className={classes.a1box}>
            <img
              className={classes.serviceImage}
              src={icon6}
              alt="logo"
            ></img>

            <div className={classes.detailsServiceContainer}>
              <div className={classes.serviceHeading1}>
                Community Events
              </div>

              <div className={classes.serviceHeading2}>
	        Engage in lively gatherings fostering connections and camaraderie among neighbors, creating lasting memories.
              </div>
            </div>
          </div>

          <div className={classes.a1box}>
            <img
              className={classes.serviceImage}
              src={icon2}
              alt="logo"
            ></img>

            <div className={classes.detailsServiceContainer}>
              <div className={classes.serviceHeading1}>
                Community Development
              </div>

              <div className={classes.serviceHeading2}>
                Building sustainable Residents Welfare Associations -
                Collaborating for a better future.
              </div>
            </div>
          </div>

          <div className={classes.a1box}>
            <img
              className={classes.serviceImage}
              src={icon5}
              alt="logo"
            ></img>

            <div className={classes.detailsServiceContainer}>
              <div className={classes.serviceHeading1}>
                Grievance Support: 
              </div>

              <div className={classes.serviceHeading2}>
                A dedicated channel to address concerns, ensuring a swift resolution and fostering a harmonious living environment.
              </div>
            </div>
          </div>
        </div>

        <img className={classes.centerImage} src={Block2Image} alt="logo"></img>

        <div className={classes.rightSideContent}>
          <div className={classes.a1box}>
            <img
              className={classes.serviceImage}
              src={icon1}
              alt="logo"
            ></img>

            <div className={classes.detailsServiceContainer}>
              <div className={classes.serviceHeading1}>
                Transparency Crusaders
              </div>

              <div className={classes.serviceHeading2}>
                Shedding light on hidden agendas - Making real estate
                accountable for all.
              </div>
            </div>
          </div>

          <div className={classes.a1box}>
            <img
              className={classes.serviceImage}
              src={icon4}
              alt="logo"
            ></img>

            <div className={classes.detailsServiceContainer}>
              <div className={classes.serviceHeading1}>
                Consumer Rights Protection
              </div>

              <div className={classes.serviceHeading2}>
                Ensuring buyers' interests are safeguarded - Standing up against
                exploitative practices.
              </div>
            </div>
          </div>

          <div className={classes.a1box}>
            <img className={classes.serviceImage} src={icon3} alt="logo"></img>

            <div className={classes.detailsServiceContainer}>
              <div className={classes.serviceHeading1}>
                Policy Reform Efforts
              </div>

              <div className={classes.serviceHeading2}>
                Advocating for legislative changes to address housing
                inequalities.{" "}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default CenterColumnLeftRightGrid;
