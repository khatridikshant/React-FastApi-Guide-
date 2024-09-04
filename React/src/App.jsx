import { useState, useEffect } from 'react'
import api from './Api'


function App() {

  const [transactions, setTransactions] = useState([]);
  const [formData, setFormData] = useState({
    amount: '',
    category: '',
    description: '',
    is_income: false,
    date: ''

  });


  const fetchTransactions = async () => {
    const response = await api.get('/transactions/')
    setTransactions(response.data)
  }

  useEffect(() => { fetchTransactions(), [] })

  const handleInputChange = (event) => {
    const value = event.target.type == 'checkbox' ? event.target.checked : event.target.value;
    setFormData({
      ...formData, [event.target.name]: value,
    });
  }

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api.post('/transactions/', formData);
    fetchTransactions()
    setFormData({
      amount: '',
      category: '',
      description: '',
      is_income: false,
      date: ''
    })
  };


  return (
    <div>
      <nav className='navbar navbar-dark bg-primary'>
        <div className="container-fluid">
          <a className='navbar-brand' href='#'>
            Finance Application
          </a>
        </div>

      </nav>
      <div className='container'>

        <form onSubmit={handleFormSubmit}>
          <div className='mb-3 mt-3'>

            <label for="amount" class="form-label">Amount</label>
            <input type="number" name='amount' class="form-control" id="amount" placeholder="Amount" onChange={handleInputChange} value={formData.amount} />


          </div>

          <div className='mb-3 mt-3'>

            <label for="category" class="form-label">Category</label>
            <input type="text" name='category' class="form-control" id="category" placeholder="Category" onChange={handleInputChange} value={formData.category} />


          </div>


          <div className='mb-3 mt-3'>

            <label for="description" class="form-label">Description</label>
            <input type="text" name='description' class="form-control" id="description" placeholder="Description" onChange={handleInputChange} value={formData.description} />


          </div>

          <div className='mb-3 mt-3'>

            <label for="is_income" class="form-label">Is_Income</label>
            <input type="checkbox" class="m-2" name='is_income' id="is_income"  onChange={handleInputChange} value={formData.is_income} />


          </div>

          <div className='mb-3 mt-3'>

            <label for="date" class="form-label">Date</label>
            <input type="text" name='date' class="form-control" id="date" placeholder="Date" onChange={handleInputChange} value={formData.date} />


          </div>

          <button  type='submit' className='btn btn-primary'>
            Submit
          </button>



        </form>

      </div>
    </div>
  )
}

export default App
