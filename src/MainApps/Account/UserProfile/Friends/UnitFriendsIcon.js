import React,{useState} from 'react';
import classes from './UnitFriendsIcon.module.css';
import {FaUsers} from 'react-icons/fa';
import AddContactForm from './Forms/AddContactForm';


const UnitFriendsIcon=(props)=>{


const [contactAddForm,showContactAddForm]=useState(false);




const contactAddFormHandler =()=>{


showContactAddForm(true);

}

const closeContactFormHandler=()=>{

showContactAddForm(false);

}









return (

<div className={classes.unitAboutIcon}>


	


   <div className={classes.FriendsIconDiv}> </div>
  
	<button onClick={contactAddFormHandler} className={classes.editButtonAbout} type='button'>+add new contact </button>


	{contactAddForm && <AddContactForm onPress={closeContactFormHandler} userData={props.userData}/>}   


</div>
);


}
export default UnitFriendsIcon;
