import App from "./components/App";
import Top from "./components/Top";
import Pic from "./components/Pic";
import Question from "./components/Question"
import React from "react";
import ReactDOM from "react-dom";


ReactDOM.render(<App />, document.getElementById("app"));
ReactDOM.render(<Top />, document.getElementById("top"));
ReactDOM.render(<Pic />, document.getElementById("pic"));
ReactDOM.render(<Question />, document.getElementById("question"));