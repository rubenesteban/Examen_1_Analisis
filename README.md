# Examen_1_Analisis
1. Script 1.py

Se extraen todos los tweets relacionados con: bicicleatas, monopatin, ventadebicicleta, tallerdebicicletas.
Se estable una conexión con el gestor de bases de datos CouchDB.
Y se guardan los tweets en la base datos "venta-bici" como archivos json.
2. Script 2.py

Se extraen los campos: title, detail, location y price, del sitio web https://listado.mercadolibre.com.ec/bicicletas-ciclismo
Se forman los archivos json con los datos obtenidos.
Se estable una conexión con el sistema MongoDB.
Y se guardan los datos en la colección "venta-bici" de la base datos "bicicletas".
3. Script 3.py

Se extraen los datos de la analitica de la inmobiliaria "idealista" de Facebook.
Se estable una conexión con el sistema MongoDB.
Y se guardan los datos en la colección "en_ventabici" de la base datos "bicicletas".
4. Script 4.py

Se crea la base de datos "examen.db" en SQLite.
Se accede a la bd "bicicletas.db", se crea la tabla "en_venta" y se ingresan datos referentes a ventas de casas y departamentos (con los campos: id, title, location y price).
Se accede a los datos de la tabla definiendo el id como index del dataframe.
Se transforman a archivo json.
Se estable una conexión con el sistema MongoDB.
Y se guardan los datos en la colección "venta-bici" (donde ya existian documentos previos - Script 2) de la base datos "bicicletas".
