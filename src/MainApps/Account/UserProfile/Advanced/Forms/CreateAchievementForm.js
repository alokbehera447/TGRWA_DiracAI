import React,{useState, useEffect} from "react";
import classes from "./EduDegreeForm.module.css";
import {AiFillCloseCircle} from "react-icons/ai";
import logoImage from '../../../../../CommonApps/BWlogo.JPG'
import {OptionField,OptionFieldSubmitValue,OptionFieldSecondaryObjs, ParagraphField,TextInput, DateField} from './FormInputObjects';
import { createachievement} from '../../../../../CommonApps/AllAPICalls.js';
//import FadeLoader from "react-spinners/FadeLoader";
//import { css } from "@emotion/react";


  /*const override = css`
  display: block;
  margin: 0 auto;
  border-color: red;
  `;*/



const CreateAchievementForm=(props)=>{


   //const [loading, setLoading] = useState(true);
   //const [color, setColor] = useState(" var(--themeColor)");

   const [data, setData] = useState({});


   const [formSubmitted,setFormSubmitted] = useState(false);




   const initialFormData = Object.freeze({
       name: "",
       description: "",
       startDate: null,
       endDate: null,
       userId: props.userData.id

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


         createachievement({formData});
	 //alert("Succssfully submitted");
	 //window.location.reload(true);
	 //alert("Successfully submitted");
	 // setShowForm(true);

         props.onPress();


         window.location.reload(false);

         //setFormSubmitted(!formSubmitted);


	 //return new Promise(resolve => {
         //    setTimeout(() => {
         //        resolve();
         //    }, 2000);
         //});
	
	
	};








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
           <div className={classes.formTitleDiv}><i style={{fontSize:"30px"}}>  Add an achievement or skill </i></div>
       </div>






        <TextInput handleChange={handleChange} label="Title " name="name" placeholder="e.g. Ten Years experience in IIT JEE coaching" />


        <ParagraphField handleChange={handleChange} label="Description" name="description" placeholder="optional" />


        <DateField handleChange={handleChange} label="Start date" name="startDate" placeholder="Enter degree start date"   />

        <DateField handleChange={handleChange} label="End date" name="endDate" placeholder="Enter degree end date"   />





       <div className={classes.submitButtonDiv}>
       
           <button type="submit"  className= {classes.submit_button} ><b>Create </b> </button>

       </div>




  </form>

   }


</div>	
);

}


export default CreateAchievementForm;
