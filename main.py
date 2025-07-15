import requests
import json
import time
import os



os.system("cls")
print()
print("""  ___  _                   ___                
 | . \| |_  ___ ._ _  ___ / __> ___  ___ ._ _ 
 |  _/| . |/ . \| ' |/ ._>\__ \/ | '<_> || ' |
 |_|  |_|_|\___/|_|_|\___.<___/\_|_.<___||_|_|
                                              
""")
print("             Diseñado por Eltotiz")
print("              github.com/Eltotiz")
print()
print()
print("""   Nota: No añada espacios ni simbolos como "+" o/y "-" """)
print()
print()
number = input("  Inserte numero de telefono >> ") 
print() 
key = "YOUR_API_KEY"
url = "http://apilayer.net/api/validate?access_key=" + key + "&number=" + number
response = requests.get(url) 
answer = response.json() 
time.sleep(1)
print() 
if answer["valid"] == True:
	os.system("cls")
	print("""  ___  _                   ___                
 | . \| |_  ___ ._ _  ___ / __> ___  ___ ._ _ 
 |  _/| . |/ . \| ' |/ ._>\__ \/ | '<_> || ' |
 |_|  |_|_|\___/|_|_|\___.<___/\_|_.<___||_|_|
                                              
""")
	print("             Diseñado por Eltotiz")
	print("              github.com/Eltotiz")
	print()
	print()
	print("     Checkeando Numverify API...") 
	print("______________________________________________________________")
	print("|   [!] Numero Telefonico:",answer["number"])
	print("|")
	print("|   [!] Formato Internacional:",answer["international_format"])
	print("|")
	print("|   [!] Prefix del Pais:",answer["country_prefix"])
	print("|") 
	print("|   [!] Nombre del Pais:",answer["country_name"])
	print("|")
	print("|   [!] Localizacion:",answer["location"])
	print("|")
	print("|   [!] Carrier:",answer["carrier"])
	print("|")
	print("|   [!] Tipo de Linea:",answer["line_type"])
	print("|______________________________________________________________")
	print()
	print()
	print("        Escaneo finalizado.")
else:
	os.system("cls")
	print("""  ___  _                   ___                
 | . \| |_  ___ ._ _  ___ / __> ___  ___ ._ _ 
 |  _/| . |/ . \| ' |/ ._>\__ \/ | '<_> || ' |
 |_|  |_|_|\___/|_|_|\___.<___/\_|_.<___||_|_|
                                              
""")
	print("             Diseñado por Eltotiz")
	print("              github.com/Eltotiz")
	print()
	print()
	print("     Checkeando Numverify API...")
	print()
	print()
	print("   Numero invalido.")
