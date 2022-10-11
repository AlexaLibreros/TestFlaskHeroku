import sqlite3 as sql
from sqlite3 import Error
from werkzeug.security import check_password_hash

def crearBD():
    try:
        conn=sql.connect('usuarios.db')
        conn.commit()
        conn.close()
    except Error:
        print(Error)

def crearTabla():
    conn=sql.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE regUsuarios(
            name text,
            username text,
            email text primary key,
            password text
        )
    """
    )
    conn.commit()
    conn.close()

def insertarProducto(nombre, valor, cantidad):
    conn=sql.connect('inventario.db')
    cursor = conn.cursor()
    instruccion= f"INSERT INTO productos VALUES('{nombre}',{valor},{cantidad})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def registrarUsuario(name, username, email, password):
    conn=sql.connect('usuarios.db')
    cursor = conn.cursor()
    instruccion= f"INSERT INTO regUsuarios VALUES('{name}','{username}','{email}','{password}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insertarVariosProductos(listaProductos):
    conn=sql.connect('inventario.db')
    cursor = conn.cursor()
    instruccion = f"INSERT INTO productos VALUES(? ,? ,? )"
    cursor.executemany(instruccion, listaProductos)
    conn.commit()
    conn.close()

def leerValoresProductos():
    conn=sql.connect('inventario.db')
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM productos"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def actualizarProducto():
    conn=sql.connect('inventario.db')
    cursor = conn.cursor()
    instruccion = f"UPDATE productos SET valor=90000 WHERE nombre ='Audifonos'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def eliminarProducto():
    conn=sql.connect('inventario.db')
    cursor = conn.cursor()
    instruccion = f"DELETE FROM productos WHERE nombre = 'Audifonos'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

#LOGICA VALIDACION USUARIOS

def validarUsuario(email,password):
    conn=sql.connect('usuarios.db')
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM regUsuarios WHERE email ='{email}'"
    cursor.execute(instruccion)
    user=cursor.fetchone()
    # Se realiza captura del hash guardado en la base de datos
    capturarContrasena = user[3]
    # Se compara el hash de la base de datos con el que se crea a partir del formulario desde el cliente
    comparacionHashContrasena = check_password_hash(capturarContrasena, password)

    conn.commit()
    conn.close()
    if user is None or comparacionHashContrasena is False:
        return False
    else:
        return True

def usuarioSesionActual(usuarioActual):
    conn=sql.connect('usuarios.db')
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM regUsuarios WHERE email ='{usuarioActual}'"
    cursor.execute(instruccion)
    user=cursor.fetchone()
    conn.commit()
    conn.close()
    return(user)

# crearBD()
# crearTabla()
# registrarUsuario('Sergio','pixel','sergio@correo.com','pass123')
# insertarProducto('TV',12000000,32)


# INSERCION VARIOS ELEMENTOS
# productos=[
#     ("MiniComponente", 350000,2),
#     ("Lavadora", 850000 , 4)
# ]

# insertarVariosProductos(productos)

# datos=leerValoresProductos()
# primerArticulo=datos[0]
# print(primerArticulo[2])

# actualizarProducto()

# eliminarProducto()