import json

default = {
    'posX':2,
    'posY':5,
    'veloc':30,
    'lista':[],
}

class ControllerP(object):
    '''
        Clase de prueba:
        -   En la version final hacer clase abstracta y controladores concretos
    '''

    def __init__(self) -> None:
        # # Hard copy
        # self._parametros = {**default} # Un poco mas lento que copy pero apenas (0.7 sec aprox 1 millon de copias)
        # self._parametros = dict(default)  # El mas lento (0.7 - 0.8 sec aprox 1 millon de copias)
        # self._parametros = default.copy() # Mas rapido (0.6 - 0.7 sec aprox 1 millon de copias)

        # # IMP: Crear 1 milon de instancias, objetos de una clase para un dict como este: 0.9 - 1.1 sec aprox 1 millon de instancias. El mas lento de todos (y que mas mem consume)

        # Only reference:  --mejor--  default ya no importa modificarlo mientras dure la ejecucion y optimizamos recursos
        self._parametros = default  # Mucho mas rapido (0.1 sec aprox 1 millon de copias)

        self.cargar_datos('controller_conf.json')
        # self._parametros['posY'] = 60
        # self.guardar_datos('D:/Zaedlen/Documents/Universidad/4o/TFG/R2P2/r2p2/pruebas/refactor/controller_conf.json')

    def __getitem__(self, name):
        '''
            Hace la clase subscriptable y permite acceder a elem como cuando accedes a un diccionario:
                con = ControllerP()
                con['posX']
        '''
        return self._parametros[name]

    def __getattr__(self, name: str) -> None:
        '''
            Nos permite acceder a los elem del dict parametros como si fueran atributos de la clase directamente
        '''
        if name in self._parametros:
            return self._parametros[name]
        else:
            raise AttributeError("'"+self.__class__.__name__+"' object has no attribute '"+name+"'")

    def __setattr__(self, name: str, value) -> None:
        '''
            Nos permite modificar los elem del dict parametros como si fueran atributos de la clase directamente

            Puede ser muyutil pero hay que pensar muy bien las politicas para añadir nuevos atributos normales
            y/o elem al dict parametros. Uno, otro, ambos introduciendo un flag o mediante alguna otra forma...
        '''
        if (name != '_parametros') and (name in self._parametros):
            print('Seteando por mi cuenta', name)
            self._parametros[name] = value
        else:
            print('Seteamos como siempre', name)
            return super().__setattr__(name, value)

    def cargar_datos(self, ruta: str):
        with open(ruta, 'r') as f:
            lectura = json.load(f)
        
        self._parametros = {**self._parametros, **lectura}

        print(self._parametros)



    def guardar_datos(self, ruta: str):
        with open(ruta, 'w') as f:
            json.dump(self._parametros, f, indent=4)



    # Definimos parametros como propiedad de forma que se accede desde fuera como nosotros queramos, con unos metodos get y set definidos:
    @property
    def parametros(self):
        return self._parametros

    @parametros.setter
    def parametros(self, key:str, value):
        self._parametros[key] = value

    @parametros.deleter
    def parametros(self):
        self._parametros.clear()
        del self._parametros
