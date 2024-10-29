
var summary; 

function submitForm() {
    var urlInput = document.getElementById('accommodationUrl').value;
    var languageSelect = document.getElementById('language-select').value;

    if (urlInput.trim() === "") {
        showModal("Warning: The URL field cannot be empty.");
    } else {
        var bookingUrlPattern = /^(https?:\/\/)?(www\.)?booking\.com\/.*$/;
        if (!bookingUrlPattern.test(urlInput)) {
            showModal("Warning: The URL must be a valid booking.com link.");
        } else {
            var csrftoken = getCookie('csrftoken');

            document.getElementById('textbox').innerText = "Fetching reviews...";

            
            fetch('/get_reviews/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrftoken
                },
                body: new URLSearchParams({
                    'accommodationUrl': urlInput,
                    'language': languageSelect 
                })
            })
            .then(() => {
                document.getElementById('textbox').innerText = "Creating summary...";
                
                return fetch('/cr_summ/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': csrftoken
                    }
                });
            })
            .then(response => response.text())  
            .then(summary => {
                
                document.getElementById('textbox').innerText = summary;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    }
}



function submitQuery() {
    var specificInfo = document.getElementById('specificInfo').value;
    var languageSelect = document.getElementById('language-select').value;

    if (specificInfo.trim() === "") {
        showModal("Warning: The query field cannot be empty.");
    } else {
        var csrftoken = getCookie('csrftoken');
        document.getElementById('textbox').innerText = "Processing query...";
      
        fetch('/get_query/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken
            },
            body: new URLSearchParams({
                'specificInfo': specificInfo,
                'language': languageSelect 
            })
        })
        .then(response => response.text())
        .then(data => {
            if (data === "no_url") {
                               
                document.getElementById('textbox').innerText = 'The summary and the answers to the queries will appear here...';
                showModal("Warning: You need to provide the accommodation URL first.");
                
            } else {
                
                document.getElementById('textbox').innerText = data;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}



function clearForm() {
    var csrftoken = getCookie('csrftoken');

    fetch('/clear_reviews/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('accommodationUrl').value = "";
        document.getElementById('specificInfo').value = ""; 
        document.getElementById('textbox').innerText = "The summary and the answers to the queries will appear here...";
        console.log("Form and reviews cleared");
        summary = undefined;
    })
    .catch(error => {
        console.error('Error:', error);
    });
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
