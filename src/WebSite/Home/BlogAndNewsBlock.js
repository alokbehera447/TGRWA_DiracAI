import { useEffect, useState } from "react";
import classes from "./BlogAndNewsBlock.module.css";
import SingleBlog from "./SingleBlog";
import axiosInstance from "../../axios";


function BlogAndNewsBlock() {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    let active = true;
    axiosInstance
      .get("blogs/")
      .then((res) => {
        if (!active) return;
        setBlogs(Array.isArray(res.data) ? res.data : []);
      })
      .catch(() => {
        if (!active) return;
        setBlogs([]);
      });

    return () => {
      active = false;
    };
  }, []);



  return (
    <div className={classes.blogAndNewsContainer}>
      <div className={classes.latest}>
        <div className={classes.latestTitle}>Blogs</div>
        <div className={classes.latestsubTitle}>Latest Blogs</div>
      </div>

      <div className={classes.newsContainer}>
        {blogs.slice(0, 4).map((b) => (
          <SingleBlog
            key={b.id || b.slug}
            title={b.title || ""}
            text={b.excerpt || ""}
            link={b.slug ? `/blog/${b.slug}` : "/blogs"}
            image={b.image || ""}
          />
        ))}
        {blogs.length === 0 ? <div>No posts yet.</div> : null}
      </div>
    </div>
  );
}

export default BlogAndNewsBlock;
