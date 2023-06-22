// Define the map options
var mapOptions = {
    center: [-1.093159, 37.012468], // Set the initial center coordinates
    zoom: 12 // Set the initial zoom level
  };
  
  // Create the map instance
  var map = L.map('map', mapOptions);
  
  // Add a tile layer (e.g., OpenStreetMap)
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
  }).addTo(map);
  // Create a marker with a custom popup
var marker = L.marker([-1.093159, 37.012468]).addTo(map);
marker.bindPopup("<b>Custom Popup Content</b><br>Horticulture").openPopup();
