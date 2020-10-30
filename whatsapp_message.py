#Uso de libreria pywhatkit
import pywhatkit as wsp

#Variables de celular + mensaje 
phone = "+51980309999"
message = "Hola Brian, este es un mensaje indicando que ya puedes utilizar tu tarjeta virtual Edenred."
cantidad = 1
minute = 26
try:

	while cantidad <= 10:
		wsp.sendwhatmsg(phone,message, 00,minute + 1,5)
		print("Enviado a " + phone)
		cantidad +=1
		minute +=1
except:
	print("Error al enviar mensaje :(")
	