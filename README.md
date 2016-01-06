# geiger-counter
Simple Python script for "Arduino compatible" geiger counter on Raspberry Pi - outputs to Collectd format

Requires RPi.GPIO:

sudo apt-get install python-rpi.gpio

Connect interrupt pin of Geiger counter to GPIO12 of RPi (configurable in script)

May need to run as root if /dev/gpiomem not available
