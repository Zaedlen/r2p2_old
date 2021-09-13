import sys

class add_path():
    '''
        Wrapper class to automatically handle adding the local controller
        directory to the simulator's execution path.
    '''
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        sys.path.insert(0, self.path)

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            sys.path.remove(self.path)
        except ValueError:
            pass

def load_controller(name):
    """
        ###
        
        Ejemplo: name = 'naive_controller.Naive_Controller'
        components = ['naive_controller', 'Naive_Controller']
        controller = naive_controller (el objeto tras el import)
        for:
            controller = getattr(naive_controller, 'Naive_Controller')
                -> controller = referencia a la clase Naive_Controller

        Si hubiera varios devuelve una lista de referencias
    """
    with add_path('controllers'):
        components = name.split('.')
        controller = __import__(components[0])
        for comp in components[1:]:
            controller = getattr(controller, comp)
    return controller

def get_controllers(config):
    """Create controllers based on the configuration received"""
    if 'class' in config:
        # Create the controller passing the config as arg to the constructor
        return load_controller(config['class'])(config)
    elif 'controllers' in config and len(config['controllers']) > 0:
        controllers = []
        for ctrl in config['controllers']:
            # Create the controller passing the config as arg to the constructor
            controller = load_controller(ctrl['class'])(config)
            controllers.append(controller)
        return controllers



