    document.addEventListener("DOMContentLoaded", function () {
        // Fonction pour gérer le défilement avec un décalage
        const handleScrollWithOffset = () => {
            const anchor = window.location.hash;

            if (anchor) {
                // Trouver la section ciblée par l'ancre
                const header = document.querySelector(`[id="${anchor.slice(1)}"]`);
                const collapsible = header?.querySelector('.collapse');

                if (collapsible) {
                    const targetId = collapsible.id; // ID de la section collapsible
                    const targetElement = document.querySelector(`#${targetId}`);

                    // Déplier la section
                    targetElement.classList.add("show");

                    // Mettre à jour l'état du header pour l'ouvrir
                    const headerToggle = document.querySelector(`[data-bs-target="#${targetId}"]`);
                    if (headerToggle) {
                        headerToggle.setAttribute("aria-expanded", "true");
                    }

                    // Décalage pour éviter la navbar
                    const navbarHeight = document.querySelector('.navbar').offsetHeight || 0;
                    const targetPosition = header.offsetTop - navbarHeight - 20;

                    // Effectuer le défilement avec offset
                    window.scrollTo({
                        top: targetPosition,
                        behavior: "smooth"
                    });
                }
            }
        };

        // Utiliser `setTimeout` pour différer le défilement après une redirection
        setTimeout(handleScrollWithOffset, 300);

        // Alternative : Attendre l'événement `load` pour garantir que tout est prêt
        window.addEventListener("load", handleScrollWithOffset);
    });

