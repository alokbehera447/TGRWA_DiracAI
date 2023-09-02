import {render,screen} from '@testing-library/react';
import Greeting from './Greeting';
import userEvent from '@testing-library/user-event';


describe('Greeting Component',()=>{
	
test('renders hello world',()=>{
//Arrage
render(<Greeting/>);
//Act
//nothing
//Assert
const HelloWorldElement = screen.getByText('Hello World',{exact: true})
expect(HelloWorldElement).toBeInTheDocument();
});




test('good to see you no click',()=>{

render(<Greeting/>);

const outputElement = screen.getByText('good to see you',{exact: false}); 	


});





});



