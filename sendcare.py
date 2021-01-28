#Projeto SendCare | NTA - Ufes.
#Agradecimentos à FAPES pelo apoio financeiro.

import serial
import time
import struct
 
#-------Iniciando comunicação serial-------------------
 
ser = serial.Serial('/dev/ttyUSB0', 115200)
 
ser.write(b'at\r\n')
a = 1
while a > 0:
    time.sleep(0.1)
    a = ser.inWaiting()
    if a > 0:
        #a
        b = ser.readline()
        print (b.decode("utf-8"))
'''
#Teste de conexao
ser.write(b'AT+CREG=1\r\n')
a = 1
while a > 0:
    time.sleep(0.5)
    a = ser.inWaiting()
    if a > 0:
        b = ser.readline()
        print (b.decode("utf-8"))
'''        
 
#-------Verificar registro na rede----------------------
print("Verificando registro na rede:")
ser.write(b'AT+CREG?\r\n') ## AT+CREG -> verificar registro na rede. 1,1 = Está conectado.
a = 1
while a > 0:
    time.sleep(0.1)
    a = ser.inWaiting()
    if a > 0:
        b = ser.readline()
        print (b.decode("utf-8"))
 
 
#-------Enviando Mensagem-------------------------------
'''
ser.write(b'AT+CMGF=1\r\n') ## AT+CMFG -> modo Texto
a = 1
while a > 0:
    time.sleep(0.5)
    a = ser.inWaiting()
    if a > 0:
        b = ser.readline()
        print (b.decode("utf-8"))
 
 
ser.write(b'AT+CMGS=\"998010116\"\r\n') ## Numero de destino
time.sleep(0.1)
ser.write(b'teste\r\n') #Mensagem a ser enviada
ser.write(struct.pack('>B',26)) #Caractere 26 para envio da mensagem.
a = 1
while a > 0:
    time.sleep(0.5)
    a = ser.inWaiting()
    if a > 0:
        b = ser.readline()
        print (b.decode("utf-8"))
 
'''
 
#-------Ler mensagem--------------------------------
'''
ser.write(b'AT+CMGD=1,4\r\n') ## Deleta mensagem mensagem.
a = 1
while a > 0:
    time.sleep(0.5)
    a = ser.inWaiting()
    if a > 0:
        b = ser.readline()
        print (b.decode("utf-8"))       
'''
 
ser.write(b'AT+CMGR=1\r\n') ## Deleta mensagem mensagem.
a = 1
c = ''
while a > 0:
    time.sleep(0.1)
    a = ser.inWaiting()
    if a > 0:
        b = ser.readline()
        print (b.decode("utf-8"))
        c = c + b.decode("utf-8")
    
#-------Extraindo texto--------------------------------
 
print(c)
 
p = c.find('@',0,-1)
 
print("agora_vai:")
 
print(p)
 
print("Bolado:")
print(c[p+2:-10])