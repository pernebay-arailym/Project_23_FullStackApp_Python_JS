import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'

function App() {
  const [contacts, setContacts] = useState([])

  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
  }


  return (
    <>
      
    </>
  )
}

export default App
