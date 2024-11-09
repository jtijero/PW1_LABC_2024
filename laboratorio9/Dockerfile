FROM debian:latest
RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-perl2 perl cpanminus && \
    cpanm CGI && \
    apt-get clean

EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]

