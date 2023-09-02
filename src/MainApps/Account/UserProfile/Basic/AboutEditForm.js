import React,{useState,useEffect} from "react";
import classes from "./AboutEditForm.module.css";
import {AiFillCloseCircle} from "react-icons/ai";
import logoImage from '../../../../CommonApps/BWlogo.JPG'
import {getuser,putuser, putuserprofile} from '../../../../CommonApps/AllAPICalls';



const AboutEditForm=(props)=>{



const [data, setData ] = useState({});



useEffect(() =>{
   getuser({setData});
  },[]);



//console.log("userData: ", data);


const initialFormData = Object.freeze({
	        usertitle: data.usertitle,
                firstname: data.firstname,
	        lastname:data.lastname,
	        email: data.email,
	        gender:data.gender,
	        position:data.position,
	        dateofbirth:data.dateofbirth,
	        institute: data.institute,
	        city: data.city,
	        state: data.state,
	        country: data.country,
        });



const [formData, updateFormData] = useState(initialFormData)

const handleChange = (e) => {
                updateFormData({
                        ...formData,
                        [e.target.name]: e.target.value.trim(),
                });
        };






const handleSubmit = (e) => {
		e.preventDefault();

	        //putuser({data,formData});
               

                putuserprofile({data, formData});

                props.userDataUpdated(true);
	        props.onPress();
	};





return(

<div className={classes.aboutEditFormDivParent}>

  <form className={classes.aboutEditForm} onSubmit={handleSubmit}>

     <div className={classes.closeButtonDiv}>
        <button onClick={props.onPress} className={classes.closeFormButton}> <AiFillCloseCircle className={classes.closeButtonIcon}/> </button>
     </div>	


     <div className={classes.logoAndTitleContainer}>
	  <img  className={classes.bwLogo} src={logoImage} alt='edr Logo' />
           <div className={classes.titleDiv}><i>  Edit profile : About </i></div>
     </div>






	  <div className={classes.position_div}>
               <div className={classes.name_txt}>Title</div>
               <select name="usertitle"  onChange={handleChange} type="text" className={classes.genpos_field} defaultValue={"titleDefault"}>
                   <option value="titleDefault" disabled>Choose your title</option>
                   <option value="1">Mr</option>
                   <option value="2">Ms</option>
                   <option value="3">Dr</option>
	           <option value="">No title</option>
               </select>
        </div>









     <div className={classes.name_div}>
	  <div className={classes.name_txt}>Firstname</div>
	  <div className={classes.name_inputDiv} >
	    <input
              type="text"
              onChange={handleChange}
              name="firstname"
              className={classes.firstname_field}
              placeholder="firstname"
	      defaultValue={data.firstname}
            />
         </div>
     </div>


     <div className={classes.name_div}>
	<div className={classes.name_txt}>Lastname</div>
	<div className={classes.name_inputDiv} >
           <input
              type="text"
              onChange={handleChange}
              name="lastname"
              className={classes.lastname_field}
              placeholder="lastname"
	      defaultValue={data.lastname}
           />
       </div>
     </div>


    <div className={classes.genpos_div}>	

      <div className={classes.gender_div}>	
	<div className={classes.name_txt}>Gender</div>
        <select name="gender"  onChange={handleChange} type="text" className={classes.genpos_field} defaultValue={"genderDefault"}>
	  <option value="genderDefault" disabled>Choose gender</option>
          <option value="Male">Male</option>
          <option value="Female">Female</option>
        </select>
      </div>


      <div className={classes.position_div}>	
	<div className={classes.name_txt}>Position</div>
        <select name="position"  onChange={handleChange} type="text" className={classes.genpos_field} defaultValue={"dobDefault"}>
	  <option value="dobDefault" disabled>Choose your position</option>
	  <option value="11th">11th</option>
          <option value="12th">12th</option>
          <option value="BSc">BSc</option>
	  <option value="BTech">BTech</option>
	  <option value="MSc">MSc</option>
	  <option value="MTech">MTech</option>
	  <option value="PhD">PhD</option>
        </select>
      </div>

    </div>
 


     {/*
     <div className={classes.dob_div}>
	<div className={classes.dob_txt}>Dates of birth</div>
	<div className={classes.dob_innerDiv}>
	  <div className={classes.dob_innerDiv2}>
	    <input
             type="date"
             onChange={handleChange}
             name="dateofbirth"
             className={classes.dateofbirth_field}
             placeholder="date of birth"

            />
	  </div>
        </div>

     </div>
    */}

      <div className={classes.name_div}>
          <div className={classes.name_txt}>Email</div>
          <div className={classes.name_inputDiv} >
            <input
              type="text"
              onChange={handleChange}
              name="email"
              className={classes.firstname_field}
              placeholder="e.g. abcd@gmail.com"
              defaultValue={data.email}
            />
         </div>
     </div>



















     <div className={classes.name_div}>
          <div className={classes.name_txt}>Institute Name</div>
          <div className={classes.name_inputDiv} >
            <input
              type="text"
              onChange={handleChange}
              name="institute"
              className={classes.firstname_field}
              placeholder="institute name"
              defaultValue={data.institute}
            />
         </div>
     </div>


     <div className={classes.name_div}>
          <div className={classes.name_txt}>City</div>
          <div className={classes.name_inputDiv} >
            <input
              type="text"
              onChange={handleChange}
              name="city"
              className={classes.firstname_field}
              placeholder="e.g. New Delhi "
              defaultValue={data.city}
            />
         </div>
     </div>



     <div className={classes.name_div}>
          <div className={classes.name_txt}>State</div>
          <div className={classes.name_inputDiv} >
            <input
              type="text"
              onChange={handleChange}
              name="state"
              className={classes.firstname_field}
              placeholder="e.g. Delhi"
              defaultValue={data.state}
            />
         </div>
     </div>



    <div className={classes.name_div}>
          <div className={classes.name_txt}>City</div>
          <div className={classes.name_inputDiv} >
            <input
              type="text"
              onChange={handleChange}
              name="country"
              className={classes.firstname_field}
              placeholder="e.g. India"
              defaultValue={data.country}
            />
         </div>
     </div>

















     <div className={classes.submitButtonDiv}>
          <button type="submit"  className= {classes.submit_button} ><b>Save </b> </button>

     </div>


  </form>

</div>	
);

}


export default AboutEditForm;
