import React,{useState,useEffect} from "react";
import classes from '../Common/MainAppContainer.module.css';
import TopInfoBarSettings from './TopInfoBarSettings';
import TopTitleBar from '../Common/TopTitleBar';



const Settings = (props) =>{

  let title="Settings";	


  const [sideNavBarWidth,setSideNavBarWith]=useState(props.sideNavBarWidth);

  const [profileWidth,setProfileWith]=useState('calc( 100% - var(--sideNavBarWidth) )')	



  useEffect(() => {
      setSideNavBarWith(props.sideNavBarWidth);
      if(props.sideNavBarWidth==="var(--sideNavBarWidth)"){setProfileWith('calc( 100% - var(--sideNavBarWidth) )');}
      if(props.sideNavBarWidth==="var(--sideNavBarWidthOnContract)"){setProfileWith('calc( 100% - var(--sideNavBarWidthOnContract) )');}



   }, [props.sideNavBarWidth]);

  const styles = {color: 'white',backgroundColor: '#919191'}




return (

<div className={classes.mainAppContainer} style={{left:sideNavBarWidth, width:profileWidth}}>


   <TopInfoBarSettings styles={styles}/>
   <TopTitleBar title={title} userData={props.userData}/>		

</div>

);

}



export default Settings;


