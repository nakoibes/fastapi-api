FROM python:3.9
WORKDIR /home/patient-signature-service
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY core core
COPY app.py app.py
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
