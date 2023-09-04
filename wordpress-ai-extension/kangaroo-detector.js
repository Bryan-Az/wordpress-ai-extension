jQuery(document).ready(function($) {
    // Handle the image upload form submission
    $('form[name="kangaroo-upload-form"]').on('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        var formData = new FormData(this);

        $.ajax({
            url: '/wp-admin/admin-ajax.php?action=upload_image_proxy', 
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.error) {
                    // Handle errors returned from the backend
                    console.error("Backend Error:", data.error);
                    displayMessage("Error: " + data.error);
                } else {
                    // Update the score on the page
                    displayScore(data.score);
                }
            },
            error: function(xhr, status, error) {
                console.error("AJAX request failed:", error);
                displayMessage("Failed to get a score. Please try again.");
            }
        });
    });

    // Function to display the score on the page
    function displayScore(score) {
        var scoreContainer = $('#kangaroo-score-container'); 
        scoreContainer.text('Kangaroo Score: ' + score);
    }

    // Function to display messages (like errors)
    function displayMessage(message) {
        var scoreContainer = $('#kangaroo-score-container'); 
        scoreContainer.text(message);
    }
});