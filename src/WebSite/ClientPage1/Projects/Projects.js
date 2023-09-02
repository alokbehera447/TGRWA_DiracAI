import {useEffect, useState, useRef} from 'react';

import OneProject from './OneProject';
import classes from "./Projects.module.css"


const Project=(props)=>{

  const isMounted = useRef(false);

   useEffect(() => {
    isMounted.current = true;
    props.passMountInfo(true);


    return () => {
            isMounted.current = false
            props.passMountInfo(false);
    }
   }, [props]);





return <div className={classes.projectMain}>


     <OneProject/>
     <OneProject/>
     <OneProject/>
     <OneProject/>


  </div>

}

export default Project;
