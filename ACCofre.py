import paho.mqtt.client as mqtt

rm = 11111

def ao_conectar(client, userdata, flags, rc):
    print("Servidor Contectado")
    cliente.subscribe(str(rm))

def ao_receber(client, userdata, msg):
    if (str(rm) in msg.topic):
        print(f"{msg.topic} --- {str(msg.payload)} ")

cliente = mqtt.Client()
cliente.on_connect = ao_conectar
cliente.on_message = ao_receber
cliente.connect("broker.hivemq.com", 1883, 60)
cliente.subscribe("cofre")
cliente.loop_start()
while True:
    cliente.publish("cofre", str(rm) + ": " + input("Envie uma mensagem: "))
cliente.loop_finish()
