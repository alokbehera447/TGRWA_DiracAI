import { send } from "process";
import classes from "./ContactUs.module.css";
import office from "./OfficeTGRWA.png";

import { MdLocationOn, MdCall, MdEmail } from "react-icons/md";
import { useEffect, useState, useRef } from "react";

const ContactUs = (props) => {
  const isMounted = useRef(false);

  useEffect(() => {
    isMounted.current = true;
    props.passMountInfo(true);

    return () => {
      isMounted.current = false;
      props.passMountInfo(false);
    };
  }, [props]);

  return (
    <div className={classes.contactUsParent}>
      <div className={classes.content}>
        <div className={classes.heading1}>Contact Us</div>

        <div className={classes.headingDetails1}>
          Connecting the dots, empowering change - Contact us and be heard!"
        </div>

        <div className={classes.heading2}>Our Office</div>

        <img
          className={classes.OfficeImageContainer}
          src={office}
          alt="logo"
        ></img>

        <div className={classes.headingDetails1}>
          Share your thoughts, questions, or concerns. We support your advocacy
          for a fair real estate sector. Email us; our team will promptly
          respond.
        </div>

        <div className={classes.bottomDetailsContainer}>
	  {/*
          <div className={classes.firstContainer}>
            <div className={classes.firstTitle}>Cuttack</div>
	  
            <div className={classes.subFIrstContainer}>
              <MdLocationOn className={classes.locationIcon} />

              <div className={classes.firstAddressText}>
                12234/Plot No :39, !0th Phase Nit Colony, Mumbai
              </div>
            </div>

            <div className={classes.subFIrstContainer}>
              <MdCall className={classes.locationIcon2} />

              <div className={classes.firstAddressText}>+91-9876543211</div>
            </div>

            <div className={classes.sub_FIrstContainer}>
              <MdEmail className={classes.locationIcon2} />

              <div className={classes.firstAddressText}>Examples@gmail.com</div>
            </div>
          </div>
	  */}




          <div className={classes.secContainer}>
            <div className={classes.firstTitle}>Bhubaneswar</div>

            <div className={classes.subFIrstContainer}>
              <MdLocationOn className={classes.locationIcon} />

              <div className={classes.firstAddressText}>
                Club House, Trident Galaxy Apartments
              </div>
            </div>

            <div className={classes.subFIrstContainer}>
              <MdCall className={classes.locationIcon2} />

              <div className={classes.firstAddressText}> + 91 9937248258 </div>
            </div>

            <div className={classes.sub_FIrstContainer}>
              <MdEmail className={classes.locationIcon2} />

              <div className={classes.firstAddressText}> tghowa@tridentgalaxyresidents.com </div>
            </div>
          </div>
        </div>
      </div>

      <div className={classes.form}>
        <div className={classes.formContainer}>
          <div className={classes.headingText}>Connect with us</div>

          <div className={classes.horizontalLine}></div>

          <div className={classes.topContainer}>
            <div className={classes.firstContainer}>
              <div className={classes.firstNameText}>First Name :</div>
              <input className={classes.firstNameEditBox} type="text" />
            </div>

            <div className={classes.secContainer}>
              <div className={classes.lastNameText}>Last Name :</div>
              <input className={classes.lastNameEditBox} type="text" />
            </div>
          </div>

          <div className={classes.emailContainer}>
            <div className={classes.textEmail}>Email Address :</div>

            <input className={classes.emailEditBox} type="text" />
          </div>

          <div className={classes.companyContainer}>
            <div className={classes.textCompany}>Company Name :</div>

            <input className={classes.companyEditBox} type="text" />
          </div>

          <div className={classes.phoneContainer}>
            <div className={classes.textphone}>Phone Number :</div>

            <input className={classes.phoneEditBox} type="text" />
          </div>

          <div className={classes.messageContainer}>
            <div className={classes.textMessage}>Message :</div>

            <input className={classes.messageEditBox} type="text" />
          </div>

          <div className={classes.sendBtnContainer}>
            <div className={classes.sendBtn}>Send</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ContactUs;
