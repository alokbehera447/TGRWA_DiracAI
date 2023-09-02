import React from 'react';
import classes from './LoginHeader.module.css';
//import {AiOutlineHome} from "react-icons/ai";
import {IoMdArrowRoundBack} from 'react-icons/io';



const LoginHeader=()=>{



    const moveToHomeHandler=()=>{



     window.location.href = "/"

    }



return(

<div className={classes.loginHeader}>
 
 <button onClick={moveToHomeHandler} className={classes.goBackHome}>
 <IoMdArrowRoundBack className={classes.homeIcon}/>
 </button>
 

</div>	

);



}

export default LoginHeader;
