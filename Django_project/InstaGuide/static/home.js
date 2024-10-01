function submitForm() {
    var urlInput = document.getElementById('accommodationUrl').value;
    
    // Check if the URL field is empty
    if (urlInput.trim() === "") {
        alert("Warning: The URL field cannot be empty!");
    } else {
        var bookingUrlPattern = /^(https?:\/\/)?(www\.)?booking\.com\/.*$/;
        if (!bookingUrlPattern.test(urlInput)) {
            alert("Warning: The URL must be a valid booking.com link!");
        } else {
            // Λήψη του CSRF token από το cookie
            var csrftoken = getCookie('csrftoken');

            // Αποστολή του URL με το CSRF token στο request
            fetch('/get_reviews/', {
                method: 'POST',
                headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',  // Ο τύπος του αιτήματος
                            'X-CSRFToken': csrftoken  // Προσθήκη του CSRF token στο request
                },
                body: new URLSearchParams({
                    'accommodationUrl': urlInput
                })
            })
            .then(response => {
                console.log("Form submitted successfully");
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    }
}

// Συνάρτηση για να λάβεις το CSRF token από τα cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function clearForm() {
    document.getElementById('accommodationUrl').value = "";
    console.log("Form cleared");
}