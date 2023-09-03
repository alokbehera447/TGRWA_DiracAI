import {useEffect, useRef, useState} from 'react';
import classes from "./Header.module.css";
import {FaReact} from 'react-icons/fa';
import DropDownOne from './DropDownOne';
import {BsChevronDown} from 'react-icons/bs';
import Logo from "./tgrwalogo.png";
import BimalenduName from "./BimalenduName.png";
import HeaderAddressBar from './HeaderAddressBar';



const  Header=(props)=> {

   const [showDropDownOne, setShowDropDownOne] = useState(false);
   const showDropDownOneHandler=()=>{
     setShowDropDownOne(true);
   }

   let activeColor="black";
   let inActiveColor="var(--themeColor)";



   const [homeButtonStyle, setHomeButtonStyle] = useState({color:inActiveColor, underlineColor:"white" });
   const [aboutButtonStyle, setAboutButtonStyle] = useState({color:inActiveColor, underlineColor:"white" })
   const [newsButtonStyle, setNewsButtonStyle] = useState({color:inActiveColor, underlineColor:"white" })
   const [contactUsButtonStyle, setContactButtonStyle] = useState({color:inActiveColor, underlineColor:"white" })
   const [homeBuyerButtonStyle, setHomeBuyerButtonStyle] = useState({color:inActiveColor, underlineColor:"white" });

   useEffect(()=>{

     props.homeMounted && setHomeButtonStyle({color:"var(--themeColor)", underlineColor:"var(--themeColor)" });
     !props.homeMounted && setHomeButtonStyle({color:"black", underlineColor:"white"});
     
   },[props.homeMounted]);


   useEffect(()=>{

     props.aboutMounted && setAboutButtonStyle({color:"var(--themeColor)", underlineColor:"var(--themeColor)"});
     !props.aboutMounted && setAboutButtonStyle({color:"black", underlineColor:"white"});


   },[props.aboutMounted]);



   useEffect(()=>{

     props.newsMounted && setNewsButtonStyle({color:"var(--themeColor)", underlineColor:"var(--themeColor)"});
     !props.newsMounted && setNewsButtonStyle({color:"black", underlineColor:"white"});

   },[props.newsMounted]);


   useEffect(()=>{

     props.contactUsMounted && setContactButtonStyle({color:"var(--themeColor)", underlineColor:"var(--themeColor)"});
     !props.contactUsMounted && setContactButtonStyle({color:"black", underlineColor:"white"});

   },[props.contactUsMounted]);



   useEffect(()=>{

     props.homeBuyerMounted && setHomeBuyerButtonStyle({color:"var(--themeColor)", underlineColor:"var(--themeColor)"});
     !props.homeBuyerMounted && setHomeBuyerButtonStyle({color:"black", underlineColor:"white"});

   },[props.homeBuyerMounted]);

   console.log("props.homeMounted", props.homeMounted);



    return (
    <div className={classes.parentFooter}>
         
         
        {/* top Navigation bar */}
        <div className={classes.topNavigationBar}>
          <div className={classes.nFirstCotainer}>
            {/* <div className={classes.logo}>  */}
	       <img className={classes.logo} src={Logo} />

	      {/*
               <div className={classes.csslogo}> 
	             <span>T</span>
	       </div>
               */}
	       <div className={classes.Name}> TGRWA </div>
        
      
	    {/* </div> */}
            {/*
           
	      <img src={BimalenduName}/>
	    </div>
	    */}
          </div>
          
          <div className={classes.navigationMenu}>

            <div className={classes.headerButtonDiv}>
               <button type="button" className={classes.headerButton} onClick={props.homeHandler} style={homeButtonStyle}>
                  <div className={classes.HomeText}>Home</div>
               </button>

	       <div className={classes.underlineDiv} style={{backgroundColor:homeButtonStyle.underlineColor}}> </div>
            </div>

            <div className={classes.headerButtonDiv}>
               <button type="button" className={classes.headerButton} onClick={props.aboutHandler} style={aboutButtonStyle}>
                  <div className={classes.headerButtonText}>About</div>
               </button>
               <div className={classes.underlineDiv} style={{backgroundColor:aboutButtonStyle.underlineColor}}> </div>

            </div>


	    <div className={classes.headerButtonDiv}>
              <button type="button" className={classes.headerButton} onClick={props.newsHandler} style={newsButtonStyle}>
                  <div className={classes.headerButtonText}>News</div>
              </button>
	      <div className={classes.underlineDiv} style={{backgroundColor:newsButtonStyle.underlineColor}}> </div>

            </div>



	    <div className={classes.headerButtonDiv}>
              <button type="button" className={classes.headerButton} onClick={showDropDownOneHandler} style={homeBuyerButtonStyle}>
                  <div className={classes.headerButtonText}><span>Resident</span> <BsChevronDown size={15} style={{marginLeft:"5px"}}/></div>
              </button>
                  { showDropDownOne && 
	                         <DropDownOne setShowDropDownOne={setShowDropDownOne} /> 
		  }

	       <div className={classes.underlineDiv} style={{backgroundColor:homeBuyerButtonStyle.underlineColor}}> </div>
            </div>


            <div className={classes.headerButtonDiv}>
              <button type="button" className={classes.headerButton} onClick={props.contactUsHandler} style={contactUsButtonStyle}>
                 <div className={classes.headerButtonText}>Contact us</div>
              </button>

	      <div className={classes.underlineDiv} style={{backgroundColor:contactUsButtonStyle.underlineColor}}> </div>
            </div>

          </div>
	  
        </div>
    
    </div>
    
    
    );
}

export default Header;
