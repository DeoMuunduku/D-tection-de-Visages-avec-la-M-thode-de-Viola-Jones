# -*- coding: utf-8 -*-
"""Detection de_1 visages avec la methode de Violas & Jone.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wYpER1jrOQ5ym39CPxDXxP_8wcUQuVSq
"""



"""## Detection de visages avec la methode de Violas & Jone
La methode de detection de visages de Violas & Jone, qui a bien explique en classe, est aussi
implemente dans OpenCV. Il y a la phase d’apprentissage et aussi la phase de détection. Pour la
première partie, je ne vous demande pas de faire apprendre un modèle de classification de visage/nonvisage. Vous pouvez utiliser les modèles qui sont pré-entraînés et fournis par les auteurs. Il y a des
modeles pour des visages frontaux, des visages de profile et aussi pour tous les types de visages.
Je vous demande d’evaluer cette methode pour la phase de detection:
- Choississez un modele de classification
- Evaluez la detection de visages avec la technique de sliding window. Il faut faire bien attention
à l’influence des parametres importantes sur la detection: la taille de la fenetre, la ratio de
overlap entre deux fenetres consecutives, ... Montrez de bons et mauvais results et essayez
d’expliquer les raisons.

# 1. Détection avec le classificateur frontal par défaut
"""



"""## avec plusieure visage"""

import cv2
from google.colab.patches import cv2_imshow

def detect_faces_variable_parameters(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Tester différentes tailles de fenêtres et ratios d'overlap
    size_options = [(30, 30),(25, 25),(40,40), (50, 50), (60, 60),(100, 100)]
    minNeighbors_options = [1,2, 3,4,5,6,7]  # Plus grande valeur, moins de fausses détections

    for size in size_options:
        for minNeighbors in minNeighbors_options:
            image_copy = image.copy()  # Utiliser une copie pour chaque test
            faces = face_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=minNeighbors, minSize=size
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(image_copy, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Afficher les résultats
            print(f"Taille de la fenêtre: {size}, MinNeighbors: {minNeighbors}, Nombre de visages détectés: {len(faces)}")
            cv2_imshow(image_copy)
            cv2.waitKey(0)  # Pause pour visualiser l'image

image_path = '/content/anua.jpeg'
detect_faces_variable_parameters(image_path)



"""## plusieure visage"""

