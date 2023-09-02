import classes from "./Footer.module.css";

import { MdOutlineWatchLater } from "react-icons/md";

import { AiOutlineMail } from "react-icons/ai";

import {
  MdCall,
  MdAccessTimeFilled,
  MdEmail,
  MdLocationPin,
} from "react-icons/md";

import Logo from './tgrwalogo.png';




function Footer() {

 const redirectDiracAIHandler=()=>{
   window.open('https://diracai.com/services/', '_blank');
 }


return (
    <div className={classes.footer}>
      <div className={classes.mainFooterContainer}>

        <div className={classes.block1}>
          <div className={classes.logotextContainer}>
            <div className={classes.logopic}>
              <div className={classes.csslogo}>
                <img src={Logo} className={classes.logoImage}/>
	      </div>
            </div>
            <div className={classes.websiteNametext}>TGRWA</div>
          </div>

          <div className={classes.websiteDetail}>
	   
           Trident Galaxy Residents Welfare Association is a registered organization with identification no : Regd No- 2586-62/ 2019-2020. We are open from monday to saturday.
             

          </div>

          <div className={classes.cont4}>
            <MdAccessTimeFilled className={classes.cont4Icon} />


            <div className={classes.cont4textContainer}>
              <div className={classes.cont4Title1}>Monday - Saturday</div>
              <div className={classes.cont4Title2}>9:00am - 5:00pm</div>
            </div>
          </div>
        </div>
        <div className={classes.block2}>
          <div className={classes.otherLink}>Other Links</div>

          <div className={classes.cont1}>
            <div className={classes.cont1Icon}></div>
            <div className={classes.cont1Text}>Home</div>
          </div>

          <div className={classes.cont1}>
            <div className={classes.cont1Icon}></div>
            <div className={classes.cont1Text}>About</div>
          </div>

          <div className={classes.cont1}>
            <div className={classes.cont1Icon}></div>
            <div className={classes.cont1Text}>News</div>
          </div>

          <div className={classes.cont1}>
            <div className={classes.cont1Icon}></div>
            <div className={classes.cont1Text}>Residents</div>
          </div>

          <div className={classes.cont1}>
            <div className={classes.cont1Icon}></div>
            <div className={classes.cont1Text}>Contact Us</div>
          </div>
        </div>
        <div className={classes.block3}>
          <div className={classes.otherLink}>Services</div>

          <div className={classes.cont1}>
            <div className={classes.cont1Icon}></div>
            <div className={classes.cont1Text}>Fair Housing Advocacy</div>
          </div>

          <div className={classes.cont1}>
            <div className={classes.cont1Icon}></div>
            <div className={classes.cont1Text}>Tenant Support Network</div>
          </div>

          <div className={classes.cont1}>
            <div className={classes.cont1Icon}></div>
            <div className={classes.cont1Text}>
              Affordable Housing Initiatives
            </div>
          </div>

          <div className={classes.cont1}>
            <div className={classes.cont1Icon}></div>
            <div className={classes.cont1Text}>Rent Control Campaigns</div>
          </div>

          <div className={classes.cont1}>
            <div className={classes.cont1Icon}></div>
            <div className={classes.cont1Text}>
              Community Engagement Projects
            </div>
          </div>
        </div>
        <div className={classes.block4}>
          <div className={classes.otherLink}>Contact Us</div>

          <div className={classes.cont4}>
            <MdLocationPin className={classes.cont4Icon} />

            <div className={classes.cont4textContainer}>
              <div className={classes.cont4Title1}>
                Club House, Trident Galaxy Apartments
              </div>
              <div className={classes.cont4Title2}>Kalinga Nagar, Bhubaneswar</div>
            </div>
          </div>

          <div className={classes.cont4}>
            <MdCall className={classes.cont4Icon} />

            <div className={classes.cont4textContainer}>
              <div className={classes.cont4Title1}>+ 91 9937248258</div>

              <div className={classes.cont4Title2}>+ 91 9937248258</div>
            </div>
          </div>

          <div className={classes.cont4}>
            <MdEmail className={classes.cont4Icon} />

            <div className={classes.cont4textContainer}>
              <div className={classes.cont4Title1}>tghowa@tridentgalaxyresidents.com</div>
            </div>
          </div>
        </div>
      </div>

      

      <div className={classes.bottomBar}>
        <div className={classes.horiLine}></div>

        <div className={classes.text1}>
          Copyright 2023 © tgrwa.in All rights reserved.
        </div>

        <div className={classes.cmpDetail}>
          <div className={classes.powerBy}>Powered By</div>

          <div className={classes.footerLogoBtn}>

            <button className={classes.websiteDetails} onClick={redirectDiracAIHandler}>
	       <div className={classes.logo}>Di</div>
	       <div style={{marginLeft:"10px"}}>DiracAI Services</div>
	    </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Footer;
