import os
import time


def cambiar(numero):
    num=numero
    asp=str(num)
    nomb=asp+".png"
    os.rename("/home/dav/Documentos/popo.png",nomb)
    