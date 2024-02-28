FROM python:3.10-slim

# installieren der dependencies
RUN apt-get update && apt-get install -y \
    # Add any system dependencies here
    && rm -rf /var/lib/apt/lists/*

# working directory setzen
WORKDIR /app

# requirements file kopieren
COPY requirements.txt ./requirements.txt

# installieren der requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# main.py file kopieren
COPY main.py ./main.py
COPY finalized_model.pkl ./finalized_model.pkl

# port setzen
EXPOSE 7777

# app starten
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7777"]
