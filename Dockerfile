# Use the official Python image with Playwright pre-installed
FROM mcr.microsoft.com/playwright/python:v1.40.0

# Set the working directory
WORKDIR /app

# Create a directory for screenshots
RUN mkdir -p screenshots

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install Playwright browsers (Chromium, Firefox, WebKit)
RUN playwright install
