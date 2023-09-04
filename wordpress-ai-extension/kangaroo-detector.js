jQuery(document).ready(function($) {
    console.log("Initiating AJAX request...");

    // Handle the image upload form submission
    $('form[name="kangaroo-upload-form"]').on('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        var formData = new FormData(this);
        for (var pair of formData.entries()) {
            console.log(pair[0] + ', ' + pair[1]);
        }
        $.ajax({
            url: '/wp-admin/admin-ajax.php?action=upload_image_proxy', 
            type: 'POST',
            data: formData,
            dataType: 'json',
            contentType: false,
            processData: false,
            success: function(data) {
                console.log("AJAX request successful. Received data:", data);
                if (data.error) {
                    // Handle errors returned from the backend
                    console.error("Backend Error:", data.error);
                    displayMessage("Error: " + data.error);
                } else {
                    // Update the score on the page
                    console.log("Non float-Parsed Score:", data.score);
                    console.log("float-Parsed Score:", parseFloat(data.score));
                    displayScore(parseFloat(data.score));
                }
            },
            error: function(xhr, status, error) {
                console.error("AJAX request failed:", error);
                displayMessage("Failed to get a score. Please try again.");
            },

            complete: function() {
                console.log("AJAX request completed.");
            }
        });
    });

    // Function to display the score on the page
    function displayScore(score) {
        var scoreContainer = $('#kangaroo-score-container'); 
        scoreContainer.text(`Kangaroo score: ${score.toFixed(2)}`);
        console.log("Updated kangaroo-score-container with score:", score.toFixed(2));
    }

    // Function to display messages (like errors)
    function displayMessage(message) {
        var scoreContainer = $('#kangaroo-score-container'); 
        scoreContainer.text(message);
    }

});