import classes from "./OneNotice.module.css";

const OneNotice = () => {
  return (
    <div className={classes.oneNotice}>
      
      <div className={classes.noticeBg}>
        <div className={classes.noticeNumber}>1</div>
      </div>

      <div className={classes.contentContainer}>
        <div className={classes.titleDiv}> RERA rules ammended 2022 </div>

        <div className={classes.contentDiv}>
          {" "}
          RERA new regulations 2022 also mandate the distribution of
          registration fees, municipal taxes, water and energy costs,
          maintenance fees, ground rent, and other fees as specified in the
          agreement. The builder is responsible for all outgoings such as water
          and electricity until possession is handed over to the buyers.{" "}
        </div>
      </div>

    </div>
  );
};

export default OneNotice;

