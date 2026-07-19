let ticking = false;
  
function scrollToSection(direction) {
  const sections = Array.from(document.querySelectorAll('.section'));
  const current = sections.findIndex(section => {
    const rect = section.getBoundingClientRect();
    return rect.top >= 0 && rect.top < window.innerHeight;
  });

  if (current === -1) return;

  const nextIndex = direction === 'down'
    ? Math.min(sections.length - 1, current + 1)
    : Math.max(0, current - 1);

  sections[nextIndex].scrollIntoView({ behavior: 'smooth' });
}

window.addEventListener('wheel', (e) => {
  if (ticking) return;

  ticking = true;
  setTimeout(() => ticking = false, 1000); // empêche scroll trop rapide

  if (e.deltaY > 0) {
    scrollToSection('down');
  } else {
    scrollToSection('up');
  }
}, { passive: true });