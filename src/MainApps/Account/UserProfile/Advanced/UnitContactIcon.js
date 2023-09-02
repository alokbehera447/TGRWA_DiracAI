import React from 'react';
import classes from './UnitAboutIcon.module.css';

import {MdContactMail} from 'react-icons/md';


const UnitAboutIcon=()=>{



return (

<div className={classes.unitAboutIcon}>

   <div> <MdContactMail className={classes.aboutIcon}/> <i>ADDRESSES</i> </div>
  
  <button className={classes.editButtonAbout}>edit </button>
</div>
);


}
export default UnitAboutIcon;
