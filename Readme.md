# Serial to Mqtt

Simple python script to handle JSON data coming from serial port, ie Arduino node, and forwarding to a MQTT broker.

    Connectig to MQTT broker: localhost:1883
    Published: {"lux": 300, "temp": 24.23, "press": 1021.2} Topic: iot/6001/o
    Published: {"lux": 307, "temp": 24.22, "press": 1021.12} Topic: iot/6001/o
    Published: {"lux": 299, "temp": 24.23, "press": 1021.21} Topic: iot/6001/o


Serial port and MQTT broker configuration is done by editing **config.json** file.

## Config.json structure:

    {
        "Broker": {
            "Host": "localhost",
            "Port": 1883,
            "ClientID": "clientID",
            "Topic" : ""
            "TopicPrefix": "prefix",
            "TopicSuffix": "suffix",
            "Qos": 0,
            "Cleansess": false
        },
        "Serial": {
            "Port": "/dev/ttyACM1",
            "Baudrate": 9600
        }
    }

## Serial data format and MQTT Topic selection

The handler expect to read standard JSON data from the serial port:

    {'lux': 305, 'temp': 24.17, 'press': 1021.24, 'id': 6001}

MQTT Topic can be specified in the **config.json** file.
It is possible to add prefixes and suffixes, *prefix/topic/suffix*.
For example: **iot/MySensorId/out**

If **Topic** is not specified in the configuration file, the handler
will look for a JSON field *id* and used its value.

    {'lux': 305, 'temp': 24.17, 'press': 1021.24, 'id': 6001}
    Topic: 6001

## Launching the script

By default **./config.json** is used.

    python serialToMqtt.py

Otherwise config file can be specified:

    python serialToMqtt.py my_config_file.json
