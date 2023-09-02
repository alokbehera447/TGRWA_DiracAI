import {useState} from 'react';


const Greeting = ()=>{

const [changeText, setChangeText] = useState(false);



const changeTextHandler=()=>{

setChangeText(true);

}



return (

<div>

<h2>Hello World</h2>

	{ !changeText && <p> Its good to see you</p>}

        { changeText && <p> Change here</p>}
<button onClick={changeTextHandler}> </button>

</div>	

);	

}

export default Greeting;
