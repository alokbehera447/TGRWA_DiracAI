import React,{useState, useEffect} from "react";
import classes from "./EduDegreeForm.module.css";
import {AiFillCloseCircle} from "react-icons/ai";
import logoImage from '../../../../../CommonApps/BWlogo.JPG'
import {OptionFieldSubmitValue,OptionFieldSecondaryObjs, ParagraphField,TextInput} from './FormInputObjects';
import {getdegreenames, getinstitutenames, getuser, createedudegree} from '../../../../../CommonApps/AllAPICalls.js';
import {institutesearchgeneral} from '../../../../../CommonApps/AllAPICalls.js';
import {OptionField, DateField, SearchAndInsert} from '../../../../../CommonApps/FormInputObjects';

import Logo from '../../../../../CommonApps/Logo';





//import FadeLoader from "react-spinners/FadeLoader";
//import { css } from "@emotion/react";


/*const override = css`
  display: block;
  margin: 0 auto;
  border-color: red;
`;*/



const CreateCourseForm=(props)=>{


//const [loading, setLoading] = useState(true);
//const [color, setColor] = useState(" var(--themeColor)");

   const [data, setData] = useState({});

   const [degreeNames, getDegreeNames] = useState([{"id": 99999999,"name": "Unable to fetch ticket category"}]);

   const [instituteNames, getInstituteNames] = useState([{"id": 99999999,"name": "Unable to fetch ticket category"}]);

   const [selectedBoardName, setSelectedBoardName] = useState("");

   const [subjectsObject,setSubjectsObject] = useState([{name:null}]);

   const [formSubmitted,setFormSubmitted] = useState(false);


   const [searchedInstitutes, getSearchedInstitutes] = useState(null)
   const [searchInstString, setSearchInstString] =  useState("Inst")
   const [pageNo , setPageNo] = useState(1);



   useEffect(() =>{
     getdegreenames({getDegreeNames});
   },[])


   useEffect(() =>{
    getinstitutenames({getInstituteNames});
   },[])


   useEffect(()=>{
      institutesearchgeneral({pageNo,searchInstString, getSearchedInstitutes});
   },[searchInstString]);




   useEffect(()=>{
     getuser({setData});
   },[]);



    console.log("searchedInstitutes: ", searchedInstitutes);



const initialFormData = Object.freeze({
        
        institute: "",
        degreename: null,
        startDate: null,
        endDate: null,
	instituteid:""

        });



const [formData, updateFormData] = useState(initialFormData);

const handleChange1 = (e) => {

	//setClassId(classId=>e.target.value);
        updateFormData({
                        ...formData,
                        [e.target.name]: e.target.value.trim()
                });
        };







const handleSubmit = (e) => {
	  e.preventDefault();
	  //setShowForm(false);
	   
          if(formData.degreename===null){
		  alert('please enter degree name');
		  return null;
	  }

          if(formData.institute===null){
                  alert('please enter name of the institute');
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

         createedudegree({formData, data});
	 //alert("Succssfully submitted");
	 //window.location.reload(true);
	 //alert("Successfully submitted");
	 // setShowForm(true);

         props.onPress();

         //setFormSubmitted(!formSubmitted);


	 //return new Promise(resolve => {
         //    setTimeout(() => {
         //        resolve();
         //    }, 2000);
         //});
	
	
	};

 
      const handleChange=(e)=>{

  
         console.log("name---: ", e.target.value);
         updateFormData({
                        ...formData,
                        [e.target.name]: e.target.value.trim()
                });

         setSearchInstString(searchInstString=>e.target.value.trim())

      }	

       //[e.target.displayname]: e.target.value.trim()


	console.log("formData: ", formData);

        console.log("searchInstString: ", searchInstString);




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
           <Logo/>
           <div className={classes.formTitleDiv}><i>  Add a degree </i></div>
       </div>



       <OptionField handleChange={handleChange1}  label="Degree" name="degreename"  options={degreeNames}/>

       {/*		   
       <OptionField handleChange={handleChange1}  label="Institute" name="institute"  options={instituteNames}/>
        */}




       <SearchAndInsert handleChange={handleChange} 
	                label="Institute" 
	                name="institute"
	                searchedObjects={searchedInstitutes}
	                formData={formData}
	                updateFormData={updateFormData}
	                setSearchInstString={setSearchInstString}
		        />



        {/*
        <input
              type="text"
              onChange={handleChange}
              name="institute"
              className={classes.input_field}
              placeholder="-"
              defaultValue="iit"
            />
         */}

         {/*
         <select name="institute"  onChange={handleChange}  mode="multiple">

          <option value="categoryDefault" disabled>
            "hello"
          </option>

          { instituteNames.map((option,index)=>{

                return <option key={index} value={option.id}> {option.name}  </option>

                }

          )}

        </select>
        */}
















       <div className={classes.dateFields}>      
         <DateField handleChange={handleChange1} label="Start date" name="startDate" placeholder="Enter degree start date"   />
         <div style={{width: "70px"}}> </div>
         <DateField handleChange={handleChange1} label="End date" name="endDate" placeholder="Enter degree end date"   />
       </div>




       <div className={classes.submitButtonDiv}>
       
           <button type="submit"  className= {classes.submit_button} ><b>Create </b> </button>

       </div>




  </form>

   }


</div>	
);

}


export default CreateCourseForm;
