FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app/

# Copy and install dependencies

COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose the backend port
EXPOSE 5000

# General App Configuration
ARG APP_NAME
ENV APP_NAME=${APP_NAME}

ARG DEBUG
ENV DEBUG=${DEBUG}

ARG ENV
ENV ENV=${ENV}

# Database Configuration
ARG DATABASE_URL
ENV DATABASE_URL=${DATABASE_URL}

ARG SQLALCHEMY_TRACK_MODIFICATIONS
ENV SQLALCHEMY_TRACK_MODIFICATIONS=${SQLALCHEMY_TRACK_MODIFICATIONS}

# JWT Configuration
ARG JWT_SECRET_KEY
ENV JWT_SECRET_KEY=${JWT_SECRET_KEY}

# Default Admin Configuration
ARG ADMIN_USER
ENV ADMIN_USER=${ADMIN_USER}

ARG ADMIN_EMAIL
ENV ADMIN_EMAIL=${ADMIN_EMAIL}

# Blacklist Configuration
ARG JWT_BLACKLIST_ENABLED
ENV JWT_BLACKLIST_ENABLED=${JWT_BLACKLIST_ENABLED}

ARG JWT_BLACKLIST_TOKEN_CHECKS
ENV JWT_BLACKLIST_TOKEN_CHECKS=${JWT_BLACKLIST_TOKEN_CHECKS}

# Swagger Configuration
ARG SWAGGER_URL
ENV SWAGGER_URL=${SWAGGER_URL}

ARG API_URL
ENV API_URL=${API_URL}

# Set entrypoint
CMD ["python", "run.py"]
