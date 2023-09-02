import classes from "./FAQ.module.css";
import bookAppointment from "./bookAppointment.jpg";
import faqimg from "./faq.jpg";

function FAQ() {
  return (
    <div className={classes.FAQParent}>
      <div className={classes.faqContent}>
        <div className={classes.faqdetailContainer}>
          <div className={classes.faqtextHeading1}>
            Frequently Asked Questions
          </div>

          <div className={classes.qaContainer}>
            <div className={classes.questionsAnsContainer}>
              <div className={classes.imgarrowContainer}></div>

              <div className={classes.questionsText}>
                What is TGRWA?
              </div>
            </div>

            <div className={classes.ansText}>
               TGRWA is the Trident Galaxy Residents Welfare Association, a community organization for residents' well-being and coordination.
            </div>
          </div>
          <div className={classes.qaContainer}>
            <div className={classes.questionsAnsContainer}>
              <div className={classes.imgarrowContainer}></div>

              <div className={classes.questionsText}>
                How can I contact TGRWA?
              </div>
            </div>

            <div className={classes.ansText}>
               Contact TGRWA through our website or office, provided with contact details.
            </div>
          </div>
          <div className={classes.qaContainer}>
            <div className={classes.questionsAnsContainer}>
              <div className={classes.imgarrowContainer}></div>

              <div className={classes.questionsText}>
                 Why join TGRWA?
              </div>
            </div>

            <div className={classes.ansText}>
             Join for enhanced community engagement, problem-solving, to defend your rights as a homebuyer.
	    </div>
          </div>


         <div className={classes.qaContainer}>
            <div className={classes.questionsAnsContainer}>
              <div className={classes.imgarrowContainer}></div>

              <div className={classes.questionsText}>
                 What events are organized? 
              </div>
            </div>

            <div className={classes.ansText}>
	      Regular social gatherings, cultural festivals, workshops, and fitness sessions are organized.
            </div>
          </div>





        </div>

        <img className={classes.faqImages} src={faqimg} alt="logo"></img>
      </div>
    </div>
  );
}

export default FAQ;
