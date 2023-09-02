import { useEffect, useState, useRef } from "react";
import classes from "./Blogs.module.css";

//import BlogAndNewsBlock from "./Blogs/BlogAndNewsBlock";
//import SingleBlog from "../Home/SingleBlog";

const Blogs = (props) => {
  const isMounted = useRef(false);

  useEffect(() => {
    isMounted.current = true;
    props.passMountInfo(true);

    return () => {
      isMounted.current = false;
      props.passMountInfo(false);
    };
  }, [props]);

  return (
    <div className={classes.blogs}>
    




   </div>
  );
};

export default Blogs;
