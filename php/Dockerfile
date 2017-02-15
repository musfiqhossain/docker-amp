FROM ubuntu:16.04
MAINTAINER Musfiq Hossain <only.musfiq@gmail.com>

# Set Apache environment variables (can be changed on docker run with -e)
ENV APACHE_RUN_USER www-data \
    APACHE_RUN_GROUP www-data \
    APACHE_LOG_DIR /var/log/apache2 \
    APACHE_PID_FILE /var/run/apache2.pid \
    APACHE_RUN_DIR /var/run/apache2 \
    APACHE_LOCK_DIR /var/lock/apache2

RUN apt-get update && \
    apt-get -y install software-properties-common && \
    locale-gen en_US.UTF-8 && \
    export LC_ALL=en_US.UTF-8 && \
    export LANG=en_US.UTF-8 && \
    add-apt-repository ppa:ondrej/php && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install \
    apache2 \
    php7.1 \
    php7.1-dev \
    php7.1-cli \
    php7.1-gd \
    php7.1-json \
    php7.1-ldap \
    php7.1-mbstring \
    php7.1-mcrypt \
    php7.1-mysql \
    php7.1-xml \
    php7.1-xsl \
    php7.1-zip \
    php7.1-soap \
    libapache2-mod-php7.1 \
    php-pear \
    wget \
    pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pecl install mongodb && \
    pecl install xdebug
#RUN yes | pecl install mongodb && echo "extension=$(find /usr/lib/php/20160303 -name mongodb.so)" > /etc/php/7.1/apache2/conf.d/mongo.ini
COPY config /
ADD zf/*.tar.gz /
RUN sh /usr/local/bin/install.sh
WORKDIR /var/www/html
EXPOSE 80 9001
ENTRYPOINT bash -C '/entrypoint.sh';'bash'
