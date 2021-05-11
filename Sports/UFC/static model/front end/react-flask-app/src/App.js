import React, { useState, useEffect } from "react";
import Home from "./Pages/Home";
import Appski from "./Pages/Appski";
import NoPage from "./Pages/NoPage";
import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";

function App() {
	const [placeholder, setPlaceholder] = useState("Hi");

	useEffect(() => {
		fetch("/hello")
			.then((res) => res.json())
			.then((data) => {
				setPlaceholder(data.result);
			});
	}, []);

	return (
		<div className="App">
			<header className="App-header">
				<Router>
					<Switch>
						<Route exact path="/" component={Home} />
						<Route exact path="/app" component={Appski} />
						<Route component={NoPage} />
					</Switch>
				</Router>
			</header>
		</div>
	);
}

export default App;
