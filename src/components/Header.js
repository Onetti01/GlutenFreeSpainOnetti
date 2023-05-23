/** @format */

import home from "../../src/assets/svg/home.svg";
import loginUser from "../assets/svg/login-user.svg";
import logOut from "../assets/svg/cerrar-sesion.svg";
import "./Header.css";
import React, { useState } from "react";

function Header() {
	const [isMenuVisible, setIsMenuVisible] = useState(false);

	const handleMouseEnter = () => {
		setIsMenuVisible(true);
	};

	const handleMouseLeave = () => {
		setIsMenuVisible(false);
	};

	function deleteCookie(cookieName) {
		document.cookie = `${cookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
	}

	// Ejemplo de uso

	function cerrarSesion(e) {
		deleteCookie("user_id");
		deleteCookie("name");
		deleteCookie("email");
		window.location.href = "/";
	}

	function getCookieValue(cookieName) {
		const cookieString = document.cookie;
		const cookies = cookieString.split(";");

		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			if (cookie.startsWith(cookieName + "=")) {
				return cookie.substring(cookieName.length + 1);
			}
		}

		return null;
	}
	let usuario = getCookieValue("name");

	return (
		<header>
			<ul>
				<li>
					<a href="/" className="header-link">
						<img src={home} alt="home" height="20px" />
						Home
					</a>
				</li>
				<li>
					<a href="/Products" className="header-link">
						Productos
					</a>
				</li>
			</ul>
			<div className="sesiones">
				{usuario ? (
					<>
						<div
							className="menu-user-links"
							onMouseEnter={handleMouseEnter}
							onMouseLeave={handleMouseLeave}>
							<ul>
								<li>
									<p id="log-info" className="header-user">
										<img
											src={loginUser}
											alt="loginUser"
											height="20px"
										/>
										{usuario}
									</p>
								</li>
								<div
									id="optionss-user"
									className={`user-menu ${
										isMenuVisible ? "" : "hidden"
									}`}>
									<ul>
										<li
											className="user-menu-li"
											id="closeSesion">
											<img
												className="menu-icon"
												src={logOut}
												alt="log out"
												width="20px"
											/>
											<button onClick={cerrarSesion}>
												Cerrar sesión
											</button>
										</li>
									</ul>
								</div>
							</ul>
						</div>
					</>
				) : (
					<>
						<button
							onClick={() => {
								window.location.href = "/Login";
							}}>
							Inicia sesion
						</button>
						<button
							onClick={() => {
								window.location.href = "/Register";
							}}>
							Registrate
						</button>
					</>
				)}
			</div>
		</header>
	);
}

export default Header;
