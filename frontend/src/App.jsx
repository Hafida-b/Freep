import { useState } from 'react'
import './App.css'
import CreateArticle from "./CreateArticle";
import ArticleList from './ArticleList';


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    < CreateArticle />
    < ArticleList />
    </>
  )
}

export default App
