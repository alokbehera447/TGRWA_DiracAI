
import classes from './NotificationContainer.module.css';
import OutsideAlerter from "../UserHead/OutsideAlerter";


const NotificationContainer=(props)=>{

return (

   <OutsideAlerter setDropDown={props.setDropDown}>

    <div className={classes.notificationContainer}>

       <div className={classes.oneNotification} style={{color:'grey'}}> There are no new notifications </div>


    </div>

   </OutsideAlerter>
	
);

}

export default NotificationContainer;
