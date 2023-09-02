import classes from "./SingleBlog.module.css"
import bn1 from "./bn1.jpg";



function SingleBlog(props){




   const redirectHandler=()=>{


      window.open(props.link,"_blank");

   }






    return(

        <div className={classes.singleContainer}>
          {/* <div className={classes.newsImage}></div> */}
          <img
            className={classes.newsImage}
            src={props.image}
            alt="logo"
          ></img>

          <div className={classes.newsTitle}>{props.title}</div>

          <div className={classes.newsDesc}>
          
	    {props.text}
	  </div>


          <button className={classes.readMoreBtn} type="button" onClick={redirectHandler}>
            <div className={classes.readMoreTitle}>Read More...</div>
          </button>
        </div>
    );
}
export default SingleBlog;
