import React,{useState,useEffect} from 'react';
import App from './App';
import Login from './CommonApps/LoginNew';
import axiosInstance from './axios';




const PreAppSecond=()=>{

 const [loggedIn, setLoggedIn] = useState(false);

  	
  useEffect(() =>{

      axiosInstance.get().then((res) => {
                        setLoggedIn(loggedIn=>true);
                       // console.log(res.data);
                });

  },[]);
  
  
  if (!loggedIn){ return <Login setLoggedIn={setLoggedIn} loadedUsername="None"/>}
  


return (
        
<App/>
      
);

}

export default PreAppSecond;
