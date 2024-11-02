import React from 'react';
import Index from './pages/Index'
import Navbar from './Navbar'
import About from './pages/About'
import { Route, Routes } from "react-router-dom"


export default function App() 
{
  return (
    <>
    <Navbar />
    <div className="Container">
      <Routes>
        <Route path="/About" element={<About />} />
        <Route path="/Index" element={<Index />} />
      </Routes>
    </div>
    </>
  );
}