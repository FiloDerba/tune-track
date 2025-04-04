# Python image
FROM python:3.11

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set working dir inside the container
WORKDIR /app

# This prevents rebuilding all requirements if they are not changed
# See https://stackoverflow.com/a/34399661
COPY setup.py /app
# This is to ensure first time setup will work.
RUN touch README.md
# Ensure pip and setuptools are up to date, in case the image is not
RUN pip install --upgrade pip setuptools
RUN pip install -e .

# Copy all local files to the container.
COPY . /app
