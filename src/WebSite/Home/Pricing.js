import classes from "./Pricing.module.css";
import bookAppointment from "./bookAppointment.jpg";

import { FaRupeeSign } from "react-icons/fa";

function Pricing() {
  return (
    <div className={classes.PricingParent}>
      <div className={classes.subscriptionDetails}>
        <div className={classes.PlanTextTitle}>Our Plans</div>
        <div className={classes.PlanTextsubTitle}>What Our Clients Says..</div>

        <div className={classes.planContainer}>
          <div className={classes.basicPlan}>
            <div className={classes.basicPlanContent}>
              <div className={classes.pic}>
                <FaRupeeSign className={classes.rupees_icon} />
              </div>

              <div className={classes.planTitle}>Basic Plan</div>

              <div className={classes.aboutPrice}>
                <div className={classes.amount}>$49</div>
                <div className={classes.amountMonth}>/Monthly</div>
              </div>

              <div className={classes.horizontalLine}></div>

              <div className={classes.features}>
                <div className={classes.checkIcon}></div>
                <div className={classes.textplanDetails}>
                  Free Amazon Prime,Disny Plus Hotstar
                </div>
              </div>
              <div className={classes.features}>
                <div className={classes.checkIcon}></div>
                <div className={classes.textplanDetails}>
                  Free Amazon Prime,Disny Plus Hotstar
                </div>
              </div>
              <div className={classes.features}>
                <div className={classes.checkIcon}></div>
                <div className={classes.textplanDetails}>
                  Free Amazon Prime,Disny Plus Hotstar
                </div>
              </div>

              <div className={classes.basicPlanBtn}>Choose Plan</div>
            </div>
          </div>

          <div className={classes.standardPlan}>
            <div className={classes.basicPlanContent}>
              <div className={classes.pic}>
                <FaRupeeSign className={classes.rupees_icon} />
              </div>

              <div className={classes.planTitle}>Standard Plan</div>

              <div className={classes.aboutPrice}>
                <div className={classes.amount}>$49</div>
                <div className={classes.amountMonth}>/Monthly</div>
              </div>

              <div className={classes.horizontalLine}></div>

              <div className={classes.features}>
                <div className={classes.checkIcon}></div>
                <div className={classes.textplanDetails}>
                  Free Amazon Prime,Disny Plus Hotstar
                </div>
              </div>
              <div className={classes.features}>
                <div className={classes.checkIcon}></div>
                <div className={classes.textplanDetails}>
                  Free Amazon Prime,Disny Plus Hotstar
                </div>
              </div>
              <div className={classes.features}>
                <div className={classes.checkIcon}></div>
                <div className={classes.textplanDetails}>
                  Free Amazon Prime,Disny Plus Hotstar
                </div>
              </div>

              <div className={classes.basicPlanBtn}>Choose Plan</div>
            </div>
          </div>

          <div className={classes.unlimitedPlan}>
            <div className={classes.basicPlanContent}>
              <div className={classes.pic}>
                <FaRupeeSign className={classes.rupees_icon} />
              </div>

              <div className={classes.planTitle}>Unlimited Plan</div>

              <div className={classes.aboutPrice}>
                <div className={classes.amount}>$49</div>
                <div className={classes.amountMonth}>/Monthly</div>
              </div>

              <div className={classes.horizontalLine}></div>

              <div className={classes.features}>
                <div className={classes.checkIcon}></div>
                <div className={classes.textplanDetails}>
                  Free Amazon Prime,Disny Plus Hotstar
                </div>
              </div>
              <div className={classes.features}>
                <div className={classes.checkIcon}></div>
                <div className={classes.textplanDetails}>
                  Free Amazon Prime,Disny Plus Hotstar
                </div>
              </div>
              <div className={classes.features}>
                <div className={classes.checkIcon}></div>
                <div className={classes.textplanDetails}>
                  Free Amazon Prime,Disny Plus Hotstar
                </div>
              </div>

              <div className={classes.basicPlanBtn}>Choose Plan</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Pricing;
