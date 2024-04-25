import os
clear = lambda: os.system('cls')

import msvcrt

Opcion = -1
Opcion_Mod = -1

diccionari = {
    "xarxa": {
    "PESCA": "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o \
    rombal, anomenada malla. Són anomenades filats i, preferentment, arts.", \
    "TÈXTIL": "Teixit de les xarxes de pescar, fabricat amb torçal de cotó o amb fil d’abacà, de cànem, de \
    lli o, modernament, de niló.",
    },
    "informàtica": {
    "TECNOLOGIA": "Conjunt de ciències, tècniques o activitats relacionades amb el tractament \
    automatitzat de dades. Informàtica de gestió. Informàtica d’oficina.", \
    "NÚVOL": "Organització d’un sistema informàtic en què l’usuari fa ús de recursos i serveis de \
    processament i emmagatzematge de dades allotjats en servidors externs accessibles a través \
    d’internet.",
    },
    "acrònim": {
    "NOM": "Qualsevol abreviació formada amb lletres o segments inicials o finals extrets dels mots \
    que componen una frase, que és pronunciable com un mot ordinari; per exemple, radar, làser, UNESCO, \
    etc."
    },
}

listaDiccionario = list(diccionari.keys())

def menu():
    import os
    clear = lambda: os.system('cls')
    clear()
    print('\n   BIENVENIDO AL DICCIONARIO DINARMICO "El Libro de las Acepciones"    \n')
    print(" Que quieres hacer?\n")
    print(" 1: Añadir")
    print(" 2: Consultar")
    print(" 3: Modificar")
    print(" 4: Eliminar")
    print(" 5: Salir")
    Opcion = int(input("\n   Introduce una opcion: "))
    return Opcion

while Opcion != 5:
    Opcion = menu() 
    match Opcion:
        case 1:
            clear()
            print("Que palabra quieres añadir?")
            palabra = input("Añade una palabra: ")
            valor = input("Añade su descripción: ")
            diccionari.update({palabra:valor})
            print("\nHas añadido la palabra:",palabra,"\nCon la descripción:",valor )
            print("\nPresione una tecla para continuar...")
            msvcrt.getch()
        case 2:
            clear()
            iNum = 1
            print("Que palabra quieres consultar?")
            for i in diccionari.keys():
                print(iNum,":".format(iNum),i)
                iNum+=1
            palabra_clave = int(input("\nIngresa el número de la palabra que quieras consultar: "))
            palabra_seleccionada = list(diccionari.keys()) [palabra_clave - 1]
            print('\n{}: {}\n'.format(palabra_seleccionada, diccionari[palabra_seleccionada]))
            
            
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        case 3:
            clear()
            iNum = 1
            print("Que palabra quieres modificar?")
            for i in diccionari.keys():
                print(iNum,":".format(iNum),i)
                iNum+=1           
            palabra_clave = int(input("\nIngresa el número de la palabra que quieras modificar: "))
            palabra_seleccionada = list(diccionari.keys())[palabra_clave - 1]
            clear()
            while Opcion_Mod < 1 or Opcion_Mod > 2:
                print("1: La palabra clave")
                print("2: La descripción de la palabra")
                Opcion_Mod = int(input("\nQue quieres modificar? "))
            
            if Opcion_Mod == 1:
                palabra_modificada = input("\nEscribe la palabra modificada:")
                descripción = list(diccionari.values())[palabra_clave - 1]
                diccionari.pop(list(diccionari.keys())[palabra_clave - 1])
                entrada = {palabra_modificada:descripción}
                diccionari.update(entrada)
            else:
                descripción_modificada = input("\nEscribe la descripción modificada:")
                diccionari.update({list(diccionari.keys())[palabra_clave - 1]:descripción_modificada})
            Opcion_Mod = -1
           
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        case 4:
            clear()
            iNum = 1
            print("Que palabra quieres eliminar?")
            for i in diccionari.keys():
                print(iNum,":".format(iNum),i)
                iNum+=1 
            palabra_clave = int(input("\nIngresa el número de la palabra que quieras eliminar: "))
            palabra_seleccionada = list(diccionari.keys())[palabra_clave - 1]
            diccionari.pop(list(diccionari.keys())[palabra_clave - 1])
            
            print("Eliminaste la palabra",palabra_seleccionada)
            
            print("\nPresione una tecla para continuar...")
            msvcrt.getch()