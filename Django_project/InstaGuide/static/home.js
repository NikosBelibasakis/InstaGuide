function clearForm() {
    document.getElementById('accommodationUrl').value = '';
}



function submitForm() {
    var urlInput = document.getElementById('accommodationUrl').value;
    
    if (urlInput.trim() === "") {
        alert("Warning: The URL field cannot be empty!");
    } else {
        
        console.log("Form submitted successfully");
    }
}
