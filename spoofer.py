import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email import Encoders

# Limpiando la pantalla con el comando "cls" de windows (si te encuentras en un SO basado en unix cambiarlo a "clear")
os.system('cls')
print "-"*62
print " "*27+"SPOOFER"
print "-"*62

print
print "."*28+" INFO "+"."*28
print "- Este programa enviara mensajes a traves de spoofing\n  a cualquier direccion."
print "- Se necesita tener una cuenta en SMTP2GO."
print "- Solamente puedes enviar email a 1 direccion,\n  por razones de seguridad."
print "- Puedes escoger entre adjuntar un archivo (*.txt/*.html)\n  o escribir el mensaje desde la consola."
print "- Para indicar un fin de linea debes escribir \\n ."
print "- Esto fue elaborado solamente por razones educativas\n  para el canal de yt kjchints."
print "."*62+"\n\n"

def check(mail):
  delimiter = '@' in mail
  if delimiter == False:
	  print "Oops :^(, es este un email valido?."
	  print "Revisa el \'@\' y el \'.\' en el email."
	  print "Intenta de nuevo!"
	  exit()

def email_option_body(msg):
	option = 0
	while True:
		print "\n1. Adjuntar archivo (*.txt/*.html)"
		print "\n2. Escribir mensaje manualmente\n\n"
		try:
			option = int(raw_input("Elige una opcion: "))
		except ValueError:
			raw_input("\nLo siento, no entendi eso :c\n")
			continue
		else:	
			if option != 1 and option != 2:
				continue
			if option == 1:
				file_path = raw_input("Ruta de archivo con extension: ")
				if ".txt" in file_path:
					file = open(file_path, 'r')
					msg.attach(MIMEText(file.read()))
					file.close()
					break
				elif ".html" in file_path:
					file = open(file_path, 'r')
					msg.attach(MIMEText(file.read(), 'html'))
					file.close()
					break
				else:
					raw_input("Archivo invalido! Extensiones validas *.txt, *.html")
					continue
			else:
				data = raw_input("Escribe el mensaje\n ")
				msg.attach(MIMEText(data))
				break


raw_input("Presiona ENTER para continuar :^)")

print "\n\nLlena los datos solicitados\n"
print "FROM -> ",
mail_f = raw_input()
check(mail_f)
print "TO -> ",
mail_t = raw_input()
check(mail_t)

print
print "SUBJECT -> ",
sub = raw_input()

msg = MIMEMultipart()
msg['From'] = mail_f
to = []
msg['To'] = to.append(mail_t)
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = sub

email_option_body(msg)
print "*"*35

# Agrega aqui el ID y PASSWORD de SMPT2GO
# --> www.SMTP2GO.com
ID = "id" #Tu user ID
PASS = "clave" #Tu Clave

# Enviar email
try:
	server = smtplib.SMTP("smtpcorp.com", 2525)
	server.ehlo()
	server.starttls()
	server.login(ID,PASS)
	server.sendmail(mail_f, mail_t, msg.as_string())
	server.close()
	print "Whoa! Email enviado satisfactoriamente!"
except smtplib.SMTPException:
	print "Error:\n Oops! Hubo un error al tratar de mandar el email."
	print "Por favor revisa todos los detalles."