
import classes from './OneFriend.module.css';

import Bibhuti from './Bibhuti.jpeg';


const OneFriend=(props)=>{


//console.log('contact: ',props.contact);

//console.log('contact: ', props.contact.profile_image);


return (


<div className={classes.oneFriend}>
  {
  <img src={props.contact.profile_image}  className={classes.friendImage} />	
  }
  <div className={classes.InfoBox}> <i>{props.contact.firstname} {props.contact.lastname}</i> </div>

</div>
);


}

export default OneFriend;
