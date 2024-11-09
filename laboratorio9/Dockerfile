FROM debian:latest
RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-perl2 perl cpanminus locales && \
    apt-get install -y libwww-perl && \
    cpanm CGI && \
    apt-get clean

# Generar locales y establecer la configuración de UTF-8
RUN echo "es_ES.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=es_ES.UTF-8

# Configurar variables de entorno para UTF-8
ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES:es
ENV LC_ALL es_ES.UTF-8

RUN a2enmod cgi
RUN mkdir -p /usr/lib/cgi-bin/ /var/www/html/
COPY ./cgi-bin/busquedaU.cgi /usr/lib/cgi-bin/busquedaU.cgi
COPY ./public/index.html /var/www/html/index.html
COPY ./public/universidades_utf8.csv /usr/lib/cgi-bin/universidades_utf8.csv

RUN chmod +x /usr/lib/cgi-bin/busquedaU.cgi

# Configurar Apache para manejar UTF-8
RUN echo 'AddDefaultCharset UTF-8' >> /etc/apache2/apache2.conf

EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]

