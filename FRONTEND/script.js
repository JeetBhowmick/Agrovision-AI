const scroll = new LocomotiveScroll({
    el: document.querySelector('#main'),
    smooth: true
});


function page4Animation() {
    var elemC = document.querySelector("#elem-container")
    var fixed = document.querySelector("#fixed-image")
    elemC.addEventListener("mouseenter", function () {
        fixed.style.display = "block"
    })
    elemC.addEventListener("mouseleave", function () {
        fixed.style.display = "none"
    })

    var elems = document.querySelectorAll(".elem")
    elems.forEach(function (e) {
        e.addEventListener("mouseenter", function () {
            var image = e.getAttribute("data-image")
            fixed.style.backgroundImage = `url(${image})`
        })
    })
}

function swiperAnimation() {
  var swiper = new Swiper(".mySwiper", {
    slidesPerView: "auto",
    centeredSlides: false,
    spaceBetween: 20,
    grabCursor: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true, // adds smaller progressive dots
    },
  });
}
function menuAnimation() {
  const menu = document.querySelector("nav h3");
  const navimg = document.querySelector("nav img");
  const nav = document.querySelector("nav");
  menu.innerHTML = `
        <span style="display:flex;align-items:center;gap:6px;">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#000000bb" viewBox="0 0 24 24">
            <path d="M3 6h18v2H3zM3 11h18v2H3zM3 16h18v2H3z"/>
          </svg>
          <span>Menu</span>
        </span>
      `;

  menu.addEventListener("click", function () {
    const isActive = nav.classList.toggle("active");

    if (isActive) {
      navimg.style.opacity = 0;
      menu.innerHTML = `
        <span style="display:flex;align-items:center;gap:6px;">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#fff" viewBox="0 0 24 24">
            <path d="M12 8l6 6H6z"/>
          </svg>
          <span>Close</span>
        </span>
      `;
      menu.style.color = "#000000bb";  
      menu.style.borderColor = "#6e6d6da1"
    } 
    else {
      navimg.style.opacity = 1;
      menu.innerHTML = `
        <span style="display:flex;align-items:center;gap:6px;">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#000000bb" viewBox="0 0 24 24">
            <path d="M3 6h18v2H3zM3 11h18v2H3zM3 16h18v2H3z"/>
          </svg>
          <span>Menu</span>
        </span>
      `;
      menu.style.color = "#000000bb"; 
      menu.style.borderColor = "#6e6d6da1";
    }
  });
}

function loaderAnimation() {
  const loader = document.querySelector("#loader");
  setTimeout(() => {
    loader.style.top = "-100%";
  }, 7000); 

}

loaderAnimation()

swiperAnimation()
page4Animation()
menuAnimation()
