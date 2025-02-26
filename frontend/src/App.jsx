import { AuthProvider } from "./auth";
import Login from "./login";
import { useState } from 'react'
import './App.css'
import CreateArticle from "./CreateArticle";
import ArticleList from './ArticleList';

function App() {
  return (
    <AuthProvider>
      <Login />
      < CreateArticle />
      < ArticleList />
    </AuthProvider>
  );

export default App;
