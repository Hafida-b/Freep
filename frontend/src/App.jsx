import { AuthProvider } from "./auth";
import Login from "./login";
import { useState } from "react";
import "./App.css";
import CreateArticle from "./CreateArticle";
import ArticleList from "./ArticleList";
import SignUpForm from "./SignUp";

function App() {
  return (
    <AuthProvider>
      <SignUpForm />
      <Login />
      <CreateArticle />
      <ArticleList />
    </AuthProvider>
  );
}

export default App;
