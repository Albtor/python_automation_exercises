import time
# import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# pip install RPi.GPIO
# pip install pyserial
# pip install paho-mqtt
# pip install flask
# pip install homeassistant

# Simulating Raspberry PI environment
# pip install RPi.GPIO paho-mqtt

def integrate_IOT():
    LIGHT_PIN = 17
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(LIGHT_PIN,GPIO.OUT)

    broker = "mqtt.eclipse.org"
    port = 1883
    topic = "home/temperature"
    TEMPERATURE_THRESHOLD = 25

    def on_connect(client, userdata, flag, response_code):
        print("Connected to MQTT broker with result code "+str(response_code))
    def on_message(client, userdata, msg):
        temperature = float(msg.payload.decode("utf-8"))
        print(f"Received temperature from MQTT broker: {temperature}ºC")
        if temperature > TEMPERATURE_THRESHOLD:
            print("Temperature is above threshold, Turning fan on")
            client.publish("home/fan", "ON")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message  = on_message
    client.connect(broker, port, 60)
    client.subscribe(topic)

    def control_light(command):
        if command == "ON":
            # GPIO.output(LIGHT_PIN, GPIO.HIGH)
            print("Light turned on")
        elif command == "OFF":
            # GPIO.output(LIGHT_PIN, GPIO.LOW)
            print("Light turned off")

    def monitor_temperature():
        while True:
            simulated_temperature = 25 + (time.time() % 10)
            print(f"Simulated temperature: {simulated_temperature}ºC")
            client.publish("home/temperature", simulated_temperature)
            time.sleep(5)

    if __name__ == "__main__":
        try:
            client.loop_start()
            control_light("ON")
            time.sleep(3)
            control_light("OFF")
            monitor_temperature()
        except KeyboardInterrupt:
            print("Shutting down")
            # GPIO.cleanup()
            client.loop_stop()
