import React,{useState, useEffect, CSSProperties} from "react";
import classes from './OnlineRegistrationHome.module.css';
import Logo from './LogoTGRWA.png';
import {createnewregistration} from '../../CommonApps/AllAPICalls';
import axios from 'axios';

import basewebURL from '../../basewebURL';


import defaultphoto from './default.png';

import FadeLoader from "react-spinners/BeatLoader";
const override: CSSProperties = {
  display: "block",
  margin: "0 auto",
  borderColor: "red",
  fontSize:"10px",
};





const OnlineRegistrationHome=()=>{

   let color="var(--themeColor)";

   const [ createState, setCreateState] = useState("notCreating");

   const [selectedPhotoFile, setSelectedPhotoFile] = useState(null);

   const [selectedSigFile, setSelectedSigFile] = useState(null);

   const initialFormData = Object.freeze({
        name: "",
        address: "",
        mobileno:"",
	email:"",
        photoFile: null,
	signatureFile: null
        });


    const [formData, updateFormData] = useState(initialFormData);


     
  const handleInputChange = (e) => {
    const { name, value, type, files } = e.target;

    // If the input is a file input, set photoFile to the selected file
    const newValue = type === 'file' ? files[0] : value;

    updateFormData({
            ...formData,
            [name]: newValue,
          });
    };



      const handleChange=(e)=>{

             updateFormData({
                        ...formData,
                        [e.target.name]: e.target.value,
                });

       }


      const handleChangeImage=(e)=>{


       if(e.target && e.target.files[0]){

                if(e.target.name === 'photoFile' ){
                  setSelectedPhotoFile({
                        image: e.target.files
                  });
                 }

                if(e.target.name === 'signatureFile' ){
                   setSelectedSigFile({
                        image: e.target.files
                  });
                 }




       }

    }






   console.log("formData: ", formData);



   const handleSubmit= async (e)=>{
      e.preventDefault();

          if(formData.name===""){
                  alert('please enter name');
                  return null;
          }


	  if(formData.mobileno===""){
                  alert('please enter mobile no');
                  return null;
          }


         if(formData.email===""){
                  alert('please enter email');
                  return null;
          }


          if(formData.address===""){
                  alert('please enter Flat No');
                  return null;
          }

         
        if(!selectedSigFile){
            alert('please upload photo of your signature');
                  return null;
         }





      let submitData = new FormData();
        submitData.append('name',formData.name);
	submitData.append('mobileno', formData.mobileno);
	submitData.append('email',formData.email);
        submitData.append('address', formData.address);
	//submitData.append('photoFile', formData.photoFile);
	if(selectedPhotoFile){
          submitData.append('photoFile', selectedPhotoFile.image[0]);
	}
	
	  
        submitData.append('signatureFile', selectedSigFile.image[0]);
	setCreateState("Creating");


	 console.log("submitData: ", submitData);
	 let postURL = `${basewebURL}/api/onlineregistration/create/`;

         console.log("postURL: ", postURL);
	 const response = await axios.post(postURL, submitData);
	 setCreateState("Success");
 	 //createnewregistration({submitData, setCreateState, config});
   }


    const showMemberPageHandler=()=>{

    window.open("https://webapp.diracai.com/tgrwamembers", "_blank");

    }

    const clearCacheHandler=()=>{

      window.location.reload();

    }





return <div className={classes.onlineRegistrationHome}>

      <div className={classes.title}>
          <span>Online TGRWA membership Registration</span>
      </div>
 

      <div className={classes.FormMainDiv}>


      <div className={classes.FormMainDiv_inner}>

           <div className={classes.titleBlock}>
                
                <div className={classes.logo}>  
		  <img src={Logo} className={classes.imageLogo}/> 
		</div>

		<div className={classes.InstTitle}>
		     <div className={classes.mainTitle}><b> {"Trident Galaxy Residents' Welfare Association"}</b> </div>
		     <div className={classes.tagTitle}> Regd. No. : 2586-62/2019-2020 </div>
		</div>
           </div>

           <div className={classes.descriptionRole}> Membership Form </div>		

	   <div className={classes.textContent}> 
		I wish to be a member of the Trident Galaxy Residents' Welfare Association. Please enroll me as a member of Trident Galaxy Residents' Welfare Association with Regd. no. 2586-62/2019-2020. I am willing to contribute Rs. 500/- as one-time membership fee. I promise to abide by the laws of association 
	   </div>	

   		
           <form className={classes.dataSubmissionForm} onSubmit={handleSubmit} >

	       <div className={classes.firstTextDiv}>
		  <div className={classes.fieldTitleDiv}>Name:  </div>
                  <input
                     type="text"
                     onChange={handleChange}
                     name="name"
                     className={classes.input_field}
                     />
               </div>
           
	        	
               <div className={classes.firstTextDiv}>
                  <div className={classes.fieldTitleDiv}>Photo(max. 1mb):  </div>
                  <input
                     type="file"
                     onChange={handleChangeImage}
                     name="photoFile"
                     className={classes.input_field}
                     />

               </div>

	       <div className={classes.firstTextDiv} style={{fontSize:"10px",color:"red", marginLeft:"120px"}}>
	        Photo is optional but strongly recommended.
	       </div>	

	         { selectedPhotoFile &&
                  <img alt="not fount" width={"250px"} src={URL.createObjectURL(selectedPhotoFile.image[0])} className={classes.photoPreView} />
                 }





               <div className={classes.firstTextDiv}>
                  <div className={classes.fieldTitleDiv}>MobileNo:  </div>
                  <input
                     type="text"
                     onChange={handleChange}
                     name="mobileno"
                     className={classes.input_field}
                     />
               </div>


              <div className={classes.firstTextDiv}>
                  <div className={classes.fieldTitleDiv}>Email:  </div>
                  <input
                     type="text"
                     onChange={handleChange}
                     name="email"
                     className={classes.input_field}
                     />
               </div>


              <div className={classes.firstTextDiv}>
                  <div className={classes.fieldTitleDiv}>Address:  </div>
                  <input
                     type="text"
                     onChange={handleChange}
                     name="address"
                     className={classes.input_field}
	             placeholder="e.g. Flat No: H210"
                     />
                   
               </div>

                <div className={classes.firstTextDiv}>
		  <div className={classes.addressDefault}>
		     <div> Trident Galaxy Apartments, K-3,  Kalinga Nagar</div>
	             <div> Ghatikia, Bhubaneswar -751003 </div>
	             <div> Odisha, India </div>
                  </div>
		</div>


               <div className={classes.firstTextDiv}>
                  <div className={classes.fieldTitleDiv}>Signature (max. 1mb):  </div>
                  <input
                     type="file"
                     onChange={handleChangeImage}
                     name="signatureFile"
                     className={classes.input_field}
                     />

               </div>



                 { selectedSigFile &&
                  <img alt="not fount" width={"250px"} src={URL.createObjectURL(selectedSigFile.image[0])} className={classes.photoPreView} />
                 }


             <div>
                 { createState === "Creating" &&
                   <FadeLoader color={color}  css={""} size={50}  />
                 }
	     </div>	

	     <div className={classes.submitButtonDiv}>
                   { createState ==="notCreating" &&
                   <button type="submit"  className= {classes.submit_button} ><b> Submit </b> </button>
		   }
	           { createState ==="Creating" &&
		   <button type="submit"  className= {classes.submit_button} disabled={true}><b> Submitting... </b> </button>
                   }
              



             </div>


                  { createState ==="Success" &&

                       <div className={classes.successMessage}> You have successfully submitted membership data.  Your membership data has been stored digitally at TGRWA's private repository. Please contact TGRWA to get copy of your certificate</div>
                   }



           </form>

           { createState ==="Success" &&
                   <button type="submit"  className= {classes.submit_button_success} onClick={clearCacheHandler}><b> Submit another one </b> </button>
                   }


    </div>		

    </div>

</div>


}

export default OnlineRegistrationHome;
