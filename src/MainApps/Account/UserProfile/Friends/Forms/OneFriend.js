import React,{useState} from 'react';
import classes from './OneFriend.module.css';
import {putaddcontact} from '../../../../../CommonApps/AllAPICalls.js';




const OneFriend=(props)=>{

  //console.log('contact: ',props.contact);
  //console.log('contact: ', props.contact);

  let imageurl = `${props.contact.profile_image}`


  const [contactAdded, setContactAdded] = useState(false);


 const addContactHandler=()=>{

  let contactId	= props.contact.id; 
  setContactAdded(true);
  putaddcontact({contactId});
  //window.location.reload(false);
 }

 let result = props.userData.contacts.map(a => a.id);


 //console.log("result: ", result);	


return (


<div className={classes.oneFriend}>
  {
  <img src={imageurl}  className={classes.friendImage} />	
  }
  <div className={classes.InfoBox}> 
	<div className={classes.fullName}> <i>{props.contact.firstname +" "}{ props.contact.lastname}</i></div>
        { !result.includes(props.contact.id) && props.userData.id !== props.contact.id &&
	<button type='button' className={classes.addContactButton} onClick={addContactHandler}>Add contact  </button>
        }

        { result.includes(props.contact.id) && props.userData.id !== props.contact.id &&
        <button type='button' className={classes.addContactButton} onClick={addContactHandler} style={{background: "green"}} disabled>Added  </button>
        }


  </div>

</div>
);


}

export default OneFriend;
