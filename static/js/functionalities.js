document.addEventListener("DOMContentLoaded", function() {
    var emptyFieldError = document.getElementById("empty_field_error");

    if (emptyFieldError) {
        // Element found, check if it's not hidden
        if (emptyFieldError.textContent.trim() !== "") {
            emptyFieldError.classList.remove("hidden");
        }
    } else {
        console.error("Element with ID 'empty_field_error' not found.");
    }
}); 

document.addEventListener("DOMContentLoaded", function() {
    var  email_exists_error = document.getElementById("email");

    if ( email_exists_error) {
        // Element found, check if it's not hidden
        if ( email_exists_error.textContent.trim() !== "") {
             email_exists_error.classList.remove("hidden");
        }
    } else {
        console.error("Element with ID 'empty_field_error' not found.");
    }
}); 

document.addEventListener("DOMContentLoaded", function() {
    const tab1 = document.getElementById("content-1");
    const tab2 = document.getElementById("content-2");
    const content1 = document.getElementById("docket_forms");
    const content2 = document.getElementById("make_search");

    tab1.addEventListener("click", function() {
        content1.classList.remove("hidden");
        content2.classList.add("hidden");
    });

    tab2.addEventListener("click", function() {
        content1.classList.add("hidden");
        content2.classList.remove("hidden");
    });
});


const uploadButton = document.getElementById('uploadButton');
const captureButton = document.getElementById('captureButton');
const fileInput = document.getElementById('image');

uploadButton.addEventListener('click', () => {
    fileInput.click();
});

captureButton.addEventListener('click', () => {
    // Add JavaScript code to capture photo here
    // This could involve accessing the device's camera using WebRTC or another method
});
