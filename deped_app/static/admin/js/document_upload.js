document.addEventListener('DOMContentLoaded', function() {
    function updateFileField() {
        const year = document.getElementById('id_year').value;
        const month = document.getElementById('id_month').value;
        const fileField = document.getElementById('id_file');
        
        if (year && month) {
            fileField.required = true;
            // Update the upload path to include year/month
            const currentPath = fileField.getAttribute('data-current-path') || '';
            const newPath = `divisionmemo/${year}/${month}/`;
            if (!currentPath.includes(newPath)) {
                fileField.setAttribute('data-upload-path', newPath);
            }
        } else {
            fileField.required = false;
        }
    }
    
    // Initialize on load
    updateFileField();
    
    // Add event listeners
    document.getElementById('id_year').addEventListener('change', updateFileField);
    document.getElementById('id_month').addEventListener('change', updateFileField);
});