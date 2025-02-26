import { useState } from "react";
import "./App.css";
import CreateArticle from "./CreateArticle";
import SignUpForm from "./SignUp";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <CreateArticle />
      <SignUpForm />
    </>
  );
}

export default App;
