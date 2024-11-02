import React from 'react';
import Navbar from './Navbar'
import About from './pages/About'
import Contact from './pages/Contact'
import { Route, Routes } from "react-router-dom"
import Index from './pages/Index';


export default function App() 
{
  return (
    <>
    <Navbar />
    <div className="nav">
      <ul>
        <Routes>
          <Route path="/About" element={<About />} />
          <Route path="/Index" element={<Index />} />
          <Route path="/Contact" element={<Contact />} />
        </Routes>
      </ul>
    </div>
    </>
  );
}