FROM python:3.8-slim-buster
Run mkdir /app
WORKDIR /app
ADD . /app/
RUN pip3 install -r requirement.txt
RUN useradd -m myapp
USER myapp
EXPOSE 4444
CMD ["python3", "/app/app.py"]
