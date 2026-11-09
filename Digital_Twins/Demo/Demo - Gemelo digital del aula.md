---
tags: [demo, digital-twin, mqtt]
---
# Demo: gemelo digital del aula

Un sensor simulado de un aula envía CO₂, temperatura y humedad a un broker MQTT en la nube. Un dashboard web muestra los datos en directo y puede enviar el comando **Ventilar** de vuelta al sensor. Ese canal de vuelta es lo que lo convierte en un **gemelo digital** y no en una simple sombra digital (ver [[Bidirectional Data Loop (Closed-Loop Feedback)]]).

Coste: cero. Todo es open source o gratuito y no hace falta crear cuentas.

## Arquitectura

```
[sensor.py] --datos cada 2 s--> [Broker MQTT público] --datos--> [index.html]
     ^                          broker.hivemq.com                     |
     +------------------- comando "ventilar" / "parar" ---------------+
```

| Pieza | Archivo / servicio | Tecnología |
|---|---|---|
| Sensor simulado | `sensor.py` | Python + paho-mqtt |
| Broker en la nube | `broker.hivemq.com` (WebSockets seguros, puerto 8884) | MQTT público, sin registro |
| Dashboard | `index.html` | mqtt.js + Chart.js, en el navegador |

Topics:
- `uji-ccdt-podmanicacos/aula1/sensores`: lecturas en JSON (`co2`, `temp`, `hum`, `ventilando`, `ts`)
- `uji-ccdt-podmanicacos/aula1/comandos`: `ventilar` o `parar`

## Cómo ejecutarla

1. Instalar Python 3 y la librería (solo la primera vez):
   ```
   pip install paho-mqtt
   ```
2. Abrir una terminal en esta carpeta y arrancar el sensor:
   ```
   python sensor.py
   ```
   Debe aparecer `Conectado a broker.hivemq.com:8884` y una línea por lectura.
3. Abrir `index.html` con doble clic en el explorador de archivos (o desde GitHub Pages). El indicador de arriba a la derecha debe ponerse en verde y los datos empiezan a llegar.

Para abrirlo desde el móvil o desde otros ordenadores, publicad `index.html` en GitHub Pages. No hace falta tocar nada: el dashboard se conecta al broker desde cualquier sitio.

## Guion de la demo (unos 3 minutos)

1. Arrancar el sensor y enseñar la terminal: "esto es el aula física".
2. Enseñar el dashboard: "esto es su gemelo en la nube". Los datos llegan cada 2 segundos.
3. El CO₂ sube (aula llena, ventanas cerradas). Al pasar de 1000 ppm, salta la alerta roja (unos 30–40 s desde el arranque).
4. Pulsar **Ventilar**: la terminal muestra `Comando recibido: VENTILAR` y el CO₂ baja en directo.
5. Idea de cierre: si ese botón lo pulsara una regla automática o un modelo de IA, el gemelo pasaría de descriptivo a **prescriptivo**.

## Si algo falla

- **El dashboard no conecta**: la wifi del aula puede bloquear el puerto 8884. Probad con el hotspot del móvil.
- **El broker de HiveMQ está caído**: usad el de reserva en los dos lados.
  - Sensor: `python sensor.py --broker test.mosquitto.org --puerto 8081`
  - Dashboard: abrir `index.html?broker=wss://test.mosquitto.org:8081/mqtt`
- **Datos de otro grupo mezclados**: cambiad el topic en los dos lados.
  - Sensor: `python sensor.py --topic otro-nombre-unico/aula1`
  - Dashboard: `index.html?topic=otro-nombre-unico/aula1`
- Plan C: tened grabado un vídeo de la demo funcionando.

## Seguridad (para el bloque de retos)

El broker es público: cualquiera que conozca el topic puede leer los datos o enviar comandos. Vale para una demo, pero en un sistema real haría falta autenticación, TLS con certificados por dispositivo y control de acceso por topic, como hacen AWS IoT Core o Azure IoT Hub.
