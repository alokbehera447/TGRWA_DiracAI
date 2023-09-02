import React,{useState} from 'react';
import { Link } from 'react-router-dom';
import {BsBoxArrowUpRight,BsUpload} from 'react-icons/bs';
import classes from './UnitBarFirstName.module.css';
import basewebURL from "../../../../basewebURL"



import {uploadofficeid,uploadgovtid1,uploadgovtid2,uploaddobcert} from '../../../../CommonApps/AllAPICalls.js';


const UnitBarIDDoc=(props)=>{



const [selectedFile, setSelectedFile] = useState(null);




let imageurl=props.data;

  /*	
  if (window.location.host === 'localhost:3000'){
      if(props.data===null){
         imageurl=null;
      } else{	  
      imageurl=basewebURL+props.data;
      }	      
     }

  if (window.location.host === '127.0.0.1:8000'){
      if(props.data===null){
         imageurl=null;
      } else{ 

      imageurl=basewebURL+props.data;
      }      
     }

  if (window.location.host === 'edresearch.co.in'){
      imageurl=props.data;
     }



  if (window.location.host === 'webapp.diracai.com'){
      imageurl=props.data;
     }
   */




  const handleChange =(e)=>{

    if(e.target && e.target.files[0]){

           //console.log("image: ", [e.target.name]);

            if(e.target.name === 'iddocfile' ){


                  setSelectedFile({
                        image: e.target.files
                   });

            }

       }

  }

   const handleSubmit=(e)=>{
    e.preventDefault();
 
    let imageformData = new FormData();

    if(props.idtype==="officeid"){
       imageformData.append('officeId_doc', selectedFile.image[0]);

       //console.log("imageformData: ", selectedFile.image[0]);
       uploadofficeid({imageformData});
    }

    if(props.idtype==="govtid1"){
       imageformData.append('govtId1_doc', selectedFile.image[0]);
        uploadgovtid1({imageformData});
	//console.log("govtId1:",selectedFile.image[0]);
    } 


    if(props.idtype==="dobdoc"){
       imageformData.append('dobCert_doc', selectedFile.image[0]);
       uploaddobcert({imageformData});
    } 



     window.location.reload(false);

    }





return (

<div className={classes.unitBarFirstName}>


    <div className={classes.firstNameTitle}> {props.docType}</div>

    <div className={classes.firstName}>  
      
        {/*
	<button className={classes.uploadButton_iddoc} onClick><BsUpload/></button>
         */}

         <form className={classes.imageUpload} onSubmit={handleSubmit}>

              <input
                    type="file"
                    onChange={handleChange}
                    name="iddocfile"
                    accept="*"
                    className={classes.image_field}
              />



              { selectedFile !==null &&
              <button type="submit"  className= {classes.submit_button} ><b>Upload </b> </button>
              }

        </form>







   
	<span style={{color: "green"}}>



        <Link to={{pathname: `${imageurl}`}}  target="_blank">
            {imageurl !==null && "Uploaded"}
	    {imageurl === null && <span style={{color: "red"}}>Not Available </span>}

	</Link>

    </span></div>



</div>
);


}
export default UnitBarIDDoc;


//<BsBoxArrowUpRight className={classes.openNewTabL}/>
