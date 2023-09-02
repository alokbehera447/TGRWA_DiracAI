import classes from './FormInputObjectsDurga.module.css';
import React,{useState} from 'react';
import Switch from "react-switch";




export const TextInput = (props)=>{

return <div className={classes.name_div}>
          <div className={classes.name_txt}>
		{props.requirement==="*" && <span style={{color:"red"}}> * </span>}
		{props.label}
	  </div>
	  <div className={classes.name_inputDiv} >	
            <input
              type="text"
              onChange={props.handleChange}
              name={props.name}
              className={classes.input_field}
              placeholder={props.placeholder}
              defaultValue={props.defaultValue}
            />
          </div>		
    </div>

}

// filesupload
export const FileUpload = (props)=>{

  return <div className={classes.file_div}>
            <div className={classes.file_txt}>
      {props.requirement==="*" && <span style={{color:"red"}}> * </span>}
      {props.label}
      </div>
      <div className={classes.name_inputDiv} >	
              <input
                type="file"
                onChange={props.handleChange}
                questionFiles={props.questionFiles}
                className={classes.file_upload}
              />
            </div>		
      </div>
  
  }





export const OptionField = (props)=>{


return <div className={classes.name_div}>

        <div className={classes.name_txt}> 
		{props.requirement==="*" && <span style={{color:"red"}}> * </span>}
		{props.label}
	</div>
 
        <div className={classes.name_inputDiv} >
        <select name={props.name}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
          <option value="categoryDefault" disabled > 
		{props.defaultValue} 
	 </option>

          
          { props.options.map((option,index)=>{

                return <option key={index} value={option.id}> {option.name}  </option>
 
                }

          )}

        </select>
      </div>		
 </div>


}





export const OptionFieldSubmitValue = (props)=>{


return <div className={classes.name_div}>

        <div className={classes.name_txt}>
		{props.requirement==="*" && <span style={{color:"red"}}> * </span>}
		{props.label}
		</div>
        <div className={classes.name_inputDiv} >

        <select name={props.name}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
          <option value="categoryDefault" disabled> --- </option>


          { props.options.map((option,index)=>{

                return <option key={index} value={option.name}> {option.name}  </option>

                }

          )}

        </select>
    </div>
 </div>


}

























export const OptionFieldSecondaryObjs = (props)=>{



return <div className={classes.name_div}>

        <div className={classes.name_txt}>
		{props.requirement==="*" && <span style={{color:"red"}}> * </span>}
		{props.label}
	</div>
        <div className={classes.name_inputDiv} >

        <select name={props.name}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
          <option value="categoryDefault" disabled> --- </option>


          { props.options.map((option,index)=>{

                return <option key={index} value={option.id}> {option}  </option>

                }

          )}

        </select>
    </div>
 </div>


}







export const ParagraphField = (props)=>{

return <div className={classes.name_div}>
          <div className={classes.name_txt}>{props.label}</div>
          <div className={classes.name_inputDiv} >
            <textarea
              type="text"
              onChange={props.handleChange}
              name={props.name}
              className={classes.input_field_paragraph}
              placeholder={props.placeholder}
              defaultValue={props.defaultValue}
            />
         </div>
    </div>

}



export const DateField = (props) =>{

return( 
	<div className={classes.name_div}>
        <div className={classes.name_txt}>
	   {props.requirement==="*" && <span style={{color:"red"}}> * </span>}
	   {props.label}
	</div>
	<div className={classes.name_inputDiv} >
          <input
             type="date"
             onChange={props.handleChange}
             name={props.name}
	     className={classes.input_field}
             placeholder={props.placeholder}
             style={{color: 'grey'}}
	     defaultValue={props.defaultValue}
          />
        </div>
     </div>

);


}










export const DayField = (props)=>{

   const [checked,setChecked]=useState(false);

   const handleChange=()=>{
     setChecked(!checked);
     props.setChecked(!checked);	  
   }	

   let hrOptions=["00","01","02","03","04","05","06","07","08","09","10","11","12"]
   let minOptions=["00","10","15","20","25","30","35","40","45","50","55","59"]
   let ampmOptions=["am","pm"]
   let classduration = ["00","10","15","20","25","30","35","40","45","50","55","59"]	

return <div className={classes.name_div}>

        <div className={classes.name_txt}>
		{props.label}
	</div>
        <div className={classes.name_inputDivDayOptions} >
        <select name={props.selectedhour}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
          <option value="categoryDefault" disabled >Hour</option>

          { hrOptions.map((option,index)=>{
                return <option key={index} value={option} disabled={!checked}> {option}  </option>
		      
                }

          )}

        </select>

       <select name={props.selectedminute}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
          <option value="categoryDefault" disabled > Minute</option>

          { minOptions.map((option,index)=>{

                return <option key={index} value={option} disabled={!checked}>{option}  </option>

                }

          )}

       </select>

       <select name={props.selectedampm}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
               <option value="categoryDefault" disabled>am or pm</option>
              { ampmOptions.map((option,index)=>{

                       return <option key={index} value={option} disabled={!checked}> {option}  </option>

                 }

             )}

       </select>


       {
       <select name={props.selectedduration}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
               <option value="categoryDefault" disabled>class duration</option>


              { classduration.map((option,index)=>{

                       return <option key={index} value={option} disabled={!checked}> {option}{" minutes"}  </option>

                 }

             )}

       </select>
       }


       <div className={classes.toggleSwitch}>
		{<Switch onChange={handleChange} checked={checked} />}
       </div>

    </div>
 </div>


}




export const TimeField = (props) =>{


   let hrOptions = ["00","01","02","03","04","05","06","07","08","09","10","11","12"]
   let minOptions = ["00","10","15","20","25","30","35","40","45","50","55","59"]	
   let ampmOptions = ["am","pm"]	


return(
        <div className={classes.name_div}>
        <div className={classes.name_txt}>
	   {props.requirement==="*" && <span style={{color:"red"}}> * </span>} 
	   {props.label}
	</div>
        <div className={classes.name_inputDivTimeField}>
       
        <select name={props.selectedhour}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
               <option value="categoryDefault" disabled>Hour</option>


              { hrOptions.map((option,index)=>{

                       return <option key={index} value={option}> {option}  </option>

                 }

             )}

        </select>



         <select name={props.selectedminute}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
               <option value="categoryDefault" disabled>Minute</option>


              { minOptions.map((option,index)=>{

                       return <option key={index} value={option}> {option}  </option>

                 }

             )}

        </select>


        <select name={props.selectedampm}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
               <option value="categoryDefault" disabled>am or pm</option>


              { ampmOptions.map((option,index)=>{

                       return <option key={index} value={option}> {option}  </option>

                 }

             )}

        </select>











	</div>

     </div>

);


}



















