import React,{useState} from 'react';
import classes from './UnitAboutIcon.module.css';

import {MdContactMail} from 'react-icons/md';


import CreateAddressForm from './Forms/CreateAddressForm';


const UnitAboutIcon=(props)=>{



const [showAddAddressForm, setShowAddAddressForm] = useState(false);



const showFormHandler=()=>{

setShowAddAddressForm(true);
}


const closeFormHandler=()=>{
setShowAddAddressForm(false);

}











return (

<div className={classes.unitAboutIcon}>

   <div> <MdContactMail className={classes.aboutIcon}/> <i>ADDRESSES</i> </div>
  
  <button className={classes.editButtonAbout} onClick={showFormHandler}>+Add </button>


	{showAddAddressForm && <CreateAddressForm onPress={closeFormHandler} userData={props.userData}/>}

</div>
);


}
export default UnitAboutIcon;
