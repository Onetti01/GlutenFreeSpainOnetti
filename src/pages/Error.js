/** @format */

import MainLayout from "hocs/layouts/MainLayout";
import { connect } from "react-redux";

function Error() {
	return (
		<MainLayout>
			<div>La ruta no existe</div>
		</MainLayout>
	);
}

const mapStateToProps = (state) => ({});

export default connect(mapStateToProps, {})(Error);
