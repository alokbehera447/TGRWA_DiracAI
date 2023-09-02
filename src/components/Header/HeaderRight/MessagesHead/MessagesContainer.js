
import classes from './MessagesContainer.module.css';
import OutsideAlerter from "../UserHead/OutsideAlerter";


const MessagesContainer=(props)=>{

return (

   <OutsideAlerter setDropDown={props.setDropDown}>

    <div className={classes.notificationContainer}>

       <div className={classes.oneNotification} style={{color:'grey'}}> There are no new messages </div>


    </div>

   </OutsideAlerter>
	
);

}

export default MessagesContainer;
