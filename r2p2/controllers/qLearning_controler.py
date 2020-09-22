import numpy as np
import math

import controller as c
import utils as u
import pygame
import random

class QLearning_controller(c.Controller):
    def __init__(self):
        super(QLearning_controller, self).__init__("QL")
        self.detected_edges = []
        self.cur_detected_edges = []
        self.actual_sensor_angles = []
        self.cur_detected_edges_distances = []

        # Guardamos condiciones iniciales
        self.origin = (-1, -1) # Lo inicializa el robot
        self.orginalOrientation = 0 # Lo inicializa el robot

        # Definimos constantes
        self.learning_rate = 0.1
        self.discount = 0.95
        self.training_episodes = 1000

        self.discrete_states_number = 3 # Numero de tramos en los que discretizamos los sensores
        self.discrete_actions_number = 3 # Numero de tramos en los que discretizamos las acciones
        self.discrete_window_size = -1 # Lo inicializa el robot

        self.max_velocity = -1 # Lo inicializa el robot
        self.max_angular = 25

        # Estructuras necesarias
        # self.

        self.number = random.randint(5,20)

    def control(self, dst):
        """
            Driver function to centralize and standardize the controller.
        """
        super(QLearning_controller, self).control(dst)
        
        # if sum(dst) < ((self.robot.vision_range[1] + self.robot.radius) * len(dst)):
        #     print(dst)
        # print(dst)
        # print(self.robot.orientation)
        # print(self.robot.x, self.robot.y)
        # print(self.robot.sensors)
        # print(self.robot.angular_velocity)
        return self.choose_speed(self.ang, dst), self.choose_angle(self.ang, self.dst)
        # return self.number + 30, self.number

    def register_robot(self, r):
        """
            Registers the robot with the controller. Can be used to issue specific instructions directly, or
            to read some odometry information from the physical hardware.
        """
        self.robot = r

        # Guardamos condiciones iniciales
        self.origin = (self.robot.x, self.robot.y)
        self.orginalOrientation = self.robot.orientation

        # Definimos constantes
        self.discrete_window_size = (r.vision_range[1] - r.vision_range[0]) / self.discrete_states_number
        self.max_velocity = r.max_speed

    def get_discrete_state(self, state):
        """
            Devuelve un estado discreto dentro de uno de los tramos en los que hemos
            dividido el rango total de los sensores.

            Cada estado se define como un combinación concreta de valores de los sensores
        """
        discrete_state = (np.array(state) - ([r.vision_range[0]] * len(state))) / ([self.discrete_window_size] * len(state))
        return discrete_state.astype(np.int).tolist()

    def get_discrete_velocities(self, high, low = 0.0, length = self.discrete_actions_number):
        veloc = [low]
        for i in range(1, length):
            veloc.append(i * (high/(length - 1)))
        return veloc

    def combine_actions(self, action_list_a, action_list_b):
        

    def choose_angle(self, ang, dst):
        """
            Sets the angular velocity to 25 degrees per second in the direction of the pressed arrow.
            If there are no side arrows pressed, it returns 0.
        """
        global joystick
        if pygame.joystick.get_count() > 0 and joystick.get_init():
            x_diff = joystick.get_axis(0)
            if abs(x_diff) >= 0.01: # Anything under that threshold can be dismissed as noise
                return 90 * x_diff
        if pygame.K_LEFT in u.pressed:
            return -25
        elif pygame.K_RIGHT in u.pressed:
            return 25
        return 0
    
    def choose_speed(self, ang, dst):
        """
            Alters the robot's acceleration based on the directional arrows pressed.
            If forward is pressed, it increases in 3 pixels per second squared.
            If backward is pressed, it decresses in 3 pixels per second squared.
            If none of them are pressed, the robot's acceleration is not modified.
        """
        if pygame.joystick.get_count() > 0 and joystick.get_init():
            y_diff = joystick.get_axis(1)
            if abs(y_diff) >= 0.01: # Anything under that threshold can be dismissed as noise
                return self.robot.max_speed * -1 * y_diff
        if pygame.K_UP in u.pressed:
            return self.robot.speed + 3
        elif pygame.K_DOWN in u.pressed:
            return self.robot.speed - 3
        elif pygame.K_r in u.pressed:
            self.robot.x = self.origin[0]
            self.robot.y = self.origin[1]
            self.robot.orientation = self.orginalOrientation
            return 0
        elif pygame.K_y in u.pressed:
            self.robot.orientation = 90
            return 0
        return 0

    def on_collision(self, pos):
        # self.robot.x = self.origin[0]
        # self.robot.y = self.origin[1]
        # self.robot.orientation = self.orginalOrientation
        self.number = random.randint(5,20)