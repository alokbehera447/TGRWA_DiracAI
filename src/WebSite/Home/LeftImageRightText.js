import classes from "./LeftImageRightText.module.css";
import bookAppointment from "./Block3.jpg";

import picnic from './picnic.jpg';


function LeftImageRightText() {
  return (
    <div className={classes.LeftImageRightTextParent}>
      <div className={classes.websiteContent2}>
	<div>
        <img
          className={classes.HomeImageContainer2}
          src={bookAppointment}
          alt="logo"
        />

        <img
          className={classes.HomeImageContainer2}
          src={picnic}
          alt="logo"
        />



       </div>

        <div className={classes.detailContainer2}>
	  {/*
          <div className={classes.aboutHeading1}>Empowerment</div>
          */}
          <div className={classes.aboutHeading2}> 
	     Trident Galaxy 
	     is more than just a residence; 
	     it's a lifestyle 
	  </div>

          <div className={classes.aboutDetails}>
	     Our association plays a pivotal role as the catalyst, igniting a profound transformation that turns mere living spaces into warm, inviting, and nurturing homes. Moreover, it fosters a sense of belonging that transcends mere acquaintanceship, forging connections that endure for a lifetime, turning neighbors into cherished, lifelong friends. Through a meticulously designed array of initiatives, our relentless dedication is evident. These initiatives span a wide spectrum, from engaging recreational activities that rejuvenate the very core of one's being to enlightening educational workshops that serve to broaden the horizons of the mind. Our ultimate aim is to ensure that we cater comprehensively to the diverse interests and multifaceted needs of our esteemed residents.

As you become a cherished member of the Trident Galaxy Residents Welfare Association, you will discover that you are not just a passive observer, but an active participant. Within our vibrant community, your voice holds significance, your ideas are not only heard but deeply valued, and your dreams and aspirations are actively nurtured and supported. Together, united by a common purpose and bound by a shared sense of community, we embark on a collective journey. Our goal is not merely to construct a thriving residential complex, but to craft a harmonious, shared haven that each of us can proudly and lovingly call home.
          </div>
        </div>
      </div>
    </div>
  );
}

export default LeftImageRightText;
