#!/bin/bash -x
set -e

a2enmod rewrite expires

# Apache gets grumpy about PID files pre-existing
: "${APACHE_PID_FILE:=${APACHE_RUN_DIR:=/var/run/apache2}/apache2.pid}"
rm -f "$APACHE_PID_FILE"

source /etc/apache2/envvars && exec /usr/sbin/apache2 -DFOREGROUND "$@"
