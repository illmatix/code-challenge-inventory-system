# Use an official Node.js runtime as the base image
FROM node:18

# Set the working directory inside the container
WORKDIR /app/

# Copy the package.json and package-lock.json to leverage Docker cache
COPY package.json package-lock.json ./

# Install dependencies (if you want to cache this step)
RUN npm install

# Copy the rest of the application files
COPY . /app/

# Copy the entrypoint script and set executable permissions
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 5173
EXPOSE 8080

# General App Configuration
ARG APP_NAME
ENV APP_NAME=${APP_NAME}

ARG DEBUG
ENV DEBUG=${DEBUG}

ARG ENV
ENV ENV=${ENV}

ARG VITE_API_URL
ENV VITE_API_URL=${VITE_API_URL}

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
