"""
File: serialToMqtt.py
Description: Simple json serial to Mqtt data forwarder
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import signal
import json
import pprint
import serial
import paho.mqtt.client as mqtt

s = serial.Serial()

def sigint_handler(signum, frame):
    print("Closing serial and exiting")
    s.close()
    sys.exit(0)

def configure_mqtt_client(config_mqtt):
    client = mqtt.Client(config_mqtt['ClientID'])
    client.connect(config_mqtt['Host'], config_mqtt['Port'])

    print("\nConnectig to MQTT broker: " + config_mqtt['Host'] \
            + ":" + str(config_mqtt['Port']))

    return client

def config_serial(config_serial):
    s.port = config_serial['Port']
    s.baudrate = config_serial['Baudrate']

def parse_config_file(argv):
    if len(argv) > 1:
        try:
            f = open(argv[1])
        except Exception as e:
            raise e
    else:
        try:
            f = open("config.json")
        except Exception as e:
            raise e
    try:
        config = json.loads(f.read())
    except Exception as e:
        raise e

    return config

if __name__ == "__main__":

    # Handling SIGINT
    signal.signal(signal.SIGINT, sigint_handler)

    # Parsing configuration
    config = parse_config_file(sys.argv)

    print(sys.argv[0] + " configuration:\n")
    pprint.pprint(config)

    # Serial port configuration
    config_serial(config['Serial'])

    # Opening serial port and flush the first bytes
    try:
        s.open()
    except Exception as e:
        raise e

    time.sleep(2)
    s.flush()

    # Configure MQTT client
    client = configure_mqtt_client(config['Broker'])
    client.loop_start()

    while True:
        try:

            # Reading and decoding data
            s_data = s.readline().decode()[:-2]
            data = json.loads(s_data)
            time.sleep(2)

            # Preparing MQTT topic and payload
            topic = config['Broker']['TopicPrefix'] + "/" + str(data['id']) \
                    + "/" + config['Broker']['TopicSuffix']

            data.pop('id', None)
            payload = json.dumps(data)

            # Publishing
            try:
                client.publish(topic, payload)
                print("Published: " + payload + " Topic: " + topic)
            except Exception as e:
                raise e

        except Exception as e:
            s.flush()

    s.close()
