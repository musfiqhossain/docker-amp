# docker-amp

This is meant to be run on existing linux machine.

APACHE
MYSQL
PHP
XDEBUG

docker-compose up --build


# go into desired directory, ie code directory
composer create-project symfony/framework-standard-edition mmi_symfony


# run in container for now

chmod 777 /var/www/html/mmi_symfony/var/cache/dev -R
chmod 777 /var/www/html/mmi_symfony/var/logs -R
chmod 777 /var/www/html/mmi_symfony/var/sessions/ -R
