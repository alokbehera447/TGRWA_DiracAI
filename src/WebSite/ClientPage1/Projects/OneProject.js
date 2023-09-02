import classes from "./OneProject.module.css";
import pic from "./ap.jpg";

import { BsBoxArrowUpRight } from "react-icons/bs";

const OneProject = () => {
  return (
    <div className={classes.mainContainer}>
      <div className={classes.oneProject}>
        <img className={classes.imageProject} src={pic} alt="logo"></img>

        <div className={classes.projectName}>Trident Galaxy Apartment</div>

        <div className={classes.discription}>
          Welcome to the forefront of change! I am Bimalendu Pradhan, a
          dedicated RERA activist fueled by a relentless passion to stand up for
          the people and combat the pressing real estate issues that deeply
          affect our communities.With unwavering determination, I strive to be a
          driving force in creating a
        </div>

        <div className={classes.locationContainer}>
          <div className={classes.locationTitle}>Location : </div>
          <div className={classes.location}>Bhubneswar</div>
        </div>

        <div className={classes.launchDateContainer}>
          <div className={classes.launchTitle}>Launch Date : </div>
          <div className={classes.launchDate}>12 - 09 - 2023</div>
        </div>

        <div className={classes.statusContainer}>
          <div className={classes.statusTitle}>Status : </div>
          <div className={classes.status}>In Progress</div>
        </div>

        <div className={classes.reraContainer}>
          <div className={classes.rereTitle}>RERA : </div>
          <div className={classes.rera}>N/A</div>
        </div>

        <div className={classes.bottomContnet}>
          <div className={classes.noOfUnitsContainer}>
            <div className={classes.noofUnitsTitle}>No Of Units : </div>
            <div className={classes.no_fu_units}>1200</div>
          </div>

          <button className={classes.btnRedirect}>
            View In RERA Website <BsBoxArrowUpRight />
          </button>
        </div>
      </div>
    </div>
  );
};

export default OneProject;
