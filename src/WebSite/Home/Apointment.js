import classes from "./Apointment.module.css";
import bookAppointment from "./bookAppointment.jpg";
import img from "./appointment.jpg"

function Appointment() {
  return (
    <div className={classes.bookAppointment}>
     <img className={classes.bookpic} src={img} alt="logo"></img>
      <div className={classes.bookDetail}>
        <div className={classes.bookDetailContainer}>
          <div className={classes.bookTitle}>Book Appointment</div>
          <div className={classes.booksubTitle}>
            We take pride in serving you. Welcome, Dear Resident!
          </div>

          <div className={classes.bookaptBtn}>
            <div className={classes.bookaptText}>Book Appointment</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Appointment;
