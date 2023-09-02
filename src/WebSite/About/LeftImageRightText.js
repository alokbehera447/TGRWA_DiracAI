import classes from "./LeftImageRightText.module.css";
import bookAppointment from "./about.jpg";


function LeftImageRightText() {
  return (
    <div className={classes.LeftImageRightTextParent}>

      <div className={classes.aboutTitle}> About  </div>

      <div className={classes.websiteContent2}>
        <img
          className={classes.HomeImageContainer2}
          src={bookAppointment}
          alt="logo"
        ></img>

        <div className={classes.detailContainer2}>

          <div className={classes.aboutHeading2}>Bimalendu Pradhan</div>

          <div className={classes.aboutDetails}>
             Mr. Kailash Satyarthi, a prominent social reformer and Nobel Peace Laureate, stands out as an exceptional leader and an unwavering advocate for the marginalized and voiceless. In 2014, he was honoured with the Nobel Peace Prize for his tireless crusade against the oppression of children and youth, and his unwavering commitment to ensuring every child's right to education. With Satyarthi Movement for Global Compassion, he exemplifies a life guided by compassion, setting an unmatched standard in the field of social reforms. Through his courageous and persistent advocacy, he has played a pivotal role in shaping ground-breaking legislations worldwide, with the aim of eradicating violence against the powerless. His remarkable efforts have left an indelible mark on the path to a more equitable and just society.


Through his organization, Bachpan Bachao Andolan, Mr. Satyarthi has liberated more than 100,000 children from child labour, slavery, trafficking and other forms of exploitation and developed a successful model for their education, rehabilitation and reintegration into mainstream society. The Global March Against Child Labour, which he led, galvanized support in 103 countries resulting in the adoption of ILO Convention 182 on the Worst Forms of Child Labor, which went on to become the only universally ratified convention in the history of the ILO.

	  </div>
        </div>
      </div>
    </div>
  );
}

export default LeftImageRightText;
