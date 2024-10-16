function submitForm() {
    var urlInput = document.getElementById('accommodationUrl').value;

    
    if (urlInput.trim() === "") {
        showModal("Warning: The URL field cannot be empty.");
    } else {
        var bookingUrlPattern = /^(https?:\/\/)?(www\.)?booking\.com\/.*$/;
        if (!bookingUrlPattern.test(urlInput)) {
            showModal("Warning: The URL must be a valid booking.com link.");
        } else {
            var csrftoken = getCookie('csrftoken');

            document.getElementById('textbox').innerText = "Creating summary...";

            fetch('/get_reviews/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrftoken
                },
                body: new URLSearchParams({
                    'accommodationUrl': urlInput
                })
            })
            .then(response => response.text())  
            .then(data => {
                
                document.getElementById('textbox').innerText = data;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    }
}



function clearForm() {
    document.getElementById('accommodationUrl').value = "";
    document.getElementById('textbox').innerText = "The summary of the accommodation reviews will appear here ...";
    console.log("Form and textbox cleared");
}


function showModal(message) {
    var modal = document.getElementById('customAlert');
    var modalMessage = document.getElementById('modalMessage');
    modalMessage.innerText = message;
    modal.style.display = "flex";
    document.body.style.pointerEvents = "none";
    modal.style.pointerEvents = "auto";
}


function closeModal() {
    var modal = document.getElementById('customAlert');
    modal.style.display = "none";
    document.body.style.pointerEvents = "auto";
}


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
