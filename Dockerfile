FROM python:3.9
WORKDIR /apps
COPY *.py ./
CMD ["python","./alert-manager.py"]
