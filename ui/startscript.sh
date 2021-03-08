#!/bin/sh

npm start &
cd api && flask run
