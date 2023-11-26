import { useEffect, useState, useRef } from "react";
import classes from "./RulesAndRegulations.module.css";

import OnlineRegistrationHome from './../OnlineRegistration/OnlineRegistrationHome_v1';

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
    


     <OnlineRegistrationHome/>





    </div>
  );
};

export default RulesAndRegulations;
