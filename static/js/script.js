document.addEventListener("DOMContentLoaded", function() {
    const uploadInput = document.getElementById('imageUpload');
    const preview = document.getElementById('imagePreview');
    const fileLabel = document.querySelector('label[for="imageUpload"]');
    const dropArea = document.getElementById('drop-area'); // Ensure you have this ID in your HTML
    // Existing input change event listener
    uploadInput.addEventListener('change', function(event) {
        
    });

    // Drag and drop events
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false); // Optional: prevent defaults for the whole document
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    dropArea.addEventListener('drop', handleDrop, false);

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    function highlight() {
        dropArea.classList.add('highlight');
    }

    function unhighlight() {
        dropArea.classList.remove('highlight');
    }

    function handleDrop(e) {
        let dt = e.dataTransfer;
        let files = dt.files;
        handleFiles(files);
    }

    function handleFiles(files) {
        ([...files]).forEach(file => {
            previewFile(file);
            // Add here any upload functionality or other processing
        });
    }

    function previewFile(file) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = () => {
            preview.src = reader.result;
            preview.style.display = 'block';
            fileLabel.textContent = file.name; // Update label text to the name of the file
        };
    }
});
