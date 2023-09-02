import React,{useState} from 'react';
import classes from './AllFriends.module.css';
import OneFriend from './OneFriend';
import {BsSearch} from 'react-icons/bs'

import {getusersfromnames} from '../../../../CommonApps/AllAPICalls.js';



const AllFriends=(props)=>{


  const [searchedUsers, getSearchedUsers] = useState(null);




return (

 <div className={classes.allFriends_parent}>

    {/*	
    <div className={classes.searchBar_contact}>
       <BsSearch className={classes.searchIcon}/>
    </div>
    */}

    <div className={classes.allFriends}>


          {  props.userData.id !==null && props.userData.contacts !==null && props.userData.contacts.map((contact, index)=>{

                         return <OneFriend key={index}
                         contact={contact}
		         userData={props.userData}
		         />
                     })
          }

   </div>


 </div>

);


}

export default AllFriends;
