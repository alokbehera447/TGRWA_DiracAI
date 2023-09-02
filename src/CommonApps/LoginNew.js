import React, { useState,CSSProperties, useRef } from 'react';
import axiosInstance from '../axios';
//import { Link } from 'react-router-dom';
//import classes from "./Login.module.css"
import classes from './Register.module.css';
import LoginHeader from "./LoginHeader";
//import LoginFooter from "./LoginFooter";
//import logoImage from './BWlogo.JPG'
import { useHistory } from "react-router-dom";
import {changepassword} from './AllAPICalls';
import FadeLoader from "react-spinners/FadeLoader";
import OTPinputUnit from './OTPinputUnit';

import Logo from './Logo';

//const override: CSSProperties = {
//  display: "block",
//  margin: "0 auto",
//  borderColor: "red",
//};

const override={}

const useFocus = () => {
    const htmlElRef = useRef(null)
    const setFocus = () => {htmlElRef.current &&  htmlElRef.current.focus()}
    return [ htmlElRef, setFocus ] 
}














const Login =(props)=> {


    const history = useHistory();

    let loadedUsername=String(props.loadedUsername);
    let phoneNum= loadedUsername;   
    const [UsernameValue, setUsernameValue] = useState(phoneNum);

    let color="var(--themeColor);";
    const initialFormData = Object.freeze({
	        username:loadedUsername,
		email: '',
		password: '',
	});

    const [formData, updateFormData] = useState(initialFormData);


    const [buttonStyle, setButtonStyle]= useState(
             {
               color:'white',
               backgroundColor:'var(--themeColor)'
             }
   
      );


    const [buttonStyleOTP, setButtonStyleOTP]= useState({ 
      color:'grey',
      backgroundColor:'lightgrey'

    });

    const [loginState, setLoginState] = useState("OTPnotrequested");

    const [inputRef1, setInputFocus1] = useFocus();
    const [inputRef2, setInputFocus2] = useFocus();
    const [inputRef3, setInputFocus3] = useFocus();
    const [inputRef4, setInputFocus4] = useFocus();
    const [inputRef5, setInputFocus5] = useFocus();	





    const handleChangeUserName = (event) => {
       setUsernameValue(event.target.value);

        updateFormData({
                        ...formData,
                        [event.target.name]: event.target.value.trim(),
                });


    }


    const handleSubmitOTP = (e) => {
		e.preventDefault();

               if( 
		  !(("first" in formData) && (formData.first !=="")) ||
                  !(("second" in formData) && (formData.second !=="") )||
		  !(("third" in formData) && (formData.third !==""))||
		  !(("fourth" in formData) && (formData.fourth !==""))||
		  !(("fifth" in formData) && (formData.fifth !==""))     

	         ){alert("fill all the boxes ");} 
                
 
		 formData["password"]= String(formData.first)+
		            String(formData.second)+String(formData.third)+String(formData.fourth)+String(formData.fifth);


		 axiosInstance.post(`token/`, {username: formData.username,password: "OLsbd!@#45"+formData.password,})
			.then((res) => {
				localStorage.setItem('access_token', res.data.access);
				localStorage.setItem('refresh_token', res.data.refresh);
				axiosInstance.defaults.headers['Authorization'] =
					'JWT ' + localStorage.getItem('access_token');
				props.setLoggedIn(true);
				let location_=window.location.href;
				if(location_.includes("createaccount")){
				  window.location.href="https://bimalendupradhan.com"	

				}
				
			});
	};   






    const handleSubmitGetOTP=(e)=>{
       e.preventDefault();
   //      if( !(formData.username.includes("+91")) && (formData.username.length !==10) ){
    //       alert("Enter a 10 digit number");
     //  }

      // if( (formData.username.includes("+91")) && (formData.username.length !==13) ){
      //     alert("Enter a 10 digit number");
      // }



      // if(!(formData.username.includes("+91"))){

      //   formData['username']="+91"+formData.username;

      // }


      // if(formData.username.length === 13 ){
          setLoginState(loginState=>"OTPsending");
          changepassword({formData, setLoginState});
       //}

    } 

    const handleChangeOTP=(e)=>{
     updateFormData({
                        ...formData,
                        [e.target.name]: e.target.value.trim(),
                });

     //setInputFocus();
     if(e.target.name==="first"){setInputFocus2()}
     if(e.target.name==="second"){setInputFocus3()}
     if(e.target.name==="third"){setInputFocus4()}
     if(e.target.name==="fourth"){setInputFocus5()}	   


     if(
         e.target.name==="fifth"
       ){

          setButtonStyleOTP({
            color:'white',
            backgroundColor:'var(--themeColor)'
           });
       }
    }



    const createAccountPageHandler=()=>{

      history.push('/createaccount');

    }


    const TnSHandler=()=>{

      window.open("https://diracai.com/terms-conditions/", "_blank");

    }


    const privacyHandler=()=>{

      window.open("https://diracai.com/privacy-policy/", "_blank");

    }











return (



<div className={classes.registerParent}>
  

   <LoginHeader/>


     { loginState==="OTPsending" &&
          <div className={classes.registerDiv}>
               <div className={classes.titleDiv}> <h2>Sending OTP ... </h2> </div>
               <div style={{margin:'auto'}}>
                   <FadeLoader color={color} loading={true} css={override} size={50}   />
               </div>
          </div>
    }






    
   { loginState ==="OTPnotrequested" && <>


     <div className={classes.registerDiv}>


      <div className={classes.titleDiv}> <Logo/> <h2 style={{marginLeft:"10px"}}> Login </h2> </div> 



      <div className={classes.phoneNumberDiv}>
         <div className={classes.phonetitle}>Enter email </div>

         <div className={classes.enterPhoneDiv}>


           <input
             type="text"
             onChange={handleChangeUserName}
             name="username"
             placeholder="e.g. jon.1988@gmail.com"
             className={classes.usernameInput}
             value={UsernameValue}	     
          />



       </div>

       <div className={classes.phonetnc}>
              <span> By continuing, you agree to our
                                  <span style={{color:"var(--themeColor)", cursor: "pointer"}} onClick={TnSHandler}> Terms of Service </span>
                             and  <span style={{color:"var(--themeColor)", cursor: "pointer"}} onClick={privacyHandler}> Privacy Policy </span>
              </span>
       </div>
     </div>

    <div className={classes.switchMethodDiv}>  </div>


     <div className={classes.submitButtonDiv}>

           <button type="button" onClick={handleSubmitGetOTP} className={classes.sendOTPButton} style={buttonStyle}> <b>Send OTP</b>  </button>

     </div>
     
     <button type="button" className={classes.linkToAccountCreation} onClick={createAccountPageHandler}>
      Don't have an account? Create one here 
     </button>	
     

		   



    </div>
    </>
    }



    { loginState==="OTPsent" && <>


       <div className={classes.registerDiv}>		    

       <div className={classes.titleDiv}> <Logo/>  <h2 style={{marginLeft:"10px"}}> Login </h2> </div>


 
       <div className={classes.phoneNumberDiv}>
           <div className={classes.phonetitle}>Enter OTP </div>

           <div className={classes.enterOTPDiv}>

           

	     <OTPinputUnit handleChangeOTP={handleChangeOTP} name="first" inputRef={inputRef1}/>	     
	     <OTPinputUnit handleChangeOTP={handleChangeOTP} name="second" inputRef={inputRef2}/>
	     <OTPinputUnit handleChangeOTP={handleChangeOTP} name="third" inputRef={inputRef3}/>	    
             <OTPinputUnit handleChangeOTP={handleChangeOTP} name="fourth" inputRef={inputRef4}/>
             <OTPinputUnit handleChangeOTP={handleChangeOTP} name="fifth" inputRef={inputRef5}/>
              












           </div>


         <div className={classes.phonetnc}>
	      <span> By continuing, you agree to our
                                  <span style={{color:"var(--themeColor)", cursor: "pointer"}} onClick={TnSHandler}> Terms of Service </span>
                             and  <span style={{color:"var(--themeColor)", cursor: "pointer"}} onClick={privacyHandler}> Privacy Policy </span>
              </span>

	 </div>


       </div>



       <div className={classes.switchMethodDiv}>  </div>
          <div className={classes.submitButtonDiv}>
             <button type="button" onClick={handleSubmitOTP} className={classes.sendOTPButton} style={buttonStyleOTP}> <b>Submit OTP</b>  </button>
          </div>
       </div>


    </>

   }


</div>

);






}

export default Login;


