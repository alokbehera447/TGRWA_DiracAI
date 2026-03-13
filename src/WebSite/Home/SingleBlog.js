import classes from "./SingleBlog.module.css"
import { useHistory } from "react-router-dom";



function SingleBlog(props){
   const history = useHistory();




   const redirectHandler=()=>{
      if (props.onClick) {
        props.onClick();
        return;
      }
      const link = props.link || "";
      if (link.startsWith("http://") || link.startsWith("https://")) {
        window.open(link, "_blank");
        return;
      }
      if (link) {
        history.push(link);
      }
   }






    return(

        <div className={classes.singleContainer}>
          {props.image ? (
            <img className={classes.newsImage} src={props.image} alt="" />
          ) : null}

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
