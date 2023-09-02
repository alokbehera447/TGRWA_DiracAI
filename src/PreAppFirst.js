import PreAppSecond from './PreAppSecond';
import {Route,Switch} from 'react-router-dom'
import Register from './CommonApps/Register';
import Website from './WebSite/Website';


import ViewAllRegistrants from './WebSite/OnlineRegistration/ViewAllRegistrants';


const PreAppFirst=()=>{



return (

<div>

<Switch>

   <Route exact path='/createaccount/' >
        <Register/>
   </Route>


   <Route exact path='/tgrwamembers123/' >
        <ViewAllRegistrants/>
   </Route>



   <Route   path='/' >
        <Website/>
   </Route>

   
   <Route  path='/app/' >
        <PreAppSecond/>
   </Route>	



</Switch>




</div>
);
}

export default PreAppFirst;
