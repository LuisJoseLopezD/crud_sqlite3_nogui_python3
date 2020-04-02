# Ejercicio con base de datos

import sqlite3

db = 'testdb.db'

conn = sqlite3.connect(db)

def opciones():
	if resp == "1":
		print("Escriba el 'id' de la persona")
		id = input(">")
		print("Escriba el 'nombre' de la persona")
		name = input(">")
		print("Escriba la 'opcion' de la persona")
		opcion = input(">")
		filaAdd = (id, name, opcion)
		c = conn.cursor()
		c.execute("INSERT INTO test_table VALUES(?, ?, ?)", filaAdd)
		conn.commit()
		print("Registro nuevo agregado.")
		conn.close()

	elif resp == "2":
		c = conn.cursor()
		c.execute("SELECT * FROM test_table")
		fila = c.fetchall()
		print(fila)
		conn.close()

	elif resp == "3":
		print("Escriba el 'id' de la persona")
		id = input(">")
		c = conn.cursor()
		c.execute("SELECT * FROM test_table WHERE id =?",id)
		fila = c.fetchone()
		print(fila)
		print("Actualizar el registro:")
		print("Escriba el 'nombre' de la persona para actualizar")
		name = input(">")
		c = conn.cursor()
		c.execute("UPDATE test_table SET nombre=? WHERE id=?", (name,id))
		print("Escriba la 'opcion' de la persona para actualizar")
		opcion = input(">")
		c.execute("UPDATE test_table SET opcion=? WHERE id=?", (opcion,id))
		conn.commit()
		print("Registro Actualizado")
		conn.close()

	elif resp == "4":
		print("Escriba el 'id' de la persona")
		id = input(">")
		c = conn.cursor()
		c.execute('DELETE FROM test_table WHERE id =?',id)
		conn.commit()
		print("Registro Borrado")
		conn.close()
	else:
		print("No seleccionó la opción correcta")	


print("Bievenido a la base de datos")
print("1. Crear nuevo registro en la base de datos")
print("2. Mostrar la base de datos")
print("3. Actualizar o modificar la base de datos")
print("4. Eliminar registro de la base de datos")
print("Escriba 1,2,3 o 4 para ejecutar")
resp = input(">")
opciones()


# Commit: Consolidar, confirmar​ o hacer un commit se refiere,
# en el contexto de la ciencia de la computación y la gestión de datos,
# a la idea de confirmar un conjunto de cambios provisionales de forma permanente.
# Un uso popular es al final de una transacción de base de datos.