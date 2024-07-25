#!/bin/bash


cd frontend/monopoly
npm run build
cd ../../backend
rm -r static/*
cp -r ../frontend/monopoly/build/* static/
mv static/static/* static/
rm -r static/static




# Run the Flask app
flask run
