import { useState } from 'react'
import './App.css'
import CreateArticle from "./CreateArticle";


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    < CreateArticle />
    </>
  )
}

export default App
