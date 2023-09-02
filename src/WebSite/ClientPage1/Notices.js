import {useEffect, useState, useRef} from 'react';
import classes from './Notices.module.css';

import {BsSearch} from 'react-icons/bs';


import OneNotice from './OneNotice';


const Notices =(props)=>{

   const isMounted = useRef(false);

   useEffect(() => {
    isMounted.current = true;
    props.passMountInfo(true);


    return () => {
            isMounted.current = false
            props.passMountInfo(false);
    }
   }, [props]);




   return <div className={classes.notices}>

           

            <div className={classes.searchbar}> 
		<BsSearch className={classes.serchIcon}/>
                 <input className={classes.searchInput} placeholder="  search..."/>                    
	    </div>


            No Notices available!


         </div>


}

export default Notices;
