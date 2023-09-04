<?php
/*
Plugin Name: Kangaroo Detector
Description: A plugin to detect kangaroos in images.
Version: 1.0
Author: 
*/

// Adding the CSS and JS files
function kangaroo_detector_scripts() {
    // Enqueue the stylesheet for the plugin
    // wp_enqueue_style('kangaroo-detector', plugin_dir_url(__FILE__) . 'kangaroo-detector.css', array(), '1.0.0', 'all');

    // Enqueue jQuery (though it's usually already included by WordPress themes)
    wp_enqueue_script('jquery');

    // Enqueue the custom JavaScript for the plugin, ensuring it's loaded after jQuery
    wp_enqueue_script('kangaroo-detector', plugin_dir_url(__FILE__) . 'kangaroo-detector.js', array('jquery'), '1.0.0', true);
}
add_action('wp_enqueue_scripts', 'kangaroo_detector_scripts');

// Creating a shortcode for the plugin
function kangaroo_detector_shortcode() {
    ob_start();
    ?>
    <form name="kangaroo-upload-form" method="post" enctype="multipart/form-data">
        <input type="file" name="image" required>
        <input type="submit" value="Upload Image">
    </form>
    <div id="kangaroo-score-container"></div>
    <?php
    return ob_get_clean();
}
add_shortcode('kangaroo_detector', 'kangaroo_detector_shortcode');

// Proxy endpoint to handle AJAX request and forward it to the Flask app
function kangaroo_detector_proxy_endpoint() {
    error_log(print_r($_FILES, true));
    if (isset($_FILES['image'])) {
        $image_data = file_get_contents($_FILES['image']['tmp_name']);
        error_log(print_r($_FILES['image'], true));
        $response = wp_remote_post('http://flask-app:5000/predict', array(
            'body' => json_encode(array('image' => base64_encode($image_data))),
            'headers' => array('Content-Type' => 'application/json')
        ));

        if (is_wp_error($response)) {
            echo 'Failed to get a response from the model.';
            wp_die();
        }

        echo $response['body'];
        wp_die();
    } else {
        error_log("Upload error code: " . $_FILES['image']['error']);
        echo json_encode(["error" => "No image data received. Error code: " . $_FILES['image']['error']]);
        wp_die();
}

}
add_action('wp_ajax_upload_image_proxy', 'kangaroo_detector_proxy_endpoint');
add_action('wp_ajax_nopriv_upload_image_proxy', 'kangaroo_detector_proxy_endpoint');

?>
