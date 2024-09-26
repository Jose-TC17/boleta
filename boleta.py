# importanto la libreria de tkinter
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk # para poder crear el treeview

# colores
blanco = "#fff"
azul = "#16397A"


class Boleta:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Boleta de venta")
        self.ventana.geometry("500x700")
        self.ventana.resizable(0, 0)
        self.ventana.protocol("WM_DELETE_WINDOW", self.bloqueo_salir)
        self.ventana.iconbitmap('img/logotipo.ico')
    
    def inicio(self):

        # fondo
        self.fondo = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/fondo.png")
        self.insertarFondo = Label(image=self.fondo, text="inicio")
        self.insertarFondo.place(x=0, y=0, relheight=1, relwidth=1)
        
        # información importante: en el fondo hay un ruc lo cual ese ruc es invalido, no existe, 
        # solo son numeros aleatorios para dar estilo a la boleta de venta.
        
        # creando botones
        self.btnComenzar = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/comenzar.png")
        self.mostrarBtnComenzar = Button(self.ventana, image=self.btnComenzar, cursor="hand2", border=0, command=self.ventana_registros)
        self.mostrarBtnComenzar.place(x=150, y=350)
        
        # creando el boton de ajustes
        self.btnAjustes = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/ajustes.png")
        self.mostrarBtnAjustes = Button(self.ventana, image=self.btnAjustes, border=0, cursor="hand2", command=self.ajustes)
        self.mostrarBtnAjustes.place(x=150, y=430)
        
        # creando el boton de salir
        self.btnSalir = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/salir.png")
        self.mostrarBtnSalir = Button(self.ventana, image=self.btnSalir, border=0, cursor="hand2", command=self.salir)
        self.mostrarBtnSalir.place(x=150, y=510)
        
        self.ventana.mainloop()
        
    def ventana_registros(self):
        
        self.nombre_usuario = ""
        self.nombre_apellido = ""
        self.dni_usuario = 0
        self.correo_usuario = ""
        self.telefono_usuario = 0
        
        self.ventana.withdraw()
        
        self.ventana_registro = Toplevel(self.ventana)
        self.ventana_registro.geometry("500x700")
        self.ventana_registro.resizable(0, 0)
        self.ventana_registro.protocol("WM_DELETE_WINDOW", self.bloqueo_salir)
        self.ventana_registro.iconbitmap('img/logotipo.ico')
        
    
        self.fondo_registro = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/fondo-registro.png")
        self.mostrar_fondo_registro = Label(self.ventana_registro, image=self.fondo_registro)
        self.mostrar_fondo_registro.place(x=0, y=0, relwidth=1, relheight=1)
        
        # boton de regresar
        self.btn_regresar = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-regresar.png")
        self.mostrar_btn_regresar = Button(self.ventana_registro, image=self.btn_regresar, border=0, cursor="hand2", command=lambda: self.regresar(self.ventana_registro))
        self.mostrar_btn_regresar.place(x=25, y=40)
        
        # entradas de texto
        
        self.tipo_entrada_nombre = StringVar()
        self.entrada_nombre = Entry(self.ventana_registro, width=25, textvariable=self.tipo_entrada_nombre)
        self.entrada_nombre.place(x=250, y=215)
        
        self.tipo_entrada_apellido = StringVar()        
        self.entrada_apellido = Entry(self.ventana_registro, width=25, textvariable=self.tipo_entrada_apellido)
        self.entrada_apellido.place(x=250, y=295)
        
        self.tipo_entrada_DNI = IntVar()
        self.entrada_DNI = Entry(self.ventana_registro, width=25, textvariable=self.tipo_entrada_DNI)
        self.entrada_DNI.place(x=250, y=370)
        
        self.tipo_entrada_correo = StringVar()
        self.entrada_correo = Entry(self.ventana_registro, width=25, textvariable=self.tipo_entrada_correo)
        self.entrada_correo.place(x=250, y=445)
        
        self.tipo_entrada_telefono = IntVar()
        self.entrada_telefono = Entry(self.ventana_registro, width=25, textvariable=self.tipo_entrada_telefono)
        self.entrada_telefono.place(x=250, y=525)
        
        # boton de limpiar
        
        self.btn_limpiar = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/btn-limpiar.png")
        self.mostrar_btn_limpiar = Button(self.ventana_registro, image=self.btn_limpiar, border=0, cursor="hand2", command=self.limpiar_casillas)
        self.mostrar_btn_limpiar.place(x=30, y=640)
        
        # boton de registrar
        
        self.btn_registrar = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/btn-registrar.png")
        self.mostrar_btn_registrar = Button(self.ventana_registro, image=self.btn_registrar, border=0, cursor="hand2", command=self.obteniendo_datos_usuario)
        self.mostrar_btn_registrar.place(x=150, y=580)
        
        self.btn_ven_registro = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-ventana-producto.png")
        self.btn_ventana_registro = Button(self.ventana_registro, image=self.btn_ven_registro, border=0, cursor="hand2", command=self.ventana_operacion)
        self.btn_ventana_registro.place(x=270, y=640)     
        
        
    def ventana_operacion(self):
        
        try:
            if self.nombre_usuario != "" and self.apellido_usuario != "" and self.dni_usuario != 0:
                
                self.nombre_producto = ""
                self.cantidad_producto = 0
                self.precio_producto = 0.0
                
                self.ventana_registro.withdraw()
                self.ventana_operaciones = Toplevel(self.ventana)
                self.ventana_operaciones.geometry("500x700")
                self.ventana_operaciones.resizable(0, 0)
                self.ventana_operaciones.protocol("WM_DELETE_WINDOW", self.bloqueo_salir)
                self.ventana_operaciones.iconbitmap('img/logotipo.ico')
                
                
                
                # fondo de la ventana de registrar productos
                self.fondo_registroP = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/fondo-registroP.png")
                self.mostrar_fondo_registroP = Label(self.ventana_operaciones, image=self.fondo_registroP)
                self.mostrar_fondo_registroP.place(x=0, y=0, relwidth=1, relheight=1)    
                
                # boton regresar
                self.btn_regresar = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-regresar.png")
                self.mostrar_btn_regresar = Button(self.ventana_operaciones, image=self.btn_regresar, border=0, cursor="hand2", command=lambda: (self.ventana_registros(), self.ventana_operaciones.destroy()))
                self.mostrar_btn_regresar.place(x=25, y=40) 
                
                # entradas de datos
                self.tipo_entrada_nombreP = StringVar()
                self.entrada_nombreP = Entry(self.ventana_operaciones, width=25, textvariable=self.tipo_entrada_nombreP)
                self.entrada_nombreP.place(x=290, y=230)
                self.tipo_entrada_precioP = DoubleVar()
                self.entrada_precioP = Entry(self.ventana_operaciones, width=25, textvariable=self.tipo_entrada_precioP)
                self.entrada_precioP.place(x=290, y=315)
                self.tipo_entrada_cantidad = IntVar()
                self.entrada_cantidadP = Entry(self.ventana_operaciones, width=25, textvariable=self.tipo_entrada_cantidad)
                self.entrada_cantidadP.place(x=290, y=405)
                
                # entrada del total
                self.entrada_total = Label(self.ventana_operaciones, bg="#E75656", width=15)
                self.entrada_total.place(x=180, y=530)
                
                self.num_producto_registrado = Label(self.ventana_operaciones, bg="#83BCE4", width=15)
                self.num_producto_registrado.place(x=300, y=580)
                
                # botones registrar
                self.btn_registrarP = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-registrar-producto.png")
                self.mostrar_btn_registrarP = Button(self.ventana_operaciones, image=self.btn_registrarP, border=0, cursor="hand2", command=self.obteniendo_datos_producto)
                self.mostrar_btn_registrarP.place(x=150, y=460)
                
                self.dato_producto = []

                # botones del menu y del lista de productos
                self.btn_menu = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-menu-principal.png")
                self.mostrar_btn_menu = Button(self.ventana_operaciones, image=self.btn_menu, border=0, cursor="hand2", command=lambda: self.regresar(self.ventana_operaciones))
                self.mostrar_btn_menu.place(x=30, y=640)
                self.btn_listaP = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-lista-producto.png")
                self.mostrar_btn_listaP = Button(self.ventana_operaciones, image=self.btn_listaP, border=0, cursor="hand2", command=self.ventana_listaP)
                self.mostrar_btn_listaP.place(x=270, y=640)
            else:
                messagebox.showinfo("AVISO IMPORTANTE", """Antes de continuar por favor no dejes vacio el nombre, apellido y el dni, esos campos son obligatorios""")
                
        except:
            messagebox.showerror("ERROR DE ESCRITURA", """Por favor escriba correctamente los datos que se le esta solicitando""")

    def ventana_listaP(self):
        try:
            if self.nombre_producto == "" and self.precio_producto == 0.0 and self.cantidad_producto == 0:
                messagebox.showinfo("AVISO IMPORTANTE", """Por favor antes de continuar rellena los datos correctamente""")
            else:
                self.ventana_operaciones.withdraw()
                self.ventana_producto = Toplevel(self.ventana)
                self.ventana_producto.geometry("500x700")
                self.ventana_producto.resizable(0, 0)
                self.ventana_producto.protocol("WM_DELETE_WINDOW", self.bloqueo_salir)
                self.ventana_producto.iconbitmap('img/logotipo.ico')
                
                
                # fondo de la pantalla de lista productos
                self.fondo_ventana_producto = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/fondo-lista-producto.png")
                self.mostrar_fondo_ventanaP = Label(self.ventana_producto, image=self.fondo_ventana_producto)
                self.mostrar_fondo_ventanaP.place(x=0, y=0, relwidth=1, relheight=1)
                
                # boton regresar
                self.btn_regresar = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-regresar.png")
                self.mostrar_btn_regresar = Button(self.ventana_producto, image=self.btn_regresar, border=0, cursor="hand2", command=lambda: (self.ventana_operacion(), self.ventana_producto.destroy()))
                self.mostrar_btn_regresar.place(x=25, y=40) 
                
                # label del nombre del cliente
                self.label_nombre = Label(self.ventana_producto, bg="#83BCE4", text=f"{self.nombre_usuario} {self.apellido_usuario}", width=30)
                self.label_nombre.place(x=200, y=200)
                
                
                # crear el treeview
                self.columnas = ["Nombre", "Precio", "Cantidad", "Precio Total"] # creando las columnas de las tablas
                self.tabla = ttk.Treeview(self.ventana_producto, columns=self.columnas, show="headings") #creando un treeview
                for col in self.columnas:
                    self.tabla.heading(col, text=col)
                    self.tabla.column(col, width=100)
                self.tabla.place(x=50, y=250)
                
                for self.x in self.dato_producto:
                    self.tabla.insert("", "end", value=self.x)
                                    
                self.producto_precios_total = 0
                for self.i in self.dato_producto:
                    self.producto_precios_total+=self.i[-1]
                
                    
                # total de los productos
                self.resultado_productos_totales = Label(self.ventana_producto, text="{:.2f}".format(self.producto_precios_total), bg="#E75656", width=15)
                self.resultado_productos_totales.place(x=345, y=500)
                                                
                # botones
                self.boton_borrar = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-eliminar.png")
                self.mostrar_boton_borrar = Button(self.ventana_producto, image=self.boton_borrar, border=0, cursor="hand2", command=self.eliminar_producto)
                self.mostrar_boton_borrar.place(x=150, y=550)
                
                self.btn_menu = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-menu-principal.png")
                self.mostrar_btn_menu = Button(self.ventana_producto, image=self.btn_menu, border=0, cursor="hand2", command=lambda: self.regresar(self.ventana_producto))
                self.mostrar_btn_menu.place(x=30, y=620)
                
                self.btn_imprimir = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-imprimir.png")
                self.mostrar_btn_imprimir = Button(self.ventana_producto, image=self.btn_imprimir, border=0, cursor="hand2", command=self.imprimir)
                self.mostrar_btn_imprimir.place(x=270, y=620)
        except:
            messagebox.showinfo("AVISO IMPORTANTE", """Por favor antes de continuar rellena los datos correctamente""")
    
    def ajustes(self):
        
        self.ventana.withdraw()
        
        self.ventana_ajustes = Toplevel(self.ventana)
        self.ventana_ajustes.geometry("500x700")
        self.ventana_ajustes.resizable(0, 0)
        self.ventana_ajustes.protocol("WM_DELETE_WINDOW", self.bloqueo_salir)
        
        # fondo
        self.fondo_ajustes = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/fondo-ajustes.png")
        self.mostrar_fondo_ajustes = Label(self.ventana_ajustes, image=self.fondo_ajustes)
        self.mostrar_fondo_ajustes.place(x=0, y=0, relwidth=1, relheight=1)
        
        # boton de ajustes
        self.boton_menu_ajustes = PhotoImage(file="C:/Users/Jtc17/OneDrive/Desktop/proyectos/Proyecto boleta/img/boton-menu-principal.png")
        self.mostrar_btn_menuA = Button(self.ventana_ajustes, image=self.boton_menu_ajustes, border=0, cursor="hand2", command=lambda: self.regresar(self.ventana_ajustes))
        self.mostrar_btn_menuA.place(x=150, y=620)
        
    def obteniendo_datos_usuario(self):
        
        try:
            self.nombre_usuario = self.entrada_nombre.get()
            self.apellido_usuario = self.entrada_apellido.get()
            self.dni_usuario = int(self.entrada_DNI.get())
            self.correo_usuario = self.entrada_correo.get()
            self.telefono_usuario = int(self.entrada_telefono.get())
            self.contador_dni = len(str(self.dni_usuario))
            if self.nombre_usuario != "" and self.apellido_usuario != "" and self.dni_usuario != 0:
                if self.contador_dni != 8:
                    messagebox.showinfo("AVISO", """Vuelve a escribir tu DNI correctamente, recuerda son 8 digitos""")
                    self.dni_usuario = 0
                else:
                    self.contador_telefono = len(str(self.telefono_usuario))
                    # verificando si se ingreso un correo
                    if self.correo_usuario != "":
                        
                        if not "@" in self.correo_usuario:
                            messagebox.showerror("ERROR DE ESCRITURA", """Por favor no olvide poner el @ en el correo""")
                            self.correo_ingresado = self.correo_usuario
                            self.correo_ingresado = "No se registro correctamente el correo"
                        else:
                            self.correo_ingresado = self.correo_usuario
                    else:
                        self.correo_ingresado = self.correo_usuario
                        self.correo_ingresado = "No ingreso correo"
                    
                    if self.telefono_usuario != 0 and self.telefono_usuario != "":
                        if self.contador_telefono > 10:
                            messagebox.showerror("ERROR DE ESCRITURA", """Por favor para el numero de telefono solo tiene un maximo de 10 caracteres""")
                            self.telefono_ingresado = self.telefono_usuario
                            self.telefono_ingresado = "No se registro correctamente el telefono"
                        else:
                            self.telefono_ingresado = self.telefono_usuario
                    else:
                        self.telefono_ingresado = self.telefono_usuario
                        self.telefono_ingresado = "No ingreso número de telefono"
                    
                    messagebox.showinfo("REGISTRO REALIZADO", f"""Se registro el usuario como \nUsuario: {self.nombre_usuario} {self.apellido_usuario} \nDNI: {self.dni_usuario}""")
            else:
                messagebox.showinfo("AVISO IMPORTANTE", """Por Favor no dejes casillas vacias, ingresar datos obligatoriamente del nombre, apellido y el DNI""")
                
        except:
            messagebox.showerror("ERROR DE ESCRITURA", """Por favor escriba correctamente los datos solicitados""")
            
    def obteniendo_datos_producto(self):
        try:
            self.nombre_producto = self.entrada_nombreP.get()
            self.precio_producto = float(self.entrada_precioP.get())
            self.cantidad_producto = int(self.entrada_cantidadP.get())
            self.precio_total = self.precio_producto * self.cantidad_producto
            self.entrada_total.config(text="{:.2f}".format(self.precio_total))
            if self.nombre_producto == "" and self.cantidad_producto == 0 and self.precio_producto == 0.0:
                messagebox.showinfo("AVISO IMPORTANTE", """Por favor no dejes casillas vacias, ingresar los datos correctamente""")
            else:
                messagebox.showinfo("REGISTRO REALIZADO", f"""Se registro el producto correctamente. \nProducto: {self.nombre_producto} \nPrecio: {self.precio_producto} \nPor la cantidad de productos que fue {self.cantidad_producto} el resultado total del producto s/{self.precio_total}""")
                self.dato_producto.append((self.nombre_producto, self.precio_producto, self.cantidad_producto, self.precio_total))
                # contador del los productos
                self.count = 0
                for c in self.dato_producto:
                    self.count+=1
                self.num_producto_registrado.config(text=self.count)   
                
                self.entrada_nombreP.delete(0, END)         
                self.entrada_precioP.delete(0, END)       
                self.entrada_cantidadP.delete(0, END)       

        except:
            messagebox.showerror("ERROR DE ESCRITURA", """Por favor escriba correctamente los datos que se le esta solicitando""")
    
    def imprimir(self):
        
        print(f"""
            --------------------------------------------------
                            JOSST TECNOLOGY
            --------------------------------------------------
                            BOLETA DE VENTA
                         -- RUC: 91823173177 --
            --------------------------------------------------
            Información del usuario:

            Usuario: {self.nombre_usuario} {self.apellido_usuario}
            DNI: {self.dni_usuario}
            Correo: {self.correo_ingresado}
            Telefono: {self.telefono_ingresado}      
            --------------------------------------------------
            Productos registrados:
            """)
        self.count_prodc = 0
        if len(self.dato_producto) > 0:
            
            for i in self.dato_producto:
                self.count_prodc+=1
                print(f"""
            Producto{self.count_prodc}:
            ----------------------------------------------
            Nombre Producto: {i[0]}
            Precio:{i[1]}
            Cantidad Producto: {i[2]}
            Precio Total del Producto: {i[3]}
                """)
        else:
            print("""
            No se registro ningun producto
                """)
        print("""
            --------------------------------------------------
                        GRACIAS POR SU PREFERENCIA
                            HASTA  LA PRÓXIMA 
            -------------------------------------------------- 
                """)
    
    def eliminar_producto(self):
        
        try:
            self.item = self.tabla.selection()
            self.delected_values = ()
            for item in self.item:
                self.values = self.tabla.item(item, "values")
                self.tabla.delete(item)
                
            if len(self.dato_producto) > 0:
            
                self.capturar_valor = (self.values[0], float(self.values[1]), int(self.values[2]), float(self.values[3]))
                
                if self.capturar_valor in self.dato_producto:
                    self.dato_producto.remove(self.capturar_valor)
                    
                    self.precio_total_actualizado = 0
                    for i in self.dato_producto:
                        self.precio_total_actualizado+=i[-1]
                    
                    self.resultado_productos_totales.config(text=self.precio_total_actualizado)
            else:
                messagebox.showinfo("AVISO IMPORTANTE", """No seleccionaste nada para poder eliminar""")
            
        except:
            messagebox.showinfo("AVISO IMPORTANTE", """No seleccionaste nada para poder eliminar""")
    
    def limpiar_casillas(self):
        self.entrada_nombre.delete(0, END)
        self.entrada_apellido.delete(0, END)
        self.entrada_DNI.delete(0, END)
        self.entrada_correo.delete(0, END)
        self.entrada_telefono.delete(0, END)
        
    def regresar(self, ventanas):
        ventanas.destroy()
        self.ventana.deiconify()
        
        
    def salir(self):
        messagebox.showinfo("AVISO", """Seguro quieres salir de la aplicación?""")
        self.ventana.quit()
        
    def bloqueo_salir(self):
        pass
        
if __name__ == "__main__":
    boleta = Boleta()
    boleta.inicio()