/** @format */
import MainLayout from "hocs/layouts/MainLayout";
import loginUser from "../assets/svg/login-user.svg";
import correo from "../assets/svg/correo.svg";
import password from "../assets/svg/contraseña.svg";
import { useState } from "react";

function Login() {
	let [formData, setFormData] = useState({});
	let handleChange = (event) => {
		const fieldName = event.target.name;
		const value = event.target.value;
		setFormData({ ...formData, [fieldName]: value });
	};

	function EnviarLogin(e) {
		const csrfCookie = document.cookie.match(
			"(^|;)\\s*csrftoken\\s*=\\s*([^;]+)"
		);
		const csrfToken = csrfCookie ? csrfCookie.pop() : null;
		fetch("./api/Users/login/", {
			method: "POST",
			body: JSON.stringify({
				email: formData.email,
				password: formData.password,
			}),
			headers: {
				"Content-Type": "application/json",
				"X-CSRFToken": csrfToken,
			},
		})
			.then((response) => {
				if (!response.ok) {
					return response.json();
				}
			})
			.then((data) => {
				//errores
				console.log(data);
			});
	}
	function Login(e) {
		e.preventDefault();
		EnviarLogin();
	}
	return (
		<MainLayout>
			<div className="div-center">
				<div className="card login">
					<div className="login-img div-center">
						<img
							src={loginUser}
							style={{ borderRadius: "50%" }}
							alt=""></img>
					</div>
					<div style={{ display: "flex", justifyContent: "center" }}>
						<form>
							<p
								style={{
									fontSize: "30px",
									marginTop: 0,
									fontWeight: 700,
								}}>
								Iniciar sesion
							</p>
							<div className="form-div-stile">
								<img src={correo} alt="correo"></img>
								<input
									id="email"
									type="text"
									placeholder="E-mail"
									name="email"
									value={formData.email}
									onChange={handleChange}
									required></input>
							</div>
							<div className="form-div-stile">
								<img src={password} alt="contraseña"></img>
								<input
									type="password"
									placeholder="Contraseña"
									name="contrasenha"
									value={formData.contrasenha}
									onChange={handleChange}
									required></input>
							</div>
							<div
								className="form-div-stile"
								style={{ width: "auto" }}>
								<input
									onClick={Login}
									type="submit"
									value="Ingresar"
									style={{
										margin: "0px",
										padding: "0px 20px",
									}}></input>
							</div>
							<div
								style={{
									width: "100%",
									marginBottom: "10px",
									display: "flex",
									justifyContent: "center",
								}}>
								<a style={{ color: "black" }} href="./Register">
									Registrarse
								</a>
							</div>
						</form>
					</div>
				</div>
			</div>
		</MainLayout>
	);
}

export default Login;