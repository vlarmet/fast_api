#!/bin/bash

# Mise à jour des paquets
sudo apt-get update

# Installation des dépendances
sudo apt-get -y install curl
sudo apt-get install libgomp1

gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app