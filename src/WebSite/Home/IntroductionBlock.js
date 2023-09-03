import classes from "./IntroductionBlock.module.css";
import bookAppointment from "./owner.jpg";

//Through tireless advocacy, community engagement, and policy reform initiatives, I am committed to challenging the status quo and breaking down the barri//ers that hinder equitable access to housing. My mission is to uplift marginalized voices, empower vulnerable individuals, and foster a society where eve//ryone can thrive in a place they proudly call home.
{
  /*With unwavering determination, I strive to be a driving force in creating a brighter future where housing is recognized as a fundamental human right, not a mere privilege reserved for the fortunate few. I firmly believe that safe and affordable homes are the cornerstone of strong and empowered communities.
   */
}

function IntroductionBlock() {
  return (
    <div className={classes.IntroductionBlockParent}>
      <div className={classes.websiteContent}>
        <div className={classes.detailContainer}>
          <div className={classes.textHeading1}>Trident Galaxy Residents' Welfare Association!</div>

          <div className={classes.textHeading2}>
               Uniting Hearts, Nurturing Community:  Where Every Home is Family            
          </div>

          <div className={classes.textDetails}>
	     Welcome to the Trident Galaxy Residents Welfare Association! We are a vibrant and cohesive community nestled within the captivating Trident Galaxy residential complex. With a shared vision of fostering a harmonious and enriched living experience for all residents, our association takes pride in serving as the nexus that binds this exquisite neighborhood together.
          </div>
        </div>

      </div>
    </div>
  );
}

export default IntroductionBlock;
