// script.js
// Example: Script to handle form submission
document.addEventListener('DOMContentLoaded', function() {
    const saveButton = document.getElementById('save-button');
    saveButton.addEventListener('click', function() {
      // Logic to handle saving the data
    });
  });
  
// Zoom functionality in script.js
// Initialize scale variable
let scale = 1;

// Make sure to include these functions in your script.js or within a <script> tag in your HTML
function zoomIn() {
  scale += 0.1;
  document.getElementById('diagram-img').style.transform = `scale(${scale})`;
}

function zoomOut() {
  scale = Math.max(1, scale - 0.1);
  document.getElementById('diagram-img').style.transform = `scale(${scale})`;
}

