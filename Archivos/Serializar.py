import pickle

info = [35, 88, 3.14, 16]

with open("./Archivos/ArchivoSerial", "wb") as binFile:
    pickle.dump(info, binFile)

print("Archivo binario creado!")

with open("./Archivos/ArchivoSerial", "rb") as binFile:
    lista = pickle.load(binFile)
    print(lista)

print("Archivo binario leído y reconstruido.")