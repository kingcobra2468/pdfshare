FROM python:3.7

#Setup image
WORKDIR /PDFShare
COPY app/ /PDFShare
COPY requirements.txt /PDFShare
#Dependencies
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y poppler-utils

#Expose port 9000 of server
EXPOSE 9000

ENTRYPOINT ["python3"]
CMD ["main.py"]