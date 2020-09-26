FROM python:3.8-buster

# Set application working directory
WORKDIR /usr/src/app

# Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install application
COPY . .

EXPOSE 8080

# Run application
# CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "${CONT_PORT}"]
CMD uvicorn app:app --reload --host 0.0.0.0 --port 8080
