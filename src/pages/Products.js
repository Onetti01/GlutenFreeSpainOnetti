/** @format */

import MainLayout from "hocs/layouts/MainLayout";
import Product from "components/Product";
import React, { useState, useEffect } from "react";
import "./Home.css";
import "./Products.css";
// import { Link } from "react-router-dom";

function Products(props) {
	const [Productos, setProductos] = useState([]);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await fetch(
					// "http://localhost:8000/api/Products/list"
					"/api/Products/list"
				);
				const data = await response.json();
				setProductos(data.Products);
			} catch (error) {
				console.error("Error fetching data:", error);
			}
		};
		fetchData();
	}, []);
	return (
		<MainLayout>
			<div className="all-products">
				{Productos.map((product, index) => (
					<Product product={product}></Product>
				))}
			</div>
		</MainLayout>
	);
}

export default Products;
