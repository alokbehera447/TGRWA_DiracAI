import {useState} from 'react';
import classes from './DropDownOne.module.css';
import OutsideAlerter from './OutsideAlerter';
import {BsChevronDown} from 'react-icons/bs';
import { Route, Switch, useHistory } from "react-router-dom";



const DropDownOne=(props)=>{


    const history = useHistory();

    const [showDropDownTwo, setShowDropDownTwo] = useState(false);

    const showDropDownHandler=()=>{
       setShowDropDownTwo(true);
    }


    const noticesHandler=()=>{

       history.push('/resident/notices');

    }



    const RulesAndRegulationsHandler=()=>{
     
       history.push('/resident/memberregistration');

    }

    const BlogsHandler=()=>{

      history.push('/resident/blogs');	    

    }



   const ProjectsHandler=()=>{
    history.push('/resident/lifecycle/projects');

   }


   const DoctorsHandler=()=>{
   history.push('/resident/health/doctors');

   }


   const BloodDonorsHandler=()=>{
   history.push('/resident/health/blooddonors');

   }



   const SaleDeedHandler=()=>{
    history.push('/resident/lifecycle/saledeed');

   }

  const PossessionHandler=()=>{

   history.push('/resident/lifecycle/possession');
  }

  const AssociationHandler=()=>{
   history.push('/resident/lifecycle/association');


  }

  const MaintenanceHandler=()=>{

    history.push('/resident/lifecycle/maintenance');

  }	


  const GalleryHandler=()=>{



  }


  const RentSaleHandler=()=>{

  }















   return    <OutsideAlerter setDropDown={props.setShowDropDownOne}>
		<div className={classes.dropdownOne}>
                       <div className={classes.dropdownOneDiv}>
                          <button type="button" className={classes.dropDownTwoButton} onClick={noticesHandler}> 
		                    Notices 
		          </button>
                       </div>
                       <div className={classes.dropdownOneDiv}>
                          <button type="button" className={classes.dropDownTwoButton} onClick={RulesAndRegulationsHandler}> 
		                   Member Registration 
		          </button>

                       </div>

                       <div className={classes.dropdownOneDiv}>
                          <button type="button" className={classes.dropDownTwoButton} onClick={GalleryHandler}>
                                   Gallery  
                          </button>

                       </div>


                       <div className={classes.dropdownOneDiv}>
                          <button type="button" className={classes.dropDownTwoButton} onClick={RentSaleHandler}>
                                Rent/Sale            
                          </button>
                       </div>






                       <div className={classes.dropdownOneDiv3}>
                         <button type="button" onClick={showDropDownHandler} className={classes.dropDownTwoButton}> 
		              <span>Health Resources </span>
		              <BsChevronDown size={15} style={{marginLeft:"5px"}}/>
		         </button>
                            <div className={classes.dropdownTwoDiv}>
                                 <button type="button" className={classes.dropDownTwoButton} onClick={DoctorsHandler}> Doctors </button>
                                 <button type="button" className={classes.dropDownTwoButton} onClick={BloodDonorsHandler}> Blood Donors </button>
		                 {/*
                                 <button type="button" className={classes.dropDownTwoButton} onClick={SaleDeedHandler}> Sale Deed </button>
                                 <button type="button" className={classes.dropDownTwoButton} onClick={PossessionHandler}> Possession </button>
                                 <button type="button" className={classes.dropDownTwoButton} onClick={AssociationHandler}> Association </button>
                                 <button type="button" className={classes.dropDownTwoButton} onClick={MaintenanceHandler}> Maintenance </button>
				 */}
                            </div>
                       </div>
                       <div className={classes.dropdownOneDiv}>
                          <button type="button" className={classes.dropDownTwoButton} onClick={BlogsHandler}> 
		                 Blogs
		          </button>
                       </div>
                  </div>
		 </OutsideAlerter>


}

export default DropDownOne;

