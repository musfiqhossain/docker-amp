FROM php:5.6-apache

COPY config/ /

RUN docker-php-ext-install pdo pdo_mysql

RUN yes | pecl install xdebug && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini

RUN docker-php-ext-install mysqli

EXPOSE 9000
