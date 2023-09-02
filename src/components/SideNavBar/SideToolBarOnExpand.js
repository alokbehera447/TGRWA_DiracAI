import React,{useState,useEffect} from 'react';
import SideToolBarButton1 from './SideToolBarButton1';
import SideToolBarButton2 from './SideToolBarButton2';
import SideToolBarButton3 from './SideToolBarButton3';
import SideToolBarButton4 from './SideToolBarButton4';
import classes from './SideToolBarOnExpand.module.css';

import {BsFillArrowRightSquareFill} from 'react-icons/bs';






const SideToolBarOnExpand = (props)=>{


  const [toolBarWidth,setSideToolBarWith]=useState(props.toolBarWidth);

  const [contract, setContract] = useState(false);



  useEffect(() => {
     setSideToolBarWith(props.toolBarWidth);

     setContract(contract=>!contract);
	
  }, [props.toolBarWidth]);




   console.log("contract: ".contract);



return (


<div className={classes.parentDiv} 
	style={{width:toolBarWidth, backgroundColor: props.toolBarBkgColor }}
	>
  <div className={classes.sideToolBarDiv} 
       style={{width:toolBarWidth, backgroundColor: props.toolBarBkgColor }}
       >

    {/*	
    {contract && <SideToolBarButton1/>}

    {contract && <SideToolBarButton3/>}

    {contract && <SideToolBarButton4/>}

    {contract && <SideToolBarButton2/>}

    {!contract && <BsFillArrowRightSquareFill />}
    */}

 </div>
</div>







);

}

export default SideToolBarOnExpand;
