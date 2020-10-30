import pywhatkit as wsp
phone = "+51980309999"
message = "Hola Brian, este es un mensaje indicando que ya puedes utilizar tu tarjeta virtual Edenred."
try:
	wsp.sendwhatmsg(phone,message, 23,45)
	print("Enviado")
except:
	print("Error al enviar mensaje :(")
	