import React, { useEffect } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import '../index.css';

const MapComponent = () => {
  useEffect(() => {
    // Initialize the map
    const map = L.map('map', {
      center: [38.690083, -100.809859],
      zoom: 5,
    });

    // Add the tile layer
    L.tileLayer('https://api.maptiler.com/maps/hybrid/{z}/{x}/{y}.jpg?key=oAuktb1FxylJvFK6EM', {
      attribution: '&copy; <a href="https://www.maptiler.com/copyright" target="_blank">MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>',
    }).addTo(map);

    // Cleanup function to remove the map instance
    return () => {
      map.remove();
    };
  }, []);

  return (
    <div
      id="map"
      style={{
        height: '100vh', // Set the height as per your requirement
        width: '100%', // Set the width as per your requirement
      }}
    >{<MapComponent />}</div>
  );
};

export default MapComponent;