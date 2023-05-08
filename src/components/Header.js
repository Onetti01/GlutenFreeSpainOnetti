/** @format */
import logo from "../logo.svg";
import React from "react";

function Header() {
	return (
		<header>
			<a href=" ">
				<img src={logo} alt="logo" height="50px" />
			</a>
			<ul>
				<li>
					<a href=" ">Home</a>
				</li>
			</ul>
		</header>
	);
}

export default Header;
