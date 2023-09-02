import classes from "./Header.module.css";

import {
  BsFacebook,
  BsTwitter,
  BsLinkedin,
  BsYoutube,
  BsEnvelope,
} from "react-icons/bs";
import { AiFillTwitterCircle } from "react-icons/ai";

import { FaFacebookF, FaLinkedinIn } from "react-icons/fa";

const HeaderAddressBar = () => {


  const facebookHandler=()=>{

    window.open('https://www.facebook.com/pages/Trident-Galaxy/1274159099348085', '_blank');	  
  }


  const youtubeHandler=()=>{

    window.open('https://www.youtube.com/@tridentgalaxyresidentswelf2614/videos','_blank');	  

  }	

  
  const linkedInHandler=()=>{


  } 	


  const twitterHandler=()=>{



  }





  return (
    <div className={classes.topbar}>
      <div className={classes.inner_topbar}>


        <div className={classes.rightContainer}>
          <div className={classes.firstTopContainer}>
            <div className={classes.emailIcon}>
              <BsEnvelope size={20} />
            </div>
            <div className={classes.textEmail}>
              tghowa@tridentgalaxyresidents.com
            </div>

          </div>

          {/*
               <div className={classes.secTopContainer}>
                  <div className={classes.mobileIcon}></div>
                  <div className={classes.mobileNumber}>+91 929399494959</div>
               </div>
	       */}
        </div>

        <div className={classes.socialiconContainer}>
          <button className={classes.fbicon} onClick={facebookHandler}>
            <FaFacebookF size={20} />
          </button>
          <button className={classes.fbicon} onClick={facebookHandler}>
            <BsTwitter size={20} />
          </button>
          <button className={classes.fbicon} onClick={facebookHandler}>
            <FaLinkedinIn size={20} />
          </button>
          <button className={classes.fbicon} onClick={youtubeHandler}>
            <BsYoutube size={25} />
          </button>
        </div>

        
      </div>
    </div>
  );
};

export default HeaderAddressBar;
