import classes from "./Testimonial.module.css";
import bookAppointment from "./bookAppointment.jpg";
import t1 from "./t1.jpg";
import t2 from "./RajendraSahoo.jpeg";
import t3 from "./Kiran1.jpeg";

import Arindam from "./Arindam.jpeg";

import { AiFillTwitterCircle } from "react-icons/ai";

function Testimonial() {
  return (
    <div className={classes.TestimonialParent}>
      <div className={classes.ourClientDetails}>
        <div className={classes.clientTitle}> Voices of Change </div>
        <div className={classes.clientSubTitle}>What people say..</div>

        <div className={classes.clientFeedbackContainer}>
          
          <div className={classes.aboutClinetBox}>
            <div className={classes.clientFeedback}>
              <img className={classes.clientImg} src={Arindam} alt="logo"></img>

              <AiFillTwitterCircle className={classes.socialNetworkImage} />
            </div>

            <div className={classes.clientDetails}>
	      TGRWA has transformed our community. Their events and initiatives foster unity and make our residence truly feel like home
            </div>

            <div className={classes.clientName}>Arindam Choudhury</div>

            <div className={classes.clientStatus}>
              Former Secretary (Trident Galaxy Residential Welfare Association)
            </div>
          </div>

          <div className={classes.aboutClinetBox}>
            <div className={classes.clientFeedback}>
              <img className={classes.clientImg} src={t2} alt="logo"></img>

              <AiFillTwitterCircle className={classes.socialNetworkImage} />
            </div>
            <div className={classes.clientDetails}>
	      Joining TGRWA was the best decision. Their dedicated committees ensure smooth living, and I've made wonderful friends through their events.
            </div>

            <div className={classes.clientName}>Dr Rajendra Sahoo</div>

            <div className={classes.clientStatus}>
              Resident , Trident Galaxy
            </div>
          </div>

          <div className={classes.aboutClinetBox}>
            <div className={classes.clientFeedback}>
              <img className={classes.clientImg} src={t3} alt="logo"></img>

              <AiFillTwitterCircle className={classes.socialNetworkImage} />
            </div>
            <div className={classes.clientDetails}>
	      TGRWA's events celebrate our diversity. From cultural festivals to fitness workshops, they bring everyone together in the spirit of camaraderie.
            </div>

            <div className={classes.clientName}>Kiran Samantray</div>

            <div className={classes.clientStatus}>Resident, Trident Galaxy </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Testimonial;
