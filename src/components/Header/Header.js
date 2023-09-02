import classes from './Header.module.css';
import HeaderLeft from './HeaderLeft';
import HeaderRight from './HeaderRight';




function Header(props){

return (

   <>
   <header className={classes.header}>

     <HeaderLeft 
	onPress = {props.onPress} 
	userData={props.userData} 
     />

     	
     <HeaderRight
	userData={props.userData}
	rerender={props.rerender}
	/>	
      

   </header>
  </>


);
}


export default Header;
















