import classes from './FormInputObjects.module.css';





export const TextInput = (props)=>{

return <div className={classes.name_div}>
          <div className={classes.name_txt}>{props.label}</div>
          <div className={classes.name_inputDiv} >
            <input
              type="text"
              onChange={props.handleChange}
              name={props.name}
              className={classes.input_field}
              placeholder={props.placeholder}
              defaultValue=""
            />
         </div>
    </div>

}





export const OptionField = (props)=>{


return <div className={classes.name_div}>

        <div className={classes.name_txt}>{props.label}</div>
	<div className={classes.name_inputDiv} >

        <select name={props.name}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
          <option value="categoryDefault" disabled>Choose an option</option>

          
          { props.options.map((option,index)=>{

                return <option key={index} value={option.id}> {option.name}  </option>
 
                }

          )}

        </select>
    </div>
 </div>


}





export const OptionFieldAdr = (props)=>{


return <div className={classes.name_div}>

        <div className={classes.name_txt}>{props.label}</div>
        <div className={classes.name_inputDiv} >

        <select name={props.name}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
          <option value="categoryDefault" disabled>Choose an option</option>


          { props.options.map((option,index)=>{

                return <option key={index} value={option.name}> {option.name}  </option>

                }

          )}

        </select>
    </div>
 </div>


}





















export const OptionFieldSubmitValue = (props)=>{


return <div className={classes.name_div}>

        <div className={classes.name_txt}>{props.label}</div>
        <div className={classes.name_inputDiv} >

        <select name={props.name}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
          <option value="categoryDefault" disabled>Choose an option</option>


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

        <div className={classes.name_txt}>{props.label}</div>
        <div className={classes.name_inputDiv} >

        <select name={props.name}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
          <option value="categoryDefault" disabled>Choose an option</option>


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
              className={classes.inputText_field}
              placeholder={props.placeholder}
              defaultValue=""
            />
         </div>
    </div>

}



export const DateField = (props) =>{

return( 
	<div className={classes.name_div}>
        <div className={classes.name_txt}>{props.label}</div>
        <div className={classes.name_inputDiv}>
	{/*<div className={classes.dob_innerDiv2}>*/}
          <input
             type="date"
             onChange={props.handleChange}
             name={props.name}
	     className={classes.input_field_date}
             placeholder={props.placeholder}

          />
	{/*</div>*/}
       </div>

     </div>

);


}











