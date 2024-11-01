FROM debian:latest
RUN apt-get update && \
    apt-get install -y perl apache2 curl libcgi-pm-perl && \ 
    a2enmod cgid && \
    apt-get clean
COPY index.html /var/www/html/index.html
COPY calculadora.cgi /usr/lib/cgi-bin/calculadora.cgi
RUN chmod 755 /usr/lib/cgi-bin/calculadora.cgi
EXPOSE 80
CMD ¨=["apachectl","-D","FOREGRUND"]
