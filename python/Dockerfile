# Use an official Python image as a base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt (if you have dependencies)
COPY requirements.txt .

# Install any dependencies from requirements.txt (if applicable)
RUN pip install --no-cache-dir -r requirements.txt

# Make sure the container stays alive. We can use a simple sleep command or use a long-running process like `tail -f`.
# The `tail -f` command keeps the container alive by reading the log indefinitely.
CMD ["tail", "-f", "/dev/null"]
