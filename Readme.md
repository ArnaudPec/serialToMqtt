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
            "TopicPrefix": "prefix",
            "TopicSuffix": "suffix",
            "qos": 0,
            "cleansess": false
        },
        "Serial": {
            "Port": "/dev/ttyACM1",
            "Baudrate": 9600
        }
    }

## Launching the script

By default **./config.json** is used.

    python serialToMqtt.py

Otherwise config file can be specified:

    python serialToMqtt.py my_config_file.json
