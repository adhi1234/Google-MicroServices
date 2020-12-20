FROM tiangolo/uwsgi-nginx-flask

# Create app directory
WORKDIR /usr/src/adhisapp


COPY app.py .

EXPOSE 8888
RUN pip install requests
CMD [ "python", "app.py" ]
