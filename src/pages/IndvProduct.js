/** @format */

import vegetarian from "../assets/svg/vegetariano_adobe_express.svg";
import not_vegetarian from "../assets/svg/no-vegetarian_adobe_express.svg";
// import { Link } from "react-router-dom";
import { useParams } from "react-router-dom";
import MainLayout from "hocs/layouts/MainLayout";
import React, { useState, useEffect } from "react";
import "./IndvProduct.css";
import "./Home.css";

function IndvProduct(props) {
	const { id } = useParams();
	const [product, setProduct] = useState({});
	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await fetch(
					// `http://localhost:8000/api/Products/${id}`
					`/api/Products/${id}`
				);
				const data = await response.json();
				setProduct(data);
			} catch (error) {
				console.error("Error fetching data:", error);
			}
		};
		fetchData();
	}, [id]);

	return (
		<>
			<MainLayout>
				<div className="home">
					<div className="banner">
						<img src={product.image} alt={product.name} />
					</div>
					<div className="product-indv-detail">
						<p>
							<h2>
								{product.name + "   "}
								<img
									className="vegetarian"
									src={
										product.is_vegetarian
											? vegetarian
											: not_vegetarian
									}
									alt=""
									height="20px"
								/>
							</h2>
						</p>

						<p className="desc">{product.description}</p>
						<p>
							Precio:{" "}
							<span className="price">${product.price}</span>
						</p>

						<p>Valoraciones: {product.votaciones}</p>
					</div>
					<div className="comentarios">
						<h3>Comentarios</h3>
						<div className="cont-comentarios">En desarrollo</div>
					</div>
				</div>
			</MainLayout>
		</>
	);
}

export default IndvProduct;
