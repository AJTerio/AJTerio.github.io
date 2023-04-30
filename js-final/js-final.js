// Scrollbar
let scroll = document.getElementById("scrollbar");
let totalHeight = document.body.scrollHeight - window.innerHeight;
window.onscroll = function () {
    let scrollHeight = (window.pageYOffset / totalHeight) * 100;
    scroll.style.height = scrollHeight + "%";
    }