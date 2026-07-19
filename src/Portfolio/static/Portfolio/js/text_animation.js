const words = ["DevOps", "De Production" ];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;

const typingSpeed = 200; // Vitesse d'écriture (ms)
const deletingSpeed = 100; // Vitesse de suppression (ms)
const pauseBeforeDeleting = 2000; // Pause après l'écriture complète d'un mot (ms)
const pauseBeforeTyping = 1000; // Pause avant d'écrire un nouveau mot (ms)

const animatedText = document.getElementById("animated-text");

function typeEffect() {
  const currentWord = words[wordIndex];
  const displayedText = currentWord.substring(0, charIndex);

  animatedText.textContent = displayedText;

  if (!isDeleting && charIndex < currentWord.length) {
    charIndex++; // Ajouter un caractère
    setTimeout(typeEffect, typingSpeed); // Vitesse d'écriture
  } else if (!isDeleting && charIndex === currentWord.length) {
    isDeleting = true;
    setTimeout(typeEffect, pauseBeforeDeleting); // Pause avant suppression
  } else if (isDeleting && charIndex > 0) {
    charIndex--; // Supprimer un caractère
    setTimeout(typeEffect, deletingSpeed); // Vitesse de suppression
  } else if (isDeleting && charIndex === 0) {
    isDeleting = false;
    wordIndex = (wordIndex + 1) % words.length; // Mot suivant
    setTimeout(typeEffect, pauseBeforeTyping); // Pause avant d'écrire le prochain mot
  }
}

// Démarrer l'effet
typeEffect();

