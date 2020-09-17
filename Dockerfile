FROM python:3.7-alpine
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install ipython
CMD ["python3", "/src/main.py"]
