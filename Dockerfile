# Use official Python base image
FROM python:3.12-slim

# Install curl (used to install uv) and some system dependencies
# Install uv and move it to a directory in PATH
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv ~/.cargo/bin/uv /usr/local/bin/

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set working directory
WORKDIR /app

# Copy pyproject.toml and optionally poetry.lock/pdm.lock if you use them
COPY pyproject.toml ./

# Install dependencies using uv
RUN uv pip install --system --no-deps .

# Copy the rest of the code
COPY . .

# Command to run your app (adjust as needed)
CMD ["python", "main.py"]
