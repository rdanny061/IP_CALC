data = {
    'ip': [],
    'class':'',
    'defaultMask':'',
    'net':'',         #porción de red
    'host': '',       #porción de host
    'firstNet': '',   #primera direccion disponible
    'lastNet': '',    #ultima direccion disponible
    'netDir': '',     #direción de red
    'broadcast': '',  #direción de difución
}
while True:
    print("")
    ip = input("Ingrese la IP a analizar en formato decimal: ")
    if(len(ip.split(".")) != 4):
        print("Debe ingresar correctamente la ip.")
    else:
        ip = ip.split(".")
        data['ip'] = ip
        if(int(ip[0]) >= 1 and int(ip[0]) <= 127):
            #Definición de clase
            data['class'] = 'A'

            #Definición de máscara
            data['defaultMask'] = '255.0.0.0'

            #Definicoón de porción de máscara y host
            data['net'] = ip[0]
            data['host'] = ip[1] + "." + ip[2] + "." + ip[3]

            #Dirección de red
            data['netDir'] = ip[0] + ".0.0.0"

            #Primera dirección disponible
            data['firstNet'] = ip[0] + ".0.0.1"

            #última dirección disponible
            data['lastNet'] = ip[0] + ".255.255.254"

            #Broadcast
            data['broadcast'] = ip[0] + ".255.255.255"               
        elif(int(ip[0]) >= 128 and int(ip[0]) <= 191):
            #Definición de clase
            data['class'] = 'B'

            #Definición de máscara
            data['defaultMask'] = '255.255.0.0'

            #Definicoón de porción de máscara y host
            data['net'] = ip[0] + "." + ip[1]
            data['host'] = ip[2] + "." + ip[3]

            #Dirección de red
            data['netDir'] = ip[0] + "." + ip[1] + ".0.0"

            #Primera dirección disponible
            data['firstNet'] = ip[0] + "." + ip[1] + ".0.1"

            #Ultima dirección disponible
            data['lastNet'] = ip[0] + "." + ip[1] + ".255.254"

            #Broadcast
            data['broadcast'] = ip[0] + "." + ip[1] + ".255.255"
        elif(int(ip[0]) >= 192 and int(ip[0]) <= 223):
            #Definición de clase
            data['class'] = 'C'

            #Definición de máscara
            data['defaultMask'] = '255.255.255.0'

            #Definicoón de porción de máscara y host
            data['net'] = ip[0] + "." + ip[1] + "." + ip[2]
            data['host'] = ip[3]

            #Dirección de red
            data['netDir'] = ip[0] + "." + ip[1] + "." + ip[2] + ".0"

            #Primera dirección disponible
            data['firstNet'] = ip[0] + "." + ip[1] + "." + ip[2] + ".1"

            #Ultima dirección disponible
            data['lastNet'] = ip[0] + "." + ip[1] + "." + ip[2] + ".254"

            #Broadcast
            data['broadcast'] = ip[0] + "." + ip[1] + "." + ip[2] + ".255"
        elif(int(ip[0]) >= 224 and int(ip[0]) <= 239):
            #Definición de clase
            data['class'] = 'D'
        elif(int(ip[0]) >= 240 and int(ip[0]) <= 255):
            #Definición de clase
            data['class'] = 'E'

        print("")
        print("*******************************************************************************")
        print("*********************************** IP CALC ***********************************")
        print("*******************************************************************************")
        print("")	
        if(data['class'] == 'D' or data['class'] == 'E'):
            print("             Ip ingresda: " + ip[0] + "." + ip[1]+ "." + ip[2] + "." + ip[3]) 
            print("             Clase: ", data['class'])
        else:
            print("             Ip ingresda: " + ip[0] + "." + ip[1]+ "." + ip[2] + "." + ip[3]) 
            print("             Clase: ", data['class'])
            print("             Máscara: ", data['defaultMask'])
            print("             Segmento de red: ", data['net'])
            print("             Segmento de host: ", data['host'])
            print("             Dirección de red: ", data['netDir'])
            print("             Primera dirección disponible: ", data['firstNet'])
            print("             Última dirección disponible: ", data['lastNet'])
            print("             Dirección de broadcast: ", data['broadcast'])
        print("")
        print("*******************************************************************************")
        print("** Brandon Cruz **************** Rebeca Bolaños **************** Danny Rojas **")
        print("*******************************************************************************")