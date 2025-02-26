FROM python:3.11-bullseye

# Open port 8000 for http service

ENV FAST_API_PORT=8000
EXPOSE 8000

# Install dependencies

COPY \*.py .
COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Install models

RUN python3 install_models.py

# Start the FASTAPI server

CMD python3 run.py