document.addEventListener('DOMContentLoaded', function() {
    var cropSelect = document.getElementById('crop-select');
    cropSelect.addEventListener('change', function() {
        var selectedCrop = cropSelect.value;
        
        // Construct the URL with the query parameter
        var url = '/map?crop=' + encodeURIComponent(selectedCrop);
        
        // Redirect to the map page with the query parameter
        window.location.href = url;
    });
});