Franco Zapata Ingenieria Informatica UM

Ajedrez por Franco Zapata

El repositorio contiene un programa que permite jugar una partida de ajedrez.
Para comenzar, los usuarios deben determinar quien jugará que color.
Por cada turno, el usuario podra elegir un movimiento de ajedrez, indicando fila y columna de la pieza a mover y la fila y columna destino. 
En caso de que el movimiento sea invalido, se debera reintroducir los valores.

# ajedrez-2024-francozapata05
ajedrez-2024-francozapata05 created by GitHub Classroom

# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-francozapata05/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-francozapata05/tree/main)

Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/fcb2a124e14b860c3f81/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-francozapata05/maintainability)

Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/fcb2a124e14b860c3f81/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-francozapata05/test_coverage)

# Funcionamiento con Docker
Para poner en funcionamiento el proyecto con Docker, se debe ejecutar los siguientes comandos:
    1. Intalar Docker
    # apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    2. Crear imagen de Docker
    # docker buildx build -t ajedrez . -- no-cache
    
    3. Ejecutar tests y jugar.
    # docker run -i ajedrez

