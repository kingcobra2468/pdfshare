FROM python:3.7

# Setup system
RUN useradd -m server
RUN apt-get update && apt-get install -y poppler-utils gunicorn
COPY backend/entrypoint.sh /home/server/
ADD backend/pdfshare/ /home/server/pdfshare
# Give execution permission to launcher script
RUN chmod +x /home/server/entrypoint.sh
RUN chown -R server:server /home/server

# Create user server
USER server
ENV PATH="/home/server/.local/bin:${PATH}"

# Install python dependencies
COPY requirements.txt /tmp

# Dependencies
RUN pip3 install -r /tmp/requirements.txt --user

# Move pdfshare onto image
WORKDIR /home/server

# Expose port 9000 of server
EXPOSE 9000

# Launches pdfbsd daemon and pdfshare
CMD ["/bin/bash", "-c", "./entrypoint.sh"]