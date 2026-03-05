# Step 1: Use a lightweight Python base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /security_tools

# Step 3: Copy your script from your laptop to the container
COPY pass_gen.py .

# Step 4: Run the script when the container starts
CMD ["python", "pass_gen.py"]