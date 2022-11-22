
// window onload animations

var OnLoadAnimation = anime.timeline({});

OnLoadAnimation.add({
    targets: ".astronaut-img",
    left: '78%',
    duration: 1500,
    easing: 'easeInOutSine'
})

// scroll animations
// const animation2 = anime({
//     targets: ".animation",
//     translateX: 400,
//     duration: 4000
// })

const section3 = document.querySelector(".aboutus3");
