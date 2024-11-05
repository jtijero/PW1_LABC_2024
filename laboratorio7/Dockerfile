FROM debian:latest
RUN apt-get update && \
    apt-get install -y perl apache2 curl libcgi-pm-perl && \ 
    a2enmod cgid && \
    apt-get clean
COPY search.cgi /usr/lib/cgi-bin/search.cgi
COPY image_search.cgi /usr/lib/cgi-bin/image_search.cgi
COPY index.html /var/www/html/index.html
COPY fondo.jpg /var/www/html/fondo.jpg
RUN chmod 755 /usr/lib/cgi-bin/*.cgi

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]

