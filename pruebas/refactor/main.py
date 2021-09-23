
from controllerP import ControllerP

if __name__ == '__main__':
    con = ControllerP()
    print(con['veloc'])
    print(con.parametros['veloc'])
    print(con.posX)
    con.noEsta = 3
    con.posX = 50
    print(con.posX)
    print(con['posX'])
    print(con.noEsta)
    con.guardar_datos('D:/Zaedlen/Documents/Universidad/4o/TFG/R2P2/r2p2/pruebas/refactor/controller_conf.json')
