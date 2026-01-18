const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".nav-links");
toggle.addEventListener("click", (e) => {
  e.stopPropagation(); 
  nav.classList.toggle("active");
});
document.addEventListener("click", () => {
  nav.classList.remove("active");
});
nav.addEventListener("click", (e) => {
  e.stopPropagation();
});