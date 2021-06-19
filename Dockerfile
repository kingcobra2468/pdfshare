FROM python:3.7

#Setup image
COPY requirements.txt /root/
#Dependencies
RUN pip3 install -r root/requirements.txt
RUN apt-get update && apt-get install -y poppler-utils gunicorn && useradd -m server

WORKDIR /home/server
COPY pdfshare/ /home/server
RUN chown -R server:server /home/server
USER server
#Expose port 9000 of server
EXPOSE 9000

CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]