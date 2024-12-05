#!/bin/bash

set -e

echo "Running in environment: $NODE_ENV"

npm install

if [ "$NODE_ENV" == "production" ]; then
  echo "Building for production..."
  npm run build
  echo "Starting production server..."
  npx serve -s dist -l 8080 # Matches your Docker ports
else
  echo "Starting development server..."
  npm run dev
fi
