new Swiper('.card-wrapper', {
    // Optional parameters
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      dynamicBullets: true

    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    breakpoints: {
      // when window width is >= 320px
      0: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      // when window width is >= 480px
      1000: {
        slidesPerView: 2,
        spaceBetween: 30
      },
    // //   when window width is >= 640px
    //   1024: {
    //     slidesPerView: 3,
    //     spaceBetween: 140
    //   }
    }
  });