FROM python:3.10

RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app /app
EXPOSE 8080
RUN pip install pytest
# RUN  pytest
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]