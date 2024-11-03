document.addEventListener('DOMContentLoaded', function() {
    var cropForm = document.getElementById('crop-form');
    cropForm.addEventListener('submit', function(event) {
        event.preventDefault();

        var cropSelect = document.getElementById('crop-select');
        var yearSelect = document.getElementById('year-select');
        var selectedCrop = cropSelect.value;
        var selectedYear = yearSelect.value;

        if (selectedCrop && selectedYear) {
            var url = '/map?crop=' + encodeURIComponent(selectedCrop) + '&year=' + encodeURIComponent(selectedYear);
            window.location.href = url;
        }
    });
});