// static/chirper/js/scripts.js
// Created: 2025/03/24
// Updated: 2025/03/24
//
// Stores the javasctrip from base.html

// To check javascript is correctly leaded in base.html
document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript from static is loaded!');
});

// Function to retrieve a cookie value by its name
function getCookie(name) {
    let cookieArr = document.cookie.split(";");
    for (let i = 0; i < cookieArr.length; i++) {
        let cookie = cookieArr[i].trim();
        if (cookie.startsWith(name + "=")) {
            return cookie.substring(name.length + 1);
        }
    }
    return null;
}

// Get the 'sort_type' cookie value if it exists
let sortType = getCookie("sort_type");

// Set default value if cookie doesn't exist
if (!sortType) {
    sortType = "date";  // Default value
}

// Update the button text to reflect the current 'sort_type' or default
document.getElementById("dropdownMenuButton").innerText = getButtonText(sortType);

// Function to get button text based on selected sort type
function getButtonText(sortType) {
    switch (sortType) {
        case "most_likes":
            return "Most Likes";
        case "latest_reply":
            return "Latest Reply";
        case "most_replies":
            return "Most Replies";
        default:
            return "Date Created";
    }
}

// Dropdown item selection behavior
document.querySelectorAll('.dropdown-item').forEach(item => {
    item.addEventListener('click', function (event) {
        event.preventDefault();
        let sort_type = this.getAttribute('data-value');
        document.getElementById('dropdownMenuButton').innerText = this.innerText;
        document.getElementById('selectedOption').value = sort_type;

        // Set the cookie with the selected value
        document.cookie = "sort_type=" + sort_type + "; path=/; max-age=86400"; // 86400 seconds = 1 day

        // Submit the form to refresh the page or use AJAX if needed
        document.getElementById('dropdownForm').submit();
    });
});

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.like-btn-toggle').forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Prevents the default button action

            // Get the like button & count span
            let likeCountSpan = document.querySelector(`#like-count-${this.dataset.chirpId}`);
            let chirpId = this.dataset.chirpId;

            // Toggle UI instantly for better UX
            if (this.innerHTML.includes('❤️')) {
                this.innerHTML = '♡';
                this.classList.remove('btn-primary');
                this.classList.add('btn-outline-primary');
                if (likeCountSpan) {
                    likeCountSpan.textContent = Math.max(0, parseInt(likeCountSpan.textContent) - 1);
                }
            } else {
                this.innerHTML = '❤️';
                this.classList.remove('btn-outline-primary');
                this.classList.add('btn-primary');
                if (likeCountSpan) {
                    likeCountSpan.textContent = parseInt(likeCountSpan.textContent) + 1;
                }
            }
        });
    });
});