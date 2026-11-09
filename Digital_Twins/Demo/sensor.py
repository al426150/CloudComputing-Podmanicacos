"""
Sensor simulado del gemelo digital de un aula (demo del seminario).

Publica cada 2 s las lecturas de CO2, temperatura y humedad en un broker
MQTT público y escucha comandos de vuelta desde el dashboard:
  - "ventilar": abre la ventilación, el CO2 empieza a bajar
  - "parar":    cierra la ventilación, el CO2 vuelve a subir

Uso:
    pip install paho-mqtt
    python sensor.py

Opciones (todas opcionales):
    python sensor.py --topic otro-topic-unico/aula1 --intervalo 1
"""

import argparse
import json
import random
import sys
import time

try:
    import paho.mqtt.client as mqtt
except ImportError:
    sys.exit("Falta la librería paho-mqtt. Instálala con:  pip install paho-mqtt")

# Broker público de HiveMQ por WebSockets seguros (puerto 8884).
# Es el mismo que usa el dashboard, así que si uno conecta, el otro también.
# Reserva si se cae: --broker test.mosquitto.org --puerto 8081
BROKER = "broker.hivemq.com"
PUERTO = 8884
TOPIC = "uji-ccdt-podmanicacos/aula1"

parser = argparse.ArgumentParser(description="Sensor simulado del aula")
parser.add_argument("--broker", default=BROKER)
parser.add_argument("--puerto", type=int, default=PUERTO)
parser.add_argument("--topic", default=TOPIC, help="prefijo de topic, debe ser único")
parser.add_argument("--intervalo", type=float, default=2.0, help="segundos entre lecturas")
parser.add_argument("--sin-tls", action="store_true", help="WebSockets sin cifrar (p. ej. un broker local)")
args = parser.parse_args()

TOPIC_SENSORES = f"{args.topic}/sensores"
TOPIC_COMANDOS = f"{args.topic}/comandos"

# Estado físico simulado del aula
estado = {"co2": 650.0, "temp": 21.5, "hum": 45.0, "ventilando": False}


def on_connect(client, userdata, flags, reason_code, properties=None):
    if str(reason_code) in ("0", "Success"):
        print(f"Conectado a {args.broker}:{args.puerto}")
        client.subscribe(TOPIC_COMANDOS)
        print(f"Publicando en  {TOPIC_SENSORES}")
        print(f"Escuchando en  {TOPIC_COMANDOS}\n")
    else:
        print(f"Error al conectar: {reason_code}")


def on_message(client, userdata, msg):
    comando = msg.payload.decode().strip().lower()
    if comando == "ventilar":
        estado["ventilando"] = True
        print(">>> Comando recibido: VENTILAR (abriendo ventilación)")
    elif comando == "parar":
        estado["ventilando"] = False
        print(">>> Comando recibido: PARAR (cerrando ventilación)")
    else:
        print(f">>> Comando desconocido: {comando!r}")


def simular_paso():
    """Avanza la simulación un paso y devuelve la lectura."""
    if estado["ventilando"]:
        # Entra aire de fuera: baja el CO2, refresca un poco y baja la humedad
        estado["co2"] -= random.uniform(25, 45)
        estado["temp"] -= random.uniform(0.02, 0.08)
        estado["hum"] -= random.uniform(0.1, 0.3)
    else:
        # Aula llena con la ventilación cerrada
        estado["co2"] += random.uniform(10, 30)
        estado["temp"] += random.uniform(0.0, 0.05)
        estado["hum"] += random.uniform(0.0, 0.15)

    estado["co2"] = max(420.0, min(estado["co2"], 2500.0))
    estado["temp"] = max(18.0, min(estado["temp"], 28.0))
    estado["hum"] = max(30.0, min(estado["hum"], 70.0))

    return {
        "co2": round(estado["co2"]),
        "temp": round(estado["temp"] + random.uniform(-0.1, 0.1), 1),
        "hum": round(estado["hum"] + random.uniform(-0.3, 0.3), 1),
        "ventilando": estado["ventilando"],
        "ts": time.time(),
    }


def crear_cliente():
    client_id = f"sensor-aula-{random.randint(1000, 9999)}"
    try:  # paho-mqtt 2.x
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id, transport="websockets")
    except AttributeError:  # paho-mqtt 1.x
        client = mqtt.Client(client_id=client_id, transport="websockets")
    client.ws_set_options(path="/mqtt")
    if not args.sin_tls:
        client.tls_set()
    client.on_connect = on_connect
    client.on_message = on_message
    return client


def main():
    client = crear_cliente()
    print(f"Conectando a {args.broker}:{args.puerto} ...")
    client.connect(args.broker, args.puerto, keepalive=30)
    client.loop_start()
    try:
        while True:
            lectura = simular_paso()
            client.publish(TOPIC_SENSORES, json.dumps(lectura))
            vent = "ON " if lectura["ventilando"] else "OFF"
            print(f"CO2 {lectura['co2']:>5} ppm | {lectura['temp']:>4} °C | "
                  f"{lectura['hum']:>4} % | ventilación {vent}")
            time.sleep(args.intervalo)
    except KeyboardInterrupt:
        print("\nSensor detenido.")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
