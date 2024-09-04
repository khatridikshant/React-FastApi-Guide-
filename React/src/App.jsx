import { useState, useEffect } from 'react'
import api from './Api'


function App() {

  const [transactions,setTransactions] = useState([]);
  const [formData,setFormData] = useState({
    amount: '',
    category: '',
    description: '',
    is_income: false,
    date: ''

  });



  return (
    <>
<div>

</div>
    </>
  )
}

export default App
