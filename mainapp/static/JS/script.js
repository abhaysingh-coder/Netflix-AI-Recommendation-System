const carouselElement = document.querySelector('#netflixCarousel');
if (carouselElement) {
    new bootstrap.Carousel(carouselElement, {
      interval: 3500,
      ride: 'carousel',
      pause: false,
      wrap: true
    });
}