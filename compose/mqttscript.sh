## DOCS https://github.com/eclipse/mosquitto/blob/master/docker/2.0/docker-entrypoint.sh ##

#!/bin/ash
set -e

# Set permissions
user="$(id -u)"
if [ "$user" = '0' ]; then
	[ -d "/mosquitto" ] && chown -R mosquitto:mosquitto /mosquitto || true
fi

exec "$@"