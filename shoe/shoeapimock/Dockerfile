FROM python:3.8
COPY requirements.txt /user/requirements.txt
WORKDIR /user
RUN pip install -r requirements.txt
COPY . /user
ENTRYPOINT ["python"]
CMD ["app.py"]
