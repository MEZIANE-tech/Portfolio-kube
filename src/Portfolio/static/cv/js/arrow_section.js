// Gérer les flèches dynamiques
document.querySelectorAll('.collapse-header').forEach(header => {
    const icon = header.querySelector('.arrow'); // Trouve la flèche
    const targetId = header.getAttribute('data-bs-target'); // ID de la section

    // Ajouter un événement pour basculer l'état des flèches
    const target = document.querySelector(targetId);
    target.addEventListener('show.bs.collapse', () => {
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-up');
    });

    target.addEventListener('hide.bs.collapse', () => {
        icon.classList.remove('fa-chevron-up');
        icon.classList.add('fa-chevron-down');
    });
});