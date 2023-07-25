new Swiper('.js-carousel', {  
    slidesPerView: 4,
    spaceBetween: 30,
    speed: 9000,
    loop: true,
    updateOnWindowResize: true,
    allowTouchMove: false, // можно ещё отключить свайп
    autoplay: {
      delay: 0,
      disableOnInteraction: false // или сделать так, чтобы восстанавливался autoplay после взаимодействия
    }
});



