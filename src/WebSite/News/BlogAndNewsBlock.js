import classes from "./BlogAndNewsBlock.module.css";
import bookAppointment from "./bookAppointment.jpg";
import bn1 from "./bn1.jpg";
import bn2 from "./bn2.jpg";
import bn3 from "./bn3.jpg";
import bn4 from "./bn4.jpg";


function BlogAndNewsBlock() {
  return (
    <div className={classes.blogAndNewsContainer}>
      <div className={classes.latest}>
        <div className={classes.latestTitle}>News</div>
        <div className={classes.latestsubTitle}>Latest News</div>
      </div>

      <div className={classes.newsContainer}>

        <div className={classes.singleContainer}>
          {/* <div className={classes.newsImage}></div> */}
          <img
            className={classes.newsImage}
            src={bn1}
            alt="logo"
          ></img>

          <div className={classes.newsTitle}>Builder, two former panchayat officials arrested</div>

          <div className={classes.newsDesc}>
          The special investigation team of the crime branch, probing the irregularities in the construction of four apartment complexes in Kochi in violation of the norms of Coastal Regulation Zone (CRZ), arrested a builder and two former panchayat officials Tuesday under graft charges
          </div>

          <div className={classes.readMoreBtn}>
            <div className={classes.readMoreTitle}>Read More...</div>
          </div>
        </div>

        <div className={classes.singleContainer}>
          <img
            className={classes.newsImage}
            src={bn2}
            alt="logo"
          ></img>

          <div className={classes.newsTitle}>Cabinet nod to apartment Bill:Chief minister Naveen
        </div>

          <div className={classes.newsDesc}>
          The cabinet gave its nod to the apartment bill to make the laws governing housing projects comply with the Real Estate (Regulation and Development) Act, 2016, a senior government official said. According to the bill, associations of allottees of housing projects.
          </div>

          <div className={classes.readMoreBtn}>
            <div className={classes.readMoreTitle}>Read More...</div>
          </div>
        </div>

        <div className={classes.singleContainer}>
          <img
            className={classes.newsImage}
            src={bn3}
            alt="logo"
          ></img>

          <div className={classes.newsTitle}>Odisha notifies Apartment Ownership and Management</div>

          <div className={classes.newsDesc}>
          he state government had informed the HC that the bill had been sent to the parliamentary affairs department for placing it in the next cabinet meeting. The two-judge bench of Chief Justice S Muralidhar and Justice M S Raman had said, “It is expected that the bill will be placed
          </div>

          <div className={classes.readMoreBtn}>
            <div className={classes.readMoreTitle}>Read More...</div>
          </div>
        </div>

        <div className={classes.singleContainer}>
          <img
            className={classes.newsImage}
            src={bn4}
            alt="logo"
          ></img>

          <div className={classes.newsTitle}>Odisha govt introduces new law for apartment ownership</div>

          <div className={classes.newsDesc}>
          In order to speed up the home-buying process and safeguard customers from potential abuses, among other things, the government has decided to form a committee to work on a model buyer agreement, a top government official said on Tuesday, according to a PTI news report.
          </div>

          <div className={classes.readMoreBtn}>
            <div className={classes.readMoreTitle}>Read More...</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default BlogAndNewsBlock;
