FROM python:3.11-slim
WORKDIR /LuciFlow

## Install all dependecies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

## Copy the app
COPY . .

## Expose Port
EXPOSE 5000

## Run
CMD ["python", "app.py"]



