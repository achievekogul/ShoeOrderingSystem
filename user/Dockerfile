FROM python:3.8
COPY requirements.txt /home/pingu/serviceorientedarchitecture/project/user/userdocker/requirements.txt
WORKDIR /home/pingu/serviceorientedarchitecture/project/user/userdocker
RUN pip install -r requirements.txt
COPY . /home/pingu/serviceorientedarchitecture/project/useruserdocker
ENTRYPOINT ["python"]
CMD ["app.py"]
