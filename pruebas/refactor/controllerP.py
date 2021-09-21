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
        self._parametros = {**default}
        self.cargar_datos('controller_conf.json')
        self._parametros['posY'] = 60
        self.guardar_datos('D:/Zaedlen/Documents/Universidad/4o/TFG/R2P2/r2p2/pruebas/refactor/controller_conf.json')

    def __getitem__(self, name):
        return self._parametros[name]

    def cargar_datos(self, ruta: str):
        with open(ruta, 'r') as f:
            lectura = json.load(f)
        
        self._parametros = {**self._parametros, **lectura}

        print(self._parametros)



    def guardar_datos(self, ruta: str):
        with open(ruta, 'w') as f:
            json.dump(self._parametros, f, indent=4)



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
