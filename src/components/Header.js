/** @format */
import logo from "../logo.svg";
import React from "react";
import homa from "../../src/assets/svg/home.svg";

function Header() {
	return (
		<header>
			<img src={logo} alt="logo" height="50px" />
			<ul>
				<li>
					<a href="./" className="header-link">
						<img src={homa} alt="home" height="30px" />
						Home
					</a>
				</li>
			</ul>
			<div className="sesiones">
				<button onClick={()=>{
					window.location.href="./Login"
				}}>Inicia sesion</button>
				<button onClick={()=>{
					window.location.href="./Register"
				}}>Registrate</button>
			</div>
		</header>
	);
}

export default Header;
