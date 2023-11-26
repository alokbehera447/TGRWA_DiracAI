import classes from "./TeamBlock.module.css";
import bookAppointment from "./bookAppointment.jpg";
import pic1 from "./NarayanPati_1.png";
import pic2 from "./debjeetswain.png";
import pic3 from "./PrasantNanda1.png";
import pic4 from "./PratapO.png";
import pic5 from "./NilamaniTripathi.png";


import { FaFacebookF } from "react-icons/fa";

import { AiFillInstagram } from "react-icons/ai";
import { BsTwitter } from "react-icons/bs";



function TeamBlock() {
  return (
    <div className={classes.TeamBlockParent}>
      <div className={classes.parentOurTeam}>
        <div className={classes.ourTeam}>
          <div className={classes.ourTeamTitle}>Our People</div>
          <div className={classes.ourTeamSubTitle}> Office Bearers</div>
        </div>

        <div className={classes.allTeamMemberdetail}>
          
          <div className={classes.ourTeamdetailContainer}>
            <img className={classes.developerPic} src={pic1} alt="logo"></img>

            <div className={classes.developerName}>Narayan Pati</div>

            <div className={classes.developerRole}>President, TGRWA</div>

            <div className={classes.socialNetworking}>
              <FaFacebookF className={classes.pic1} />
              <BsTwitter className={classes.pic2} />
              <AiFillInstagram className={classes.pic3} /> 
            </div>
          </div>

          <div className={classes.ourTeamdetailContainer}>
            <img className={classes.developerPic} src={pic5} alt="logo"></img>

            <div className={classes.developerName}> Nilamani tripathy </div>

            <div className={classes.developerRole}>Vice President, TGRWA</div>

            <div className={classes.socialNetworking}>
              <FaFacebookF className={classes.pic1} />
              <BsTwitter className={classes.pic2} />
              <AiFillInstagram className={classes.pic3} />
            </div>
          </div>

          <div className={classes.ourTeamdetailContainer}>
            <img className={classes.developerPic} src={pic3} alt="logo"></img>

            <div className={classes.developerName}>Prasanta Nanda</div>

            <div className={classes.developerRole}>Secretary, TGRWA </div>

            <div className={classes.socialNetworking}>
              <FaFacebookF className={classes.pic1} />
              <BsTwitter className={classes.pic2} />
              <AiFillInstagram className={classes.pic3} />
            </div>
          </div>





	  <div className={classes.ourTeamdetailContainer}>
            <img className={classes.developerPic} src={pic2} alt="logo"></img>

            <div className={classes.developerName}>Debjeet Swain</div>

            <div className={classes.developerRole}>Joint Secretary, TGRWA </div>

            <div className={classes.socialNetworking}>
              <FaFacebookF className={classes.pic1} />
              <BsTwitter className={classes.pic2} />
              <AiFillInstagram className={classes.pic3} />
            </div>
          </div>







          <div className={classes.ourTeamdetailContainer}>
            <img className={classes.developerPic} src={pic4} alt="logo"></img>

            <div className={classes.developerName}>Pratap Panda</div>

            <div className={classes.developerRole}>Treaserer</div>

            <div className={classes.socialNetworking}>
              <FaFacebookF className={classes.pic1} />
              <BsTwitter className={classes.pic2} />
              <AiFillInstagram className={classes.pic3} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TeamBlock;
