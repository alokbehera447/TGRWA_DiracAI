import React,{useState,useEffect} from 'react';
import {Route,Switch} from 'react-router-dom';
import  './App.css';
import Header from './components/Header/Header';
import SideBarDashboard from './components/SideNavBar/SideBarDashboard';
import UserProfile from './MainApps/Account/UserProfile/UserProfile';
//Import Applications
import General from './MainApps/Dashboard/General/General';
import {getuser} from './CommonApps/AllAPICalls';





function App() {

    
    console.log(" Main App Page reredering-----------------");
    
    let sideBarBreakPoint='850px';
        
    const [rerender,setRerender] = useState(false);

    const rerenderHandler=()=>{setRerender(!rerender);}
   
    const [sideNavBarWidth, setWidth] = useState('var(--sideNavBarWidth)');

    const [contract,setContract] = useState(true);

    const expandHandler=()=>{

        //console.log("expand handler called");
        contract && setWidth('var(--sideNavBarWidthOnContract)');
        !contract && setWidth('var(--sideNavBarWidth)');
        setContract(!contract);

    }






   const [dashboardMounted, setDashboardMounted] = useState(false);
   const [contactsMounted, setContactsMounted] = useState(false);
   const [discussionMounted, setDiscussionMounted] = useState(false);	




    	
    
   

    
   const [userData,setData]=useState({
   "id": null,	   
   "dashboardcourses": [],
   "dashboard_courses":[],	   
   "usertype":1,
   "noticeids":[]	   
   });
   



     	
   useEffect(()=>{
	//console.log("useEffect-2");   
        getuser({setData});
    },[rerender])
  





  
  return (
    <div className="edrapp">

    
         <Header onPress={expandHandler}  
	       userData={userData} 
	       rerender={rerenderHandler}
	       /> 
  
         <SideBarDashboard sideNavBarWidth={sideNavBarWidth}
	              userData={userData}
	              setWidth={setWidth}
	              setContract={setContract}
	              homeMounted={dashboardMounted}
                      />
    
 
        <Switch>	        	
            <Route exact path='/app/account/userprofile' >
               <UserProfile sideNavBarWidth={sideNavBarWidth} 
	          userData={userData}
	          rerender={rerenderHandler}
	          />
            </Route>
 
            <Route  path='/app/dashboard/general' >
                   <General sideNavBarWidth={sideNavBarWidth} 
	              passMountInfo={setDashboardMounted} 
	              userData={userData}
	              rerender = {rerenderHandler}
	              />
            </Route>

    </Switch>	  

      
    </div>

  );

 

return (<div> </div>);


}

export default App;
