/** @format */

import "index.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import Error from "pages/Error";
import Home from "pages/Home";
import Login from "pages/Login";
import Register from "pages/Register";

function App() {
	// fetch("./api/Users/list").then((res)=> res.json())
	// .then(data =>{
	// 	console.log(data)
	// })
	return (
		<Router>
			<Routes>
				<Route path="*" element={<Error></Error>}></Route>

				<Route path="/" element={<Home></Home>}></Route>

				<Route path="/Login" element={<Login></Login>}></Route>

				<Route path="/Register" element={<Register></Register>}></Route>
			</Routes>
		</Router>
	);
}

export default App;
