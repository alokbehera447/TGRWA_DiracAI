import classes from './OptionField.module.css';





export const OptionField = (props)=>{


return <div className={classes.name_div}>


        <select name={props.name}  onChange={props.handleChange} type="text" className={classes.input_field} defaultValue={"categoryDefault"}>
          <option value="categoryDefault" disabled>+91</option>


          { props.options.map((option,index)=>{

                return <option key={index} value={option}> {option}  </option>

                }

          )}

        </select>
 </div>


}
