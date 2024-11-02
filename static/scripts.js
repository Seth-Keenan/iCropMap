document.addEventListener('DOMContentLoaded', function() {
    var cropForm = document.getElementById('crop-form');
    cropForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        var cropSelect = document.getElementById('crop-select');
        var selectedCrop = cropSelect.value;
        
        if (selectedCrop != "") {
            // Construct the URL with the query parameter
            var url = '/map?crop=' + encodeURIComponent(selectedCrop);

            // Redirect to the map page with the query parameter
            window.location.href = url;   
        }
    });
});