import React, { useState } from 'react';
import axiosInstance from '../axios';
import { Link } from 'react-router-dom';
import classes from "./Login.module.css"
import LoginHeader from "./LoginHeader";
import LoginFooter from "./LoginFooter";
import logoImage from './BWlogo.JPG'
//import { useHistory } from "react-router-dom";

import {changepassword} from './AllAPICalls'
const Login =(props)=> {

   

   const initialFormData = Object.freeze({
	        username:'',
		email: '',
		password: '',
	});

   const [formData, updateFormData] = useState(initialFormData);


   const [fieldColor, setFieldColor] = useState({borderColor: "lightgrey",borderWidth:"1px"});


   const handleChange = (e) => {
		updateFormData({
			...formData,
			[e.target.name]: e.target.value.trim(),
		});
	};


	const handleSubmit = (e) => {
		e.preventDefault();
		console.log(formData);

		axiosInstance.post(`token/`, {username: formData.username,password: "OLsbd!@#45"+formData.password,})
			.then((res) => {
				localStorage.setItem('access_token', res.data.access);
				localStorage.setItem('refresh_token', res.data.refresh);
				axiosInstance.defaults.headers['Authorization'] =
					'JWT ' + localStorage.getItem('access_token');
				props.setLoggedIn(true);
				//history.push('/');
				//console.log(res);
				//console.log(res.data);
			});
	};   


   const mouseOver=()=>{

   setFieldColor({borderColor: "var(--themeColor)",borderWidth:"1px"});

   }

   const mouseLeave=()=>{

   setFieldColor({borderColor: "lightgrey",borderWidth:"1px"});

   }



  const [showOTPspace, setShowOTPspace]= useState(false);



   const handleSubmitGetOTP=(e)=>{
    e.preventDefault();
    changepassword({formData});
    setShowOTPspace(true);


   } 








return (



<div className={classes.loginDiv}>

  <LoginHeader/>

  <div className={classes.middleDiv}>

     <div className={classes.middleDiv_logo}>  
        <img  className={classes.bwLogo} src={logoImage} alt='edr Logo' />
	<i className={classes.edrTitleText}>edresearch.in</i>

     </div>

     <div className={classes.middleDiv_title}>  Sign in : Request OTP</div>

     { !showOTPspace &&
     <form onSubmit={handleSubmitGetOTP} className={classes.loginForm}>
          <input  
	     onMouseOver={mouseOver}  
	     onMouseLeave={mouseLeave}
	     style={fieldColor} 
	     type="text" 
	     onChange={handleChange} 
	     name="username" 
	     className={classes.email_field} 
	     placeholder="Enter your phone number" 
	
	  />

	  {/*
          <input  
	     onMouseOver={mouseOver} 
	     onMouseLeave={mouseLeave}
	     style={fieldColor} 
	     type="password" 
	     onChange={handleChange} 
	     name="password"  
	     className={classes.password_field} 
	     placeholder="Password"
	     autoComplete="on"
	  />
	  */}

          <button type="submit"  className= {classes.submit_button}>NEXT </button>
     </form>
    }
    { showOTPspace &&

        <form onSubmit={handleSubmit} className={classes.loginForm}>
          <input  
             onMouseOver={mouseOver} 
             onMouseLeave={mouseLeave}
             style={fieldColor} 
             type="password" 
             onChange={handleChange} 
             name="password"  
             className={classes.password_field} 
             placeholder=" _   _   _   _"
             autoComplete="on"
          />

         <button type="submit"  className= {classes.submit_button}>SIGN IN </button>

        </form>
    }







      <div className={classes.accountUtilInfo}>
	{/*
	<Link to="/" className={classes.accountUtilInfo_text}> Forgot password?</Link>  
	*/}
	<Link to="/"className={classes.accountUtilInfo_text}>Dont have an account? Sign Up</Link>   
      </div>


    

  </div>


  <LoginFooter/>


</div>





);






}

export default Login;


