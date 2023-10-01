# Compiler Stage
FROM python:3.9-slim as compiler
WORKDIR /app/

# Set up a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install project dependencies
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -Ur requirements.txt

# Runner Stage
FROM python:3.9-slim as runner
WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv

# Setting up environment
ENV PATH="/opt/venv/bin:$PATH"

# Copy project files
COPY . /app/

CMD ["python", "app.py"]
