import {useState} from 'react';
import classes from './QuickMeetingPage.module.css';
import {AiFillCloseCircle} from 'react-icons/ai';

import {meetingbasewebURL} from '../../basewebURL';


const QuickMeetingPage=(props)=>{

    let meetingLink=meetingbasewebURL+'/video/'+props.meetingRoomName

   const startMeetingHandler=()=>{
    
       window.open(meetingLink, "_blank")

    }

    const [linkCopied, setLinkCopied]=useState(false);	
    const delay = ms => new Promise(res => setTimeout(res, ms));

    const copyMeetingLinkHandler=async()=>{

	navigator.clipboard.writeText(meetingLink);    
        setLinkCopied(true);
	await delay(3000);
	setLinkCopied(false);    

    }



return (

<div className={classes.quickMeetingPage}>

    <div className={classes.meetingInfoPage}>
           <div className={classes.closeButtonDiv}>
	     
             <button onClick={props.onPress} className={classes.closeFormButton}> <AiFillCloseCircle className={classes.closeButtonIcon}/> </button>
             




	     </div>

           <div className={classes.shareMeetingTitle}>
	     <h2> Share meeting link with participants </h2>
           </div>
          

           <div> Meeting link:
	         { !linkCopied &&
	         <button type="button" onClick={copyMeetingLinkHandler} className={classes.copyButton}> copy link</button>
		 }
                 { linkCopied &&
                 <button type="button" className={classes.copyButton} > copied</button>
                 }

	   </div>

	   <button type="button" className={classes.meetingLink} onClick={startMeetingHandler}>
              {meetingLink} 
	     
           </button>


           <div> 
              <button type="button" className={classes.startMeetingNowButton} onClick={startMeetingHandler}> Start meeting now </button>

           </div>	

    </div>

</div>

);

}

export default QuickMeetingPage;
