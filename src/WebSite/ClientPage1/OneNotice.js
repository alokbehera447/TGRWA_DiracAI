import classes from "./OneNotice.module.css";

import { BsFilePdf } from "react-icons/bs";


const OneNotice = (props) => {





   const openNoticeFile=()=>{


    window.open(props.notice.noticefile,"__blank");	   
    	   

   }



  return (
    <div className={classes.oneNotice}>
     


     {/*	  
      <div className={classes.noticeBg}>
        <div className={classes.noticeNumber}>Notice ID: TGRWA-0001</div>
      </div>
     */}

      <div className={classes.contentContainer}>
           <div className={classes.titleDiv}> NoticeID: 
         	  <span style={{color:"#094fb5"}}> {props.notice.globalNoticeID}:</span> 
	          <span style={{marginLeft:"10px"}}>    {props.notice.noticeTitle} </span>
	   </div>

        <div className={classes.contentDiv}>
          {" "}
          {props.notice.noticeText}
	</div>


        <button type="button" className={classes.viewFileButton} onClick={openNoticeFile}>

	   <BsFilePdf  style={{color:"red", marginRight:"10px"}}/> View File 
        </button>

      </div>

    </div>
  );
};

export default OneNotice;

