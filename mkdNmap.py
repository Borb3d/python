#!/usr/bin/python3

import os, sys
import pathlib
import argparse


class bcolors:
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    WHITE = '\33[37m'
    GREY = '\33[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Variables Argumentos
parser = argparse.ArgumentParser(description='Crea carpetas y escanea al objetivo')

parser.add_argument("ip", help="Escribe la ip objetivo a analizar")
parser.add_argument("-o", help="Escribe el nombre del objetivo para crear las carpetas")

args = parser.parse_args()

#Variables
dirAct = pathlib.Path.cwd()




if args.o:
    print(bcolors.WARNING + "[*]" + bcolors.ENDC + bcolors.GREY + "Argumento opcional solicitado: -o" + bcolors.ENDC)
    print(bcolors.WARNING + "[!]" + bcolors.ENDC + bcolors.GREY + "Se van a crear las carpetas: "+ str(dirAct.joinpath(args.o, "nmap  "))+ "content  " + "exploits  " + "scripts" + bcolors.ENDC)
    try:
        os.makedirs(dirAct.joinpath(args.o, "nmap"))
        os.makedirs(dirAct.joinpath(args.o, "content"))
        os.makedirs(dirAct.joinpath(args.o, "exploits"))
        os.makedirs(dirAct.joinpath(args.o, "scripts"))
    except FileExistsError:
        opcion = input(bcolors.PURPLE + "Esta carpeta ya existe, ¿Está seguro que desea realizar el escaneo en la carpeta actual? s/n: " + bcolors.ENDC)
        if opcion == "s":
            print(bcolors.WARNING + "[*] Se va a realizar el escaneo en este mismo directorio" + bcolors.ENDC)
            print(bcolors.GREY + "[*]" + bcolors.ENDC + bcolors.GREEN + "Dirección ip objetivo: "+ args.ip + bcolors.ENDC + "\n" + bcolors.BOLD + "Comenzando el escaneo..." + bcolors.ENDC)
            #Sacar directorio destino
            scan = os.path.dirname(dirAct.joinpath(args.o, "nmap"))
            nmDir = scan + "/nmap"
            final = nmDir + "/allports"
            nm = os.system(f"nmap {args.ip} -p- --open -T5 -v -n -oG {final}")
            print(nm)
            exit()
        elif opcion == "n":
            print(bcolors.WARNING + "Modifique el nombre del objetivo y vuelva a lanzar el programa" + bcolors.ENDC + bcolors.FAIL + "\n Saliendo...")
            exit ()
        else:
            print(bcolors.FAIL + "No reconozco la opción elegida, saliendo del programa..." + bcolors.ENDC)
            exit ()
else:
    opcion = input(bcolors.PURPLE + "¿Está seguro que desea realizar el escaneo en la carpeta actual? s/n: " + bcolors.ENDC)
    if opcion == "s":
        print(bcolors.WARNING + "[*] No ha colocado ningún argumento opcional. \n[*] Se va a realizar el escaneo en este mismo directorio" + bcolors.ENDC)
        print(bcolors.GREY + "[*]" + bcolors.ENDC + bcolors.GREEN + "Dirección ip objetivo: "+ args.ip + bcolors.ENDC + "\n" + bcolors.BOLD + "Comenzando el escaneo..." + bcolors.ENDC)
        #os.mkdir("nmap")
        nmDir = os.path.dirname(dirAct.joinpath("nmap"))
        print(nmDir)
        final = nmDir + "/allports"
        print(final)
        nm = os.system(f"nmap {args.ip} -p- --open -T5 -v -n -oG {final}")
        print(nm)
        exit ()
    elif opcion == "n":
        print(bcolors.WARNING + "Por favor ingrese el nombre del objetivo colocando -o después de la ip objetivo" + bcolors.ENDC + bcolors.FAIL + "\n Saliendo...")
        exit ()
    else:
        print(bcolors.FAIL + "No reconozco la opción elegida, saliendo del programa..." + bcolors.ENDC)
        exit ()

if args.ip:
    #Sacar directorio destino
    scan = os.path.dirname(dirAct.joinpath(args.o, "nmap"))
    nmDir = scan + "/nmap"
    final = nmDir + "/allports"
    print(bcolors.GREY + "[*]" + bcolors.ENDC + bcolors.GREEN + "Dirección ip objetivo: "+ args.ip + bcolors.ENDC + "\n" + bcolors.BOLD + "Comenzando el escaneo..." + bcolors.ENDC)
    nm = os.system(f"nmap {args.ip} -p- --open -T5 -v -n -oG {final}")
    print(nm)