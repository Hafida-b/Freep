import { AuthProvider } from "./auth";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./login";
import CreateArticle from "./CreateArticle";
import ArticleList from "./ArticleList";
import SignUpForm from "./SignUp";
import Navigation from "./Navigation";
import "./App.css";

function App() {
  return (
    
    <AuthProvider>
      <Router>
      <Navigation />
        <Routes>
          <Route path="/" element={<ArticleList />} />
          <Route path="/signup" element={<SignUpForm />} />
          <Route path="/login" element={<Login />} />
          <Route path="/create" element={<CreateArticle />} />
          <Route path="/articles" element={<ArticleList />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;