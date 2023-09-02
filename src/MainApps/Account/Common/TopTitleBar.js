import React from "react";

import classes from './TopTitleBar.module.css';
import { useHistory } from "react-router-dom";


import {BsArrowLeft} from 'react-icons/bs';


const TopTitleBar=(props)=>{

let history = useHistory();


	
const goBackHandler=()=>{

if(props.userData.usertype===4 ){
history.push("/dashboard/employee");
}else{

history.push("/dashboard/general");
}


}	




return (

<div className={classes.topTitleBar}>

       <i className={classes.topTitleBar__Text}>
          {/*
          <button className={classes.backButton} onClick={goBackHandler}> <BsArrowLeft className={classes.backIcon}/> </button>
          */}
	<b>{props.title} </b>

	</i>

</div>

);

}


export default TopTitleBar;
