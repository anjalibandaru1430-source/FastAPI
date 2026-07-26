import Navbar from "./Navbar/Navbar";
import {BrowserRouter as Router,Routes,Route} from 'react-router-dom';
import Home from './Components/Home';
import ContactApp from "./ContactApp/ContactApp";
import 'bootstrap/dist/css/bootstrap.min.css';

let App = ()=>{
  return <div className='container-fluid p-0 m-0 '>
            <Router>
              <Navbar/>
              <Routes>
                  <Route path="/index" element={<Home/>}/>
                  <Route path="/contact" element={<ContactApp/>}/>
              </Routes>
            </Router>   
        </div>
}
export default App;