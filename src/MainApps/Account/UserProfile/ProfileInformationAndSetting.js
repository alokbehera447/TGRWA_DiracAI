import React,{useState} from 'react';
import classes from "./ProfileInformationAndSetting.module.css";
import UserProfileSwitchBar from './UserProfileSwitchBar';
import UserProfileContentBasic from './Basic/UserProfileContentBasic';
import UserProfileContentAdvanced from './Advanced/UserProfileContentAdvanced';
import UserProfileContentGrades from './Grades/UserProfileContentGrades';
import UserProfileContentFriends from './Friends/UserProfileContentFriends';


const ProfileInformationAndSetting=(props)=>{


const [basic,setBasic] = useState(true);
const [advanced,setAdvanced] = useState(false);
const [grades,setGrades] = useState(false);
const [friends, setFriends] = useState(false);



const [style,setStyle] = useState({ 
	     basic:  {color:"white",backgroundColor:"var(--themeColor)"},
             advanced:  {color:"var(--themeColor)",backgroundColor:"white"},
             grades:  {color:"var(--themeColor)",backgroundColor:"white"},
	     friends:  {color:"var(--themeColor)",backgroundColor:"white"},
             }
    );





const setAdvanceToTrue=()=>{

  setBasic(false);
  setGrades(false);	
  setFriends(false);	
  setAdvanced(true);

  setStyle({    basic:  {color:"var(--themeColor)",backgroundColor:"white"},
                advanced:  {color:"white",backgroundColor:"var(--themeColor)"},
                grades:  {color:"var(--themeColor)",backgroundColor:"white"},
	        friends:  {color:"var(--themeColor)",backgroundColor:"white"},
             });

  }


const setGradesToTrue=()=>{

  setBasic(false);
  setAdvanced(false);
  setFriends(false);	
  setGrades(true);
  setStyle({    basic:  {color:"var(--themeColor)",backgroundColor:"white"},
                grades:  {color:"white",backgroundColor:"var(--themeColor)"},
                advanced:  {color:"var(--themeColor)",backgroundColor:"white"},
	        friends:  {color:"var(--themeColor)",backgroundColor:"white"},
             });


  }	


const setBasicToTrue=()=>{

  setAdvanced(false);
  setGrades(false);
  setBasic(true);
  setFriends(false);	
  setStyle({    advanced:  {color:"var(--themeColor)",backgroundColor:"white"},
                basic:  {color:"white",backgroundColor:"var(--themeColor)"},
                grades:  {color:"var(--themeColor)",backgroundColor:"white"},
	        friends:  {color:"var(--themeColor)",backgroundColor:"white"},
             });




  }




const setFriendsToTrue=()=>{

  setAdvanced(false);
  setGrades(false);
  setBasic(false);
  setFriends(true);
  setStyle({    advanced:  {color:"var(--themeColor)",backgroundColor:"white"},
                basic:  {color:"var(--themeColor)",backgroundColor:"white"},
                grades:  {color:"var(--themeColor)",backgroundColor:"white"},
                friends:  {color:"white",backgroundColor:"var(--themeColor)"},
             });




  }














return (

<div className={classes.profileInformationAndSetting}>

    	
    <UserProfileSwitchBar onPressAdvanced = {setAdvanceToTrue} 
	                  onPressGrades   = {setGradesToTrue} 
	                  onPressBasic    = {setBasicToTrue}
	                  onPressFriends  = {setFriendsToTrue}
	                  style = {style}
                          />

   { basic  && <UserProfileContentBasic  data={props.data} userDataUpdated={props.userDataUpdated} /> }

   {/* advanced  && <UserProfileContentAdvanced  data={props.data} userDataUpdated={props.userDataUpdated} /> */}
 
   {/* grades && <UserProfileContentGrades/> */}	
   
    
   {/* friends && <UserProfileContentFriends userData={props.data}/>*/}


</div>
);

}


export default ProfileInformationAndSetting;
