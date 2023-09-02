import { useEffect, useState, useRef } from "react";

import classes from "./About.module.css";

import LeftImageRightText from "./LeftImageRightText";
import RightImageLeftText from "./RightImageLeftText";

import office from "./Block2.jpg";
import aboutimage2 from "./aboutimage2.jpg";
import p1 from "./p1.png";

import aboutimage3 from "./aboutimage3.jpg";

import checklist from "./checklist.png";

import Team from "../Home/TeamBlock";


const About = (props) => {
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
    <div className={classes.about}>
      <div className={classes.topTitle}>
        <h2>About </h2>

      </div>

      <div className={classes.aboutbox}>
        <div className={classes.leftBox}>
          <img
            className={classes.OfficeImageContainer}
            src={office}
            alt="logo"
          ></img>
        <div className={classes.whyChooseUsDescription}>
	  TGRWA being awarded by Sulochana Das, Mayor - Bhubaneswar for their contributions during the pandemic
        </div>




        </div>


        <div className={classes.RightBox}>
          <div className={classes.p1}>
           The Trident Galaxy Residents Welfare Association, registered under number 2586-62/2019-2020, was established in 2017 with the primary objective of enhancing the quality of life and fostering a sense of community among the residents of the Trident Galaxy residence. Since its inception, the association has been actively involved in organizing various welfare programs and initiatives aimed at improving the well-being of its members. These activities include maintenance and beautification of common areas, security enhancements, cultural events, and social gatherings that promote a sense of belonging among the residents. With its dedicated efforts and commitment to creating a harmonious living environment, the Trident Galaxy Residents Welfare Association continues to play a vital role in ensuring the welfare and happiness of its community members.


	  </div>

          <div className={classes.p2}>

           In addition to its ongoing commitment to enhancing the quality of life for Trident Galaxy residents, the association has also taken proactive steps to embrace sustainability and environmental stewardship. We have initiated projects to reduce our carbon footprint and promote eco-friendly practices within our community. From recycling initiatives to energy conservation programs, the Trident Galaxy Residents Welfare Association strives to create a greener and more sustainable living environment for all our members. By fostering a sense of responsibility towards the environment alongside our dedication to community well-being, we aim to create a holistic and vibrant living experience within the Trident Galaxy residence.

          </div>

          <div className={classes.p3}>

          </div>

          <div className={classes.getintouchParentDiv}>Get In Touch</div>
        </div>
      </div>

      <div className={classes.aboutbox2}>
        <div className={classes.RightBox1}>
          <div className={classes.p1}>
	    At Trident Galaxy Bhubaneswar, we envision more than just a collection of residences; we imagine a community where interactions blossom into friendships and where each individual's well-being is a shared concern. Our Residents Welfare Association is guided by the belief that a harmonious living environment is the cornerstone of a fulfilling life. We strive to create a space where diversity is celebrated, events spark joy, and support is readily available. Our vision is to be more than just a dwelling place – we aim to be a catalyst for a life lived to its fullest potential, enriched by the bonds we forge and the experiences we create together. Welcome to Trident Galaxy, where modern luxury finds its true meaning within a close-knit and vibrant community.
          </div>

          <div className={classes.p2}>
	   At Trident Galaxy Bhubaneswar, our commitment to fostering a vibrant community extends beyond the boundaries of our residence. We actively engage with the broader local community through outreach programs and charitable initiatives. Through partnerships with local organizations, we participate in efforts to uplift the underprivileged and contribute to the betterment of the society we are a part of. Our aim is to not only enhance the lives of our residents but also leave a positive impact on the surrounding neighborhoods. By embodying the values of social responsibility and civic engagement, Trident Galaxy Residents Welfare Association aims to be a beacon of positive change, making our community a better place for all.
	  </div>

          <div className={classes.p3}>
          </div>

          <div className={classes.getintouchParentDiv}>Get In Touch</div>
        </div>

        <div className={classes.leftBox1}>
          <img
            className={classes.OfficeImageContainer}
            src={aboutimage2}
            alt="logo"
          ></img>
        </div>
      </div>





      

      <div className={classes.whyChooseUsTitle}>Mission </div>
      
      <div className={classes.whyChooseUsDescription}>
	   The mission statement of TGRWA outlines the association’s purpose and the core objectives it aims to achieve for the benefit of its residents. It includes
      </div>
     



      <div className={classes.whyChooseUsContainer}>



        <div className={classes.block1st}>
          <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>

            <div className={classes.boxTitle}>Community Well-being</div>

            <div className={classes.boxDesc}>
	      To enhance the overall quality of life for residents by fostering a sense of belonging, safety, and well-being within the community.
            </div>
          </div>


          <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>

            <div className={classes.boxTitle}>Maintenance and Infrastructure:</div>

            <div className={classes.boxDesc}>
	       To ensure the upkeep and improvement of common areas, facilities, and infrastructure to meet residents' needs and expectations.
            </div>
          </div>
        </div>




        <div className={classes.block2st}>
          <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>

            <div className={classes.boxTitle}> Security</div>

            <div className={classes.boxDesc}>
	      To provide a secure and safe living environment through vigilant security measures and crime prevention initiatives.
            </div>
          </div>

          <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>

            <div className={classes.boxTitle}>Communication: </div>

            <div className={classes.boxDesc}>
	       To facilitate open and transparent communication between residents, the RWA, and relevant authorities.
            </div>
          </div>
        </div>
      </div>


       <div className={classes.block2st}>
          <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>

            <div className={classes.boxTitle}> Social and Cultural Engagement:</div>

            <div className={classes.boxDesc}>
	      To promote community engagement and social cohesion through events, cultural programs, and recreational activities.
            </div>
          </div>



      </div>





      <div className={classes.whyChooseUsTitle}>Vision</div>

      <div className={classes.whyChooseUsDescription}>
	   The vision statement of TGRWA outlines the long-term goals and aspirations for the community. It includes:
      </div>




      <div className={classes.whyChooseUsContainer}>

          <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>
            <div className={classes.boxTitle}>Sustainable Living: </div>
            <div className={classes.boxDesc}>
	      To create a sustainable and environmentally responsible community that conserves resources and promotes eco-friendly practices.
            </div>
          </div>


          <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>
            <div className={classes.boxTitle}> Inclusivity: </div>
            <div className={classes.boxDesc}>
	      To foster an inclusive and diverse community where residents of all backgrounds feel welcome and valued.
            </div>
          </div>

           <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>
            <div className={classes.boxTitle}> Community Empowerment: </div>
            <div className={classes.boxDesc}>
	      To empower residents to actively participate in decision-making processes and contribute to the betterment of the community.
            </div>
        </div>

      </div>



     <div className={classes.whyChooseUsContainer}>

          <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>
            <div className={classes.boxTitle}> Quality Living: </div>
            <div className={classes.boxDesc}>
	      To continually improve the quality of life by maintaining high standards of cleanliness, aesthetics, and services.
            </div>
          </div>


          <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>
            <div className={classes.boxTitle}> Resident Engagement: </div>
            <div className={classes.boxDesc}>
	     To encourage residents to take pride in their community, actively participate in RWA activities, and contribute to the overall betterment of the neighborhood.
            </div>
          </div>

           <div className={classes.box1}>
            <img className={classes.boxImg} src={checklist} alt="logo"></img>
            <div className={classes.boxTitle}> Safety and Security: </div>
            <div className={classes.boxDesc}>
	       To establish a reputation for being a safe and secure place to live, where residents can enjoy peace of mind.
            </div>
        </div>

      </div>





      <div className={classes.whyChooseUsDescription}>
	  It's important to note that the specific mission and vision of TGRWA may evolve over time in response to changing community needs and priorities. Therefore, regular communication and feedback from residents are essential to ensure that the RWA's mission and vision align with the current desires and expectations of the community members.
      </div>






	<Team/>





      <div className={classes.process}>
        <div className={classes.processBox1}>
          <div className={classes.processTitle}> Work and Achievements </div>

          <div className={classes.processDesc}>
	    These works highlight the multifaceted role that TGRWA play in enhancing the quality of life in residential communities and their dedication to addressing various community needs and concerns.
          </div>


          <img className={classes.processImage} src={aboutimage3} alt="logo"></img>
        </div>

        <div className={classes.processBox2}>
          <div className={classes.processCard}>
            <img className={classes.cardIcon} src={p1} alt="logo"></img>

            <div className={classes.processContent}>
              <div className={classes.title}> Protecting Home Buyers' Rights </div>

              <div className={classes.processDesc}>
	        Advocate for fair housing practices, address maintenance issues, and represent residents in dealings with builders and promoters, ensuring the rights of homebuyers are protected by interventions in H'ble High Court and RERA Odisha. 
              </div>
            </div>
          </div>

          <div className={classes.processCard}>
            <img className={classes.cardIcon} src={p1} alt="logo"></img>

            <div className={classes.processContent}>
              <div className={classes.title}> Cultural Activities:</div>

              <div className={classes.processDesc}>
	         Organize cultural like Ganesh Puja, Saraswati Puja, Independence Day, Republic Day and many other events to foster unity, celebrate diversity, and promote social interaction among residents.

              </div>
            </div>
          </div>

          <div className={classes.processCard}>
            <img className={classes.cardIcon} src={p1} alt="logo"></img>

            <div className={classes.processContent}>
              <div className={classes.title}> Peripheral Development: </div>

              <div className={classes.processDesc}>
	        Collaborate with local authorities to address road repairs, electic pole set up, Mo Bus initiatives, Anand Van development, and other development-related issues to improve the overall well-being of residents.
              </div>
            </div>
          </div>

          <div className={classes.processCard}>
            <img className={classes.cardIcon} src={p1} alt="logo"></img>

            <div className={classes.processContent}>
              <div className={classes.title}>Social Activities and Philanthropy: </div>

              <div className={classes.processDesc}>
	        Engage in charitable efforts like collecting and donating items to the needy, contributing to societal betterment and social responsibility.

              </div>
            </div>
          </div>

          <div className={classes.processCard}>
            <img className={classes.cardIcon} src={p1} alt="logo"></img>

            <div className={classes.processContent}>
              <div className={classes.title}>Environmental Initiatives:</div>

              <div className={classes.processDesc}>
	       Work on environmental projects such as tree planting and clean-up activities to maintain a clean and green environment within the community.

              </div>
            </div>
          </div>

          <div className={classes.processCard}>
            <img className={classes.cardIcon} src={p1} alt="logo"></img>

            <div className={classes.processContent}>
              <div className={classes.title}>Community Management Best Practices:</div>

              <div className={classes.processDesc}>
	        Strive to bring the best practices in community management to ensure efficient and effective governance and services for residents.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className={classes.aboutLastSection}>
        <div className={classes.lastSectionTitle1}> Join us today</div>

        <div className={classes.lastSectiondesc1}>
        Thank you for visiting! Your support means the world to me. If you have any questions or inquiries, feel free to contact me. Have a great day!
        </div>

        <div className={classes.lastSectionBtn}>Get In Touch</div>
      </div>
    </div>
  );
};

export default About;
