import { useEffect, useState, useRef } from "react";
import classes from "./RulesAndRegulations.module.css";

const RulesAndRegulations = (props) => {
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
    <div className={classes.rulesAndRegulationsParent}>
      <div className={classes.rulesHeading}>Heading Heading Title - 1</div>

      <div className={classes.container1}>
        
        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>

        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>

        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>

        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>
      </div>

      <div className={classes.rulesHeading}>Heading Heading Title - 2</div>

      <div className={classes.container2}>
        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>

        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>

        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>

        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>
      </div>

      <div className={classes.rulesHeading}>Heading Heading Title - 3</div>

      <div className={classes.container3}>
        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>

        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>

        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>

        <div className={classes.rule1}>
          <div className={classes.rightDiv}>
            <div className={classes.circle}></div>

            <div className={classes.rulesTitle}>Heading Heading Title</div>
          </div>

          <div className={classes.rulesdescription}>
            The Badminton World Federation has done a thorough job of compiling
            these rules and laying them out in an organized manner for you to
            learn.{" "}
          </div>
        </div>
      </div>
    </div>
  );
};

export default RulesAndRegulations;
