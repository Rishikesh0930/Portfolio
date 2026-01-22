// const message = document.getElementById("flash-message");
// if (message) {
//     setTimeout(() => {
//         message.style.opacity = "0";
//         setTimeout(() => {
//             message.style.display = "none";
//         }, 500);
//     }, 10000);
// }
function closePopup() {
    document.getElementById("comingPopup").style.display = "none";
}

window.onload = function () {
    const popup = document.getElementById("comingPopup");
    if (popup) {
        document.getElementById("comingPopup").style.display = "flex";
    }
};