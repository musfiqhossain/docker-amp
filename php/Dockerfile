FROM ubuntu:16.04
MAINTAINER Musfiq Hossain <only.musfiq@gmail.com>

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y \
      apache2 \
      php7.0 \
      php7.0-dev \
      php7.0-cli \
      libapache2-mod-php7.0 \
      php7.0-gd \
      php7.0-json \
      php7.0-ldap \
      php7.0-mbstring \
      php7.0-mysql \
      php7.0-pgsql \
      php7.0-sqlite3 \
      php7.0-xml \
      php7.0-xsl \
      php7.0-zip \
      php7.0-soap \
      php-pear \
      pkg-config

COPY config/ /

#pdo
#pdo_mysql
#mysqli


RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf /var/lib/apt/lists/*


# Set Apache environment variables (can be changed on docker run with -e)
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
#ENV APACHE_SERVERADMIN admin@localhost
#ENV APACHE_SERVERNAME localhost
#ENV APACHE_SERVERALIAS docker.localhost
#ENV APACHE_DOCUMENTROOT /var/www







RUN yes | pecl install mongodb && echo "extension=$(find /usr/lib/php/20151012 -name mongodb.so)" > /etc/php/7.0/apache2/conf.d/mongo.ini

RUN echo "extension=$(find /usr/lib/php/20151012 -name mongodb.so)" > /etc/php/7.0/cli/conf.d/mongo.ini


#RUN yes | pecl install xdebug && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini


ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf
RUN a2enmod rewrite


EXPOSE 80

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
