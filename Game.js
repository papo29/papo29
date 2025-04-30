let score = 0;
let currentAnimalIndex = 0;

const animals = [
  { name: "Delfín", habitat: "salada", image: "delfin.jpg" },
  { name: "Rana", habitat: "dulce", image: "rana.jpg" },
  { name: "Pulpo", habitat: "salada", image: "pulpo.jpg" }
];

const animalImage = document.getElementById('animal-image');
const feedback = document.getElementById('feedback');
const scoreDisplay = document.getElementById('score');

document.getElementById('agua-dulce').addEventListener('click', () => checkAnswer('dulce'));
document.getElementById('agua-salada').addEventListener('click', () => checkAnswer('salada'));

function checkAnswer(answer) {
  const currentAnimal = animals[currentAnimalIndex];
  if (answer === currentAnimal.habitat) {
    feedback.textContent = `¡Correcto! El ${currentAnimal.name} vive en agua ${currentAnimal.habitat}.`;
    score++;
  } else {
    feedback.textContent = `Incorrecto. El ${currentAnimal.name} vive en agua ${currentAnimal.habitat}.`;
  }

  currentAnimalIndex++;

  if (currentAnimalIndex < animals.length) {
    setTimeout(() => {
      updateGame();
    }, 2000);
  } else {
    setTimeout(() => {
      feedback.textContent = `¡Juego terminado! Tu puntaje es: ${score}`;
    }, 2000);
  }
}

function updateGame() {
  const currentAnimal = animals[currentAnimalIndex];
  animalImage.innerHTML = `<img src="${currentAnimal.image}" alt="${currentAnimal.name}">`;
  feedback.textContent = '';
}

updateGame();
