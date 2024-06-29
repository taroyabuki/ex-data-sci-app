FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-glx fonts-ipaexfont

COPY app/ .

CMD ["python", "main.py"]