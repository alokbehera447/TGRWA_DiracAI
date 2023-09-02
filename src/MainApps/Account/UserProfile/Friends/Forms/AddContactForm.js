import React,{useState} from 'react';
import classes from './AddContactForm.module.css';
import {AiFillCloseCircle} from 'react-icons/ai';
import {BsSearch} from 'react-icons/bs'
import {getusersfromnames} from '../../../../../CommonApps/AllAPICalls.js';
import OneFriend from './OneFriend';



const AddContactForm=(props)=>{


const [searchUsers, getSearchUsers] = useState([])




const handleChange=(e)=>{

     let namestring = e.target.value;
     getusersfromnames({namestring, getSearchUsers});


}



const handleSubmit=()=>{





}

//console.log("searched Users: ", searchUsers);



return (

<div className={classes.addContactForm}>
 
   <form className={classes.aboutEditForm} onSubmit={handleSubmit}>	
      <div className={classes.closeButtonDiv}>
	  <div className={classes.titleSec}> <b>Add a new contact</b> </div>
          <button onClick={props.onPress} 
	          className={classes.closeFormButton}> 
	          <AiFillCloseCircle 
	              className={classes.closeButtonIcon}
	          /> 
	  </button>
      </div>


    <div className={classes.searchBarDiv}>

        <div className={classes.searchIconDiv}>

	    <BsSearch/>
	</div>
        <input
              type="text"
              onChange={handleChange}
              name="inputText"
              className={classes.input_field}
              placeholder="Search by first name"
              
            />


    </div>

   </form>



   <div className={classes.searchedUsersGrid}>

         { /*
              searchUsers.map((contact, index)=>{

                return <div className={classes.oneFriend} key={index}>


                       <div>


                     })
         */ }


              {
              searchUsers.map((contact, index)=>{

                         return <OneFriend key={index}
                         contact={contact}
		         userData={props.userData} 
                         />
                     })
                }





   </div>





</div>

);


}

export default AddContactForm;
