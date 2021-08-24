"""
NOMBRE
    7-Simpson.py
VERSION 
     1.0
AUTOR 
    Montes Gabriel Diego <dmontes@lcg.com.mx>
DESCRIPCION
    Este programa encuentra un valor aproximado para la integral de una funcion utilizando el metodo de Simpson 
PARAMETROS DE ENTRADA 
    Funciones de la forma y=f(x)
SALIDA
    El resultado de sumar las areas bajo la curva determinadas por los arcos generados
EJEMPLO
    f(x) = x**2 + 1
"""
import sympy, numpy

from sympy import Symbol

""" funcion que comprueba que una cadena contiene un valor numerico
"""

def es_numero(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
        
#funcion para ingresar y validar un intervalo dado por el usuario
def ingresar_limites():
    
    print("ingresa el intervalo en el que quieres integrar tu funcion")
    lim_inferior = float(input("desde: "))
    lim_superior = float(input("hasta: "))
    while lim_inferior >= lim_superior:
        print("ingresa el intervalo en el que quieres integrar tu funcion ")
        lim_inferior = float(input("desde: "))
        lim_superior = float(input("hasta: "))
    return [lim_inferior, lim_superior] 

#funcion para insertar y validar expresiones   
def ingresar_funcion():
        
        from sympy.parsing.sympy_parser import parse_expr       
        from sympy import sympify
        
        print("Ingrese su funcion")        
        funcion = (sympify(input("f(x) = ")))
        print ("Es esta su funcion?")
        sympy.pprint(funcion)
        respuesta = input("responde si o no: ")
        while respuesta != "si":
            if respuesta == "no":
                print ("Ingrese su funcion")
                funcion = (parse_expr(input("f(x) = ")))
                print ("Es esta su funcion?")
                sympy.pprint(funcion)
                respuesta = input("responde si o no")    
            else:
                 respuesta = input("responde si o no")
         #se sustituyen los valores para que la expresion sea compatible con matplotlib
        funcion = funcion.subs('pi', 3.14159265359)
        funcion = funcion.subs('e', 2.71828182846)
        return funcion
 
#funcion que evalua los valores de los intervalos x y los suma a la solucion   
def calcular_integral(limites,funcion):
    
    from numpy import arange
    
    area = 0 
    i = 0
    
    subintervalos = float(input("cuantos subintervalos quieres?"))
    intervalo= (limites[1]-limites[0])/subintervalos
    for valor in arange(limites[0],limites[1]+intervalo, intervalo):    
        if (valor != limites[0] and valor != limites[1]):
            if(i % 2):
                area += funcion.subs(x,valor) * 4.0
            else:
                area += funcion.subs(x,valor) * 2.0
        else:
            area += funcion.subs(x,valor) 
        i += 1
    area = (intervalo / 3.0)  * area
    print (area)

x = Symbol('x')
#funcion principal que le pide los datos al usuario y llama a las demas funciones

print("Bienvenido al programa de integracion de Simpson")
limites = ingresar_limites()
funcion = ingresar_funcion()
calcular_integral(limites,funcion)

"""
DICCIONARIO 
	cadena: cadena usada para validar que una cadena contiene un valor numerico
	limite_inferior: limite inferior de un intervalo
	limite_superior: limite superior de un intervalo
	precision: numero de decimales que el usuario pide para sus soluciones
	es_despeje: bandera que indica si la funcion a ingresar sera la funcion principal o un despeje
	funcion: expresion de sympy que el usuario ingresa para buscar sus raices
	respuesta: cadena con respuesta de usuario
    area: aproximacion integral que se quiere obtener sumando evluaciones del intervalo
    subintervalos: cantidad de trapecios en los que se dividira la funcion a integrar
    intervalo: altura del trapecio que se manejara
    valor: iterador, que sirve para determinar como evaluar la proxima iteracion
    limites: lista con los limites de la integral
"""