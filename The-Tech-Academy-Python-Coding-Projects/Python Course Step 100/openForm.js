function openForm() {
    document.getElementById("myContactForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myContactForm").style.display = "none";
}

function valForm() {
    var name = document.forms["contactForm"]["name"].value;
    var email = document.forms["contactForm"]["email"].value;
    var phone = document.forms["contactForm"]["phone"].value;
    var phno = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (name == "") {
        alert("Name is required");
    } else if (email == "") {
        alert("Email is required");
    } else if (phone == "") {
        alert("Phone number is required");
        return false;
    }
}

$(document).ready(function(){
    $("a").on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrolltop: $(hash).offset().top
            }, 90, function(){
                window.location.hash = hash;
            });
        }
    });
});