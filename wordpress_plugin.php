<?php
/*
Plugin Name: Kangaroo Classifier
Description: A plugin to classify kangaroo images
Version: 1.0
Author: Your Name
*/

function kangaroo_classifier_shortcode() {
    ob_start();
    ?>
    <form action="http://localhost:5000/predict" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*">
        <input type="submit" value="Upload Image">
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode('kangaroo_classifier', 'kangaroo_classifier_shortcode');
