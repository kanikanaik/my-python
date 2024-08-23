FROM python:3.13-rc-bookworm
COPY . . 
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python","./hello.py"]