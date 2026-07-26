import React from 'react'
import { Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css' 

const Navbar = () => {
  return <nav className='navbar navbar-expand-lg navbar-dark bg-dark'>
    <Link to='/index' className='navbar-brand'>Logo</Link>
    <div className='ms-auto'>
        <ul className='navbar-nav'>
            <li><Link to='/index' className='nav-link'>Home</Link></li>
            <li><Link to='/contact' className='nav-link'>Contact</Link></li>
        </ul>
    </div>
  </nav>
}

export default Navbar