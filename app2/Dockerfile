FROM tiangolo/uwsgi-nginx-flask

# Create app directory
WORKDIR /usr/src/adhisapp


COPY app.py .

EXPOSE 3000
RUN pip install requests
CMD [ "python", "app.py" ]
