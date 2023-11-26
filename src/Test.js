
import {  Routes, Route } from "react-router-dom" 


import Posts from './Posts';

import NewPost from './NewPost';
import Home from './Home';
import About from './About';

const Test=()=>{

return     <div>

	   <Routes>
                <Route path='/' element={<Home/>} />
                <Route path='about' element={<About/>} />
                <Route path='posts' element={<Posts/>}>
                    <Route path='new' element={<NewPost/>} /> {/*A nested route!*/}
                    <Route path=':postId' element={<div> postId </div>} /> {/*A nested route!*/}
                </Route>
            </Routes>
       

    </div>

}

export default Test;
