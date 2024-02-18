{
    var lastScroll = window.scrollY;
    const nav = document.getElementById("navigation");

    window.addEventListener('scroll', () => {
        if (lastScroll < window.scrollY) {
            nav.classList.add("nav--hidden");
        }
        else {
            nav.classList.remove("nav--hidden")
        }

        lastScroll = window.scrollY;
    })
}

