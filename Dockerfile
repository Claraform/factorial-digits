FROM python:3.9.5

# Set the working directory in the container
WORKDIR .

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies (numpy)
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY src/ .

# Set python script as entry point
ENTRYPOINT ["python3", "./factorial-digits.py"]

