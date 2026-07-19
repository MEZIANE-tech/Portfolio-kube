const swiper = new Swiper('.card-wrapper', {
    loop: true,
    spaceBetween: 30,
    
  
    // pagination bullets
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
        
      },
      // when window width is >= 480px
      768: {
        slidesPerView: 2,
        spaceBetween: 20,
      },

      1360: {
        slidesPerView: 3,
        spaceBetween: 30,

        
      }
    }
  });