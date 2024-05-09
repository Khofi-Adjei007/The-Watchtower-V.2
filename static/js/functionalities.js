document.getElementById("register-docket").addEventListener("click", function() {
    // Check if the textarea is empty
    var textareaContent = document.getElementById("editor").value;
    if (textareaContent.trim() === "") {
        // Show alert message for empty docket
        alert("Cannot register empty docket!");
        return; // Prevent further execution
    }

    // Get CSRF token from the page
    var csrftoken = getCookie('csrftoken');

    // Proceed with registering the docket using AJAX
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{% url 'submissionpdf' %}", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrftoken); // Set CSRF token in the request headers

    xhr.onload = function () {
        if (xhr.status === 200) {
            // Show success message to the user
            alert("Docket registered successfully! It has been saved internally.");
            // Reset the textarea content
            document.getElementById("editor").value = "";
        } else {
            // Show error message if registration fails
            alert("Failed to register docket. Please try again later.");
        }
    };

    xhr.send(JSON.stringify({ content: textareaContent }));
});

// Function to get CSRF token from the cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie contains the CSRF token
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



 document.getElementById('clear-textarea').addEventListener('click', function() {
        // Select the text area and set its value to an empty string
        document.getElementById('editor').value = '';
    });


    document.getElementById('preview').addEventListener('click', function() {
    // Get the HTML content from the textarea
    var htmlContent = document.getElementById('editor').value;

    // Send the HTML content to the server
    fetch('{% url "submissionpdf" %}', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify({ html_content: htmlContent })
    })
    .then(response => {
        // Check if response is successful
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Return the response as a blob
        return response.blob();
    })
    .then(blob => {
        // Create a URL for the blob
        var url = URL.createObjectURL(blob);
        // Set the PDF content to the object element
        document.getElementById('pdf-preview-object').data = url;
        // Show the PDF preview overlay
        document.getElementById('pdf-preview-overlay').classList.remove('hidden');
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Close the PDF preview overlay when the close button is clicked
document.getElementById('close-pdf-preview').addEventListener('click', function() {
    document.getElementById('pdf-preview-overlay').classList.add('hidden');
});

// Close the PDF preview overlay when clicking outside of it
window.addEventListener('click', function(event) {
    var overlay = document.getElementById('pdf-preview-overlay');
    if (event.target == overlay) {
        overlay.classList.add('hidden');
    }
});





document.addEventListener("DOMContentLoaded", function() {
    const makeSearchLink = document.getElementById("link-make-search");
    const contactTrackingLink = document.getElementById("link-contact-tracking");
    const unsolvedLink = document.getElementById("link-unsolved");
    const profilesLink = document.getElementById("link-profiles");

    const makeSearchContent = document.getElementById("make_a_search");
    const contactTrackingContent = document.getElementById("content-contact-tracking");
    const unsolvedContent = document.getElementById("content-unsolved");
    const profilesContent = document.getElementById("content-profiles");
    const mainContent = document.getElementById("maincontent-1");

    makeSearchLink.addEventListener("click", function(event) {
        event.preventDefault();
        showContent(makeSearchContent);
        hideContent([mainContent, contactTrackingContent, unsolvedContent, profilesContent]);
    });

    contactTrackingLink.addEventListener("click", function(event) {
        event.preventDefault();
        showContent(contactTrackingContent);
        hideContent([mainContent, makeSearchContent, unsolvedContent, profilesContent]);
    });

    unsolvedLink.addEventListener("click", function(event) {
        event.preventDefault();
        showContent(unsolvedContent);
        hideContent([mainContent, makeSearchContent, contactTrackingContent, profilesContent]);
    });

    profilesLink.addEventListener("click", function(event) {
        event.preventDefault();
        showContent(profilesContent);
        hideContent([mainContent, makeSearchContent, contactTrackingContent, unsolvedContent]);
    });

    function showContent(content) {
        content.style.display = "block";
    }

    function hideContent(contents) {
        contents.forEach(function(content) {
            content.style.display = "none";
        });
    }
});



    document.addEventListener("DOMContentLoaded", function() {
    const content1 = document.getElementById("new-docket");
    const content2 = document.getElementById("Happenings");
    const content3 = document.getElementById("Ethics & Conducts");
    const content4 = document.getElementById("History");

    const tab1 = document.getElementById("content-1");
    const tab2 = document.getElementById("content-2");
    const tab3 = document.getElementById("content-3");
    const tab4 = document.getElementById("content-4");

    tab1.addEventListener("click", function() {
        showContent(content1);
        hideContent([content2, content3, content4]);
    });

    tab2.addEventListener("click", function() {
        showContent(content2);
        hideContent([content1, content3, content4]);
    });

    tab3.addEventListener("click", function() {
        showContent(content3);
        hideContent([content1, content2, content4]);
    });

    tab4.addEventListener("click", function() {
        showContent(content4);
        hideContent([content1, content2, content3]);
    });

    function showContent(content) {
        content.style.display = "block";
    }

    function hideContent(contents) {
        contents.forEach(function(content) {
            content.style.display = "none";
        });
    }
});
