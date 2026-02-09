import sqlite3

class GestionBaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("comercio.sqlite")
        self.cursor = self.conexion.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute("""
            create table if not exists ventas (
                            id integer primary key autoincrement ,
                            cliente text,
                            fecha text,
                            ComboS int,
                            CombD int,
                            CombT int,
                            Postre int,
                            total real)
                            """)
        self.conexion.commit()

        self.cursor.execute("""
            create table if not exists registro (
                            id integer primary key autoincrement,
                            encargado text,
                            fecha_evento text,
                            evento text,
                            caja real)
                            """)
        self.conexion.commit()

    def insertar_venta(self, cliente, fecha, cant_s, cant_d, cant_t, cant_p, total):
        self.cursor.execute("""
            insert into ventas (cliente, fecha, ComboS, CombD, CombT, Postre, total)
            values (?, ?, ?, ?, ?, ?, ?)
            """, (cliente, fecha, cant_s, cant_d, cant_t, cant_p, total))
        self.conexion.commit()

    def insertar_registro(self, encargado, fecha_evento, evento, caja):
        self.cursor.execute("""
            insert into registro (encargado, fecha_evento, evento, caja)
            values (?, ?, ?, ?)
            """, (encargado, fecha_evento, evento, caja))
        self.conexion.commit()



