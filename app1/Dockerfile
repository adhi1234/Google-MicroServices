FROM tiangolo/uwsgi-nginx-flask

# Create app directory
WORKDIR /usr/src/adhisapp


COPY gcloud_app.py .

EXPOSE 4444
RUN pip install requests
CMD [ "python", "gcloud_app.py" ]
