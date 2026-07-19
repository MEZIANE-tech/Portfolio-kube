function toggleMobileMenu() {
  const nav = document.getElementById('mobileNav');
  const burger = document.querySelector('.burger');
  const overlay = document.getElementById('mobileOverlay');

  nav.classList.toggle('active');
  burger.classList.toggle('open');
  overlay.classList.toggle('active');

  // Empêche le scroll du body
  document.body.classList.toggle('no-scroll');
}
