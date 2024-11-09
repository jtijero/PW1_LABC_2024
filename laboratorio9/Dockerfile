FROM debian:latest
RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-perl2 perl cpanminus locales && \
    apt-get install -y libwww-perl && \
    cpanm CGI && \
    apt-get clean

RUN a2enmod cgi
RUN mkdir -p /usr/lib/cgi-bin/ /var/www/html/

COPY ./cgi-bin/busquedaU.cgi /usr/lib/cgi-bin/busquedaU.cgi
COPY ./public/index.html /var/www/html/index.html
COPY ./public/universidades_utf8.csv /usr/lib/cgi-bin/universidades_utf8.csv

# Configurar permisos para el script CGI
RUN chmod +x /usr/lib/cgi-bin/busquedaU.cgi

EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]

