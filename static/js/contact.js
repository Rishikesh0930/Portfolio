const message = document.getElementById("flash-message");
if (message) {
    setTimeout(() => {
        message.style.opacity = "0";
        setTimeout(() => {
            message.style.display = "none";
        }, 500);
    }, 10000);
}