#Como poner invisible la contraseña por cmd
#Solo es valido si ejecuta el script por cmd
import getpass #mportamos la libreria que nos ayudará a poner invisible la contraseña

usuarios  = ["Yilver", "Juan", "Edilson", "Jair", "Winder", "Yefferson"]
passwords = ["123Y", "123J", "123E", "12J3"]

def comprobar_usuario(texto):
	return True if texto in usuarios else False


def comprobar_password(texto):
	return True if texto in passwords else False


def ingresar_credenciales():
	texto_usuario = input("Ingrese Nombre del Usuario\n|: ").title()
	texto_password = getpass.getpass("Ingrese Contraseña: ") #comando para ponerlo invisible
	return texto_usuario, texto_password


if __name__ == "__main__":
	texto_usuario, texto_password = ingresar_credenciales()
	if comprobar_usuario(texto_usuario) and comprobar_password(texto_password):
		print("Usuario Valido!")
	else:
		print("Usuario Invalido")