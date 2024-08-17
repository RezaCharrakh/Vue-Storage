FROM python:3.10.4

# Allows docker to cache installed dependencies between builds
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the entire project into the Docker image
COPY . /code

# Set the working directory to the project directory
WORKDIR /code

# Expose the port that the Django app runs on
EXPOSE 8000

# Define the entry point to run the Django development server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
