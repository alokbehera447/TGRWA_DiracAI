import {useEffect, useState, useRef} from 'react';




const Project=(props)=>{
    const isMounted = useRef(false);

   useEffect(() => {
    isMounted.current = true;
    props.passMountInfo(true);


    return () => {
            isMounted.current = false
            props.passMountInfo(false);
    }
   }, [props]);


return <div>
   
   Posession		

  </div>

}

export default Project;
