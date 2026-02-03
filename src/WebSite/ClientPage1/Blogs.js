import { useEffect, useRef, useState } from "react";
import { Route, Switch, useHistory, useParams, useRouteMatch } from "react-router-dom";
import axiosInstance from "../../axios";
import classes from "./Blogs.module.css";

import BlogAndNewsBlock from "./Blogs/BlogAndNewsBlock";

const Blogs = (props) => {
  const isMounted = useRef(false);
  const { path, url } = useRouteMatch();

  useEffect(() => {
    isMounted.current = true;
    props.passMountInfo(true);

    return () => {
      isMounted.current = false;
      props.passMountInfo(false);
    };
  }, [props]);

  return (
    <Switch>
      <Route exact path={path}>
        <div className={classes.blogs}>
          <BlogAndNewsBlock />
        </div>
      </Route>
      <Route path={`${path}/:slug`}>
        <BlogDetail baseUrl={url} />
      </Route>
    </Switch>
  );
};

export default Blogs;

const BlogDetail = ({ baseUrl }) => {
  const { slug } = useParams();
  const history = useHistory();
  const [blog, setBlog] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let active = true;
    setLoading(true);
    setBlog(null);
    axiosInstance
      .get(`blogs/${slug}/`)
      .then((res) => {
        if (!active) return;
        setBlog(res.data || null);
        setLoading(false);
      })
      .catch(() => {
        if (!active) return;
        setBlog(null);
        setLoading(false);
      });

    return () => {
      active = false;
    };
  }, [slug]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!blog) {
    return (
      <div>
        <button type="button" onClick={() => history.push(baseUrl || "/blogs")}>
          Back
        </button>
        <div>Not found.</div>
      </div>
    );
  }

  return (
    <div>
      <button type="button" onClick={() => history.push(baseUrl || "/blogs")}>
        Back
      </button>
      <div>{blog.title || ""}</div>
      <div>
        {(blog.author && blog.author.name) || ""} {blog.date || ""}
      </div>
      {blog.image ? <img src={blog.image} alt="" style={{ width: "100%", maxWidth: 900 }} /> : null}
      <div>{blog.content || ""}</div>
    </div>
  );
};
