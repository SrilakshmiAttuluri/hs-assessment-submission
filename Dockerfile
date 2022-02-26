FROM python:3.8-slim-buster
WORKDIR /app
ADD requirement.txt .
RUN pip3 install -r requirement.txt
RUN useradd -m myapp
USER myapp
COPY . /app/
EXPOSE 4444
CMD ["python3", "/app/app.py"]
