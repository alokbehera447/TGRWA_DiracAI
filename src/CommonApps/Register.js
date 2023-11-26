import React, { useState, useEffect, CSSProperties } from "react";
import LoginHeader from "./LoginHeader";
import classes from './Register.module.css';
//import {OptionField} from './OptionField';
import {createaccountwithmobileno, checkuserexist} from './AllAPICalls';
import FadeLoader from "react-spinners/FadeLoader";
import {BsCheckLg} from 'react-icons/bs';
//import { useNavigate } from "react-router-dom";

import Login from './LoginNew';
import basewebURL from '../basewebURL';
import ReCAPTCHA from 'react-google-recaptcha';
import axios from 'axios';
import Logo from './Logo';

//const override: CSSProperties = {
//  display: "block",
//  margin: "0 auto",
//  borderColor: "red",
//};


const override={}

const Register=()=>{


    const [loading, setLoading] = useState("notcreated");
    //const history = useNavigate(); 	
    let color="var(--themeColor);";
    const initialFormData = Object.freeze({
                username:'',
                usertype: '1',
	        usernamelength:8
        });

    const [formData, updateFormData] = useState(initialFormData);

    const [buttonStyle, setButtonStyle]= useState({
      color:'white',
      backgroundColor:'var(--themeColor)'	    

    });

    const handleChangeUserName = (event) => {
        
        updateFormData({
                        ...formData,
                        [event.target.name]: event.target.value.trim(),
                });



    }

    
    const handleChangeUserType = (event) => {

     updateFormData({
                        ...formData,
                        [event.target.name]: event.target.value.trim(),
                });

    }


    const handleSubmit=()=>{

       if(formData.username.length >100){ 	   
          alert("too lengthy email address!!");
       }


       if(formData.usertype===""){
         alert("Please select usertype");
       }

       if(userExists){
          alert("Try a different number");	   
       }

       if(!captchaResult){
        alert("Check the captcha");

       }

       if(formData.username.length <100 && !userExists && formData.usertype !=="" && captchaResult){
	   //formData['username']= formData.username;	 
           setLoading(loading=>"creating");
	     console.log("formData: ", formData);  
             createaccountwithmobileno({formData, setLoading});
       }
    }



    const [userExists, setUserExists] = useState(false);
      
       useEffect(()=>{
          let username = "+91"+formData.username;	   
          checkuserexist({setUserExists,username });

       },[formData.username]);
       

    //let classRank=["+91","+353","+49"]
    //<OptionField handleChange={handleChange}  label="+91" name="countrycode"  options={classRank}/>
    const [login, setLogin] = useState(false);
    const [loggedIn, setLoggedIn] = useState(false);

    const handleRedirectLogin=()=>{     	    
     //history.push(`/dashboard/general/`);
     setLogin(true);

    }

    const [captchaResult, setCaptchaResult] = useState();

    const onChangeCaptchaHandler=(value)=>{

    //console.log('Captcha value:', value);
    

    fetch(`${basewebURL}/api/verifycaptcha/`, {
         method: 'POST',
         body: JSON.stringify({ 'captcha_value': value }),
         headers: { 'Content-Type': 'application/json' }
       })
        .then(res => res.json())
        .then(data => {
          //console.log("captcha value: ",data.captcha.success)
          setCaptchaResult(data.captcha.success)
        }) 


    }


    const TnSHandler=()=>{

      window.open("https://diracai.com/terms-conditions/", "_blank");

    }


    const privacyHandler=()=>{

      window.open("https://diracai.com/privacy-policy/", "_blank");

    }


   console.log("formData", formData);



return (

<div className={classes.registerParent}>


  { !login &&  
  <LoginHeader/>
  }


     { loading==="creating" &&  
          <div className={classes.registerDiv}>
	       <div className={classes.titleDiv}> <h2>Creating ... </h2> </div>
	       <div style={{margin:'auto'}}>
                   <FadeLoader color={color} loading={true} css={override} size={50}   />
	       </div>
          </div>
    }



   { loading ==="created" && !login &&

      <div className={classes.registerDiv}>

           <div className={classes.titleDiv}> <h2><BsCheckLg style={{color:"green"}}/> Account created successfully! </h2> </div>


            <div className={classes.submitButtonDiv}>

                <button type="button" onClick={handleRedirectLogin} className={classes.sendOTPButton} style={buttonStyle}> <b>Proceed to Login</b>  </button>

            </div>



      </div>

   }


   { login &&

     <Login setLoggedIn={setLoggedIn} loadedUsername={formData.username}/>

   }





  { loading==="notcreated" && 
  <div className={classes.registerDiv}>


    <div className={classes.titleDiv}> <h2 >Create an account</h2> </div>

    <div className={classes.switchMethodDiv}>  </div>

    <div className={classes.phoneNumberDiv}>
      <div className={classes.phonetitle}>Enter your email </div>

      <div className={classes.enterPhoneDiv}>

            


           <input
             type="text"
             onChange={handleChangeUserName}
             name="username"
             placeholder="e.g. john.1990@gmail.com"
             className={classes.usernameInput}
          />



      </div>

      <div className={classes.phonetnc}>
		 <span> By continuing, you agree to our  
		                  <span style={{color:"var(--themeColor)", cursor: "pointer"}} onClick={TnSHandler}> Terms of Service </span>  
		             and  <span style={{color:"var(--themeColor)", cursor: "pointer"}} onClick={privacyHandler}> Privacy Policy </span>
		  </span>
      </div>	
    </div>

    <div className={classes.switchMethodDiv} style={{color:"red"}}> {userExists? "user with this number already exists": ""} </div>		  

    <div className={classes.usertypeDiv}> 
       {/*		  
        <div className={classes.chooseUserTypeTitle}> Choose your role  </div>
        
        <div className={classes.userTypeOptions}>
	   <div className={classes.userTypeOptionsInner}>

             <span><input type="radio" value="1" name="usertype" className={classes.radioButton} onChange={handleChangeUserType}/> 
	         Teacher
	     </span>
             <span><input type="radio" value="2" name="usertype" className={classes.radioButton} onChange={handleChangeUserType}/> 
	        Student
	     </span>
             		  
             <span><input type="radio" value="3" name="usertype" className={classes.radioButton} onChange={handleChangeUserType}/> 
	        Owner/Manager
	     </span>
	    

           </div>
	</div> 
       */}

    </div>

    <div className={classes.submitButtonDiv}>
      <ReCAPTCHA
          sitekey="6LcGJiMlAAAAAGVV09GzZwEBf2SIu4nDFslO2Wn7"
          onChange={onChangeCaptchaHandler}
        />
    </div>



    <div className={classes.submitButtonDiv}>

      <button type="button" onClick={handleSubmit} className={classes.sendOTPButton} style={buttonStyle}> <b>Create</b>  </button>

    </div>



  </div>


  }



</div>

);

}

export default Register;
