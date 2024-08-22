FROM python:3.13-rc-bookworm
COPY . . 
CMD ["python","./hello.py"]