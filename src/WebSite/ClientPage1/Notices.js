import {useState, useEffect, useRef} from 'react';
import classes from './Notices.module.css';

import {BsSearch} from 'react-icons/bs';

import {getalltgrwaNotice} from '../../CommonApps/AllAPICalls';


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



   const [allNotices, getData] = useState(null);


   const [pageNo, setPageNo] = useState(1);



   useEffect(()=>{

     getalltgrwaNotice({getData, pageNo});

   },[pageNo]);



   const nextPageHandler=()=>{

     allNotices.next !==null && setPageNo(pageNo=>pageNo+1);	   

   }


   const previousPageHandler=()=>{

   allNotices.previous !==null && setPageNo(pageNo=>pageNo-1);

   }	





   console.log("allNotices: ", allNotices)


   return <div className={classes.notices}>

           
            {/*
            <div className={classes.searchbar}> 
		<BsSearch className={classes.serchIcon}/>
                 <input className={classes.searchInput} placeholder="  search..."/>                    
	    </div>
            */}

           <div className={classes.noticeTopTitle}> Notices  </div>


           <div className={classes.noticeContainer}>   

              <div className={classes.pageInfoDiv}> Showing page 

	                  <button type="button" className={classes.nextPrevButton} onClick={previousPageHandler}> Previous </button>
	                  {pageNo} 
	                 <button type="button" className={classes.nextPrevButton} onClick={nextPageHandler}> Next </button>
                         of { allNotices !==null && allNotices.total_pages}

	     </div>


		{allNotices !==null && allNotices.results.map((notice, index)=>{

                    
		    return <OneNotice key={index}
			              notice={notice}
			              />	


		})

	     
		}	
           </div>


         </div>


}

export default Notices;
