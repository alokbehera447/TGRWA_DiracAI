import React from 'react';
import classes from './UnitAboutIcon.module.css';

//import {MdContactMail} from 'react-icons/md';

import {BsTrophyFill} from 'react-icons/bs';

const UnitAboutIcon=()=>{



return (

<div className={classes.unitAboutIcon}>

   <div> <BsTrophyFill className={classes.aboutIcon}/> <i>SKILLS AND ACHIEVEMENTS</i> </div>
  
  <button className={classes.editButtonAbout}>edit </button>
</div>
);


}
export default UnitAboutIcon;
