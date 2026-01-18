const message = document.getElementById("flash-message");
if (message) {
    setTimeout(() => {
        message.style.opacity = "0";
        setTimeout(() => {
            message.style.display = "none";
        }, 500);
    }, 5000);
}
function comingSoon() {
    document.getElementById("comingPopup").style.display = "flex";
}
function closePopup() {
    document.getElementById("comingPopup").style.display = "none";
}