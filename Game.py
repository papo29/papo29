// Estructura básica en React para la app educativa interactiva
// Nivel 3: Reino Acuático – “El Gran Océano Azul”

import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { motion } from "framer-motion";

const animals = [
  { name: "Delfín", habitat: "salada", image: "/animals/delfin.png" },
  { name: "Rana", habitat: "dulce", image: "/animals/rana.png" },
  { name: "Pulpo", habitat: "salada", image: "/animals/pulpo.png" },
  { name: "Bagre", habitat: "dulce", image: "/animals/bagre.png" },
  { name: "Tortuga marina", habitat: "salada", image: "/animals/tortuga.png" }
];

export default function OceanLevel() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [feedback, setFeedback] = useState("");

  const handleChoice = (choice) => {
    const currentAnimal = animals[currentIndex];
    if (choice === currentAnimal.habitat) {
      setFeedback("¡Correcto! " + currentAnimal.name + " ha vuelto a casa.");
      setScore(score + 1);
    } else {
      setFeedback("Intenta de nuevo. Recuerda dónde vive " + currentAnimal.name + ".");
    }

    setTimeout(() => {
      setFeedback("");
      if (currentIndex + 1 < animals.length) {
        setCurrentIndex(currentIndex + 1);
      } else {
        alert("¡Nivel completado! Has ganado la medalla 'Nadador Estrella'.");
      }
    }, 1500);
  };

  const progressPercent = (score / animals.length) * 100;

  return (
    <div className="p-4 max-w-xl mx-auto text-center">
      <h1 className="text-2xl font-bold mb-4">Nivel 3: El Gran Océano Azul</h1>

      <Card className="mb-4">
        <CardContent>
          <motion.img
            key={animals[currentIndex].name}
            src={animals[currentIndex].image}
            alt={animals[currentIndex].name}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mx-auto h-48"
          />
          <p className="text-lg mt-2">¿Dónde vive el {animals[currentIndex].name}?</p>
          <div className="flex justify-center gap-4 mt-4">
            <Button onClick={() => handleChoice("dulce")}>Agua dulce</Button>
            <Button onClick={() => handleChoice("salada")}>Agua salada</Button>
          </div>
        </CardContent>
      </Card>

      <Progress value={progressPercent} className="mb-4" />
      <p>{feedback}</p>
    </div>
  );
}
