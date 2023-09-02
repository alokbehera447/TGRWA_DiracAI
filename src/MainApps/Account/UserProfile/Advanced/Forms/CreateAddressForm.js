import React,{useState, useEffect} from "react";
import classes from "./EduDegreeForm.module.css";
import {AiFillCloseCircle} from "react-icons/ai";
import logoImage from '../../../../../CommonApps/BWlogo.JPG'
import {OptionFieldAdr,OptionFieldSubmitValue,OptionFieldSecondaryObjs, ParagraphField,TextInput, DateField} from './FormInputObjects';
import { createachievement,createaddress} from '../../../../../CommonApps/AllAPICalls.js';
//import FadeLoader from "react-spinners/FadeLoader";
//import { css } from "@emotion/react";


  /*const override = css`
  display: block;
  margin: 0 auto;
  border-color: red;
  `;*/



const CreateAddressForm=(props)=>{


   //const [loading, setLoading] = useState(true);
   //const [color, setColor] = useState(" var(--themeColor)");

    const [data, setData] = useState({});


    const [formSubmitted,setFormSubmitted] = useState(false);




    const initialFormData = Object.freeze({
               userId: props.userData.id,
               careof: "",
               houseno: "",
               streetno: "",
               district: "",
               pincode: "",
               city: "",
               state: "",
               country: "",
               addressType: null


        });



    const [formData, updateFormData] = useState(initialFormData);

    const handleChange = (e) => {

        updateFormData({
                        ...formData,
                        [e.target.name]: e.target.value.trim(),
                });
        };







    const handleSubmit = (e) => {
	  e.preventDefault();
	  //setShowForm(false);
	   
          if(formData.name===""){
		  alert('please enter a title');
		  return null;
	  }



	  if(formData.startDate===null){
                  alert('please enter start date');
                  return null;
          }

          if(formData.endDate===null){
                  alert('please enter end date');
                  return null;
          }



         //setTimeout(() => {console.log('Hello, World!')}, 5000);
         // setShowForm(false);

         //console.log("formData: ", formData);

         createaddress({formData});
	 //alert("Succssfully submitted");
	 //window.location.reload(true);
	 //alert("Successfully submitted");
	 // setShowForm(true);

         props.onPress();


         //window.location.reload(false);

         //setFormSubmitted(!formSubmitted);


	 //return new Promise(resolve => {
         //    setTimeout(() => {
         //        resolve();
         //    }, 2000);
         //});
	
	
	};



  let addressType_ = [{"id": 1,"name": "present"},{"id": 2,"name": "permanent"}]




return(

<div className={classes.createTicketFormDivParent}>

   {/*!showForm &&  
	   <div className={classes.createTicketFormLoading}>

	   <FadeLoader color={color} loading={loading} css={""} size={50}  />
	    
	   <div className={classes.submittingDiv}> Creating . . . </div>
           </div>
   */}


   { 	
  <form className={classes.createTicketForm} onSubmit={handleSubmit}>

       {/*form close button below*/}	
       <div className={classes.closeButtonDiv}>
          <button onClick={props.onPress} className={classes.closeFormButton}> <AiFillCloseCircle className={classes.closeButtonIcon}/> </button>
       </div>	

 
       {/*logo and field title container below*/}
       <div className={classes.logoAndTitleContainer}>
	  <img  className={classes.bwLogo} src={logoImage} alt='edr Logo' />
           <div className={classes.formTitleDiv}><i style={{fontSize:"30px"}}>  Add a new address </i></div>
       </div>



        <OptionFieldAdr handleChange={handleChange}  label="Choose a addres type" name="addressType"  options={addressType_}/>


        <TextInput handleChange={handleChange} label="C/o " name="careof" placeholder="Optional" />


        <TextInput handleChange={handleChange} label="House number" name="houseno" placeholder=" Enter house no." />


        <TextInput handleChange={handleChange} label="Street No/Place name/Village" name="streetno" placeholder=" Enter street no." />


        <TextInput handleChange={handleChange} label="District name" name="district" placeholder=" Enter district name" />


        <TextInput handleChange={handleChange} label="State" name="state" placeholder=" Enter state name" />


	<TextInput handleChange={handleChange} label="Country" name="country" placeholder=" Enter country name" />	   

        <TextInput handleChange={handleChange} label="Pincode" name="pincode" placeholder=" Enter pincode" />







       <div className={classes.submitButtonDiv}>
       
           <button type="submit"  className= {classes.submit_button} ><b>Create </b> </button>

       </div>




  </form>

   }


</div>	
);

}


export default CreateAddressForm;
