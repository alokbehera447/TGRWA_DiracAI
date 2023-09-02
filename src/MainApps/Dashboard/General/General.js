import React,{useState,useEffect,useRef} from "react";
import classes from "../../CommonAppUtilities/MainAppContainer.module.css"

import GeneralContentDiv from './GeneralContentDiv';


import {BsLayoutTextSidebarReverse, BsFillCameraReelsFill, BsPencilSquare} from 'react-icons/bs';
import {GiTeacher} from "react-icons/gi";

import {CgClipboard} from 'react-icons/cg';







const General=(props)=>{

    
   const [sideNavBarWidth,setSideNavBarWidth]=useState( "calc( 0.5% + "+props.sideNavBarWidth+" )");
   const [mainAppContainerWidth,setMainAppContainerWidth]=useState('calc( 99% - var(--sideNavBarWidth) )');	

   const isMounted = useRef(false);


   useEffect(() => {
      isMounted.current = true;	   
      setSideNavBarWidth("calc( 0.5% + "+props.sideNavBarWidth+" )");
      if(props.sideNavBarWidth==="var(--sideNavBarWidth)"){setMainAppContainerWidth('calc( 99% - var(--sideNavBarWidth) )');}
      if(props.sideNavBarWidth==="var(--sideNavBarWidthOnContract)"){setMainAppContainerWidth('calc( 99% - var(--sideNavBarWidthOnContract) )');}


      return () => { 
      }

   }, [props.sideNavBarWidth]);


   useEffect(() => {
    isMounted.current = true;
    props.passMountInfo(true);	   
    return () => { 
	    isMounted.current = false 
            props.passMountInfo(false);
    }
   }, [props]);







   let title="General"	
   let mainAppContainerStyle = {
	   left: sideNavBarWidth, 
	   width: mainAppContainerWidth
   }
   const infoBarActiveButtonColor = {color: 'white',backgroundColor: '#919191'}

   const showcreateCourseForm=()=>{

   }




   return(

      <div className={classes.mainAppContainer} style={mainAppContainerStyle} >
       
	   
          <GeneralContentDiv 
	     userData = {props.userData}
	     rerender={props.rerender}
	     />
           

        </div>
      

   );
}

export default General;

