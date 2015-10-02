import random
import numpy as np

# 1 kilometer = 1000 meters
# 3.6 km/h = 1 m/s
# 120 km/h = 33.33 m/s

class Road:

	def __init__(self, length):
		self.length = 1000  # meters

	def __str__(self):
		return self.length


class Car:

	def __init__(self, location, car_in_front):
		self.top_speed = 33  # meters per second
		self.accelerate_rate = 2  # meters per second
		self.decelerate_rate = 2  # meters per second
		self.length = 5  # meters
		self.speed = 0  # meters per second
		self.car_in_front = car_in_front
		self.location = location  # but how do I make them start at different places?

	def min_distance(self):
		return int((self.car_in_front.location - 6) - self.location)

	def decelerate(self):
		to_slow = random.randint(1, 10)
		if to_slow == 1:
			self.speed -= self.decelerate_rate
			if self.speed < 0:
				self.speed = 0
		return self.speed

	def accel_and_decelerate(self):
		to_slow = random.randint(1, 10)
		if to_slow == 1:
			self.speed -= self.decelerate_rate
			if self.speed < 0:
				self.speed = 0
		else:
			if self.speed < self.top_speed:
				self.speed += self.accelerate_rate
				if self.speed > self.top_speed:
					self.speed = self.top_speed
			return  self.speed

	def move_car(self):
		min_distance = int((self.car_in_front.location - 6) - self.location)
		if abs(min_distance) > self.speed:
			self.accel_and_decelerate()
			self.location += self.speed
			if self.location > 1000:
				self.location -= 1000
		else:
			self.speed = self.car_in_front.speed
			self.decelerate()
			self.location += self.speed
			if self.location > 1000:
				self.location -= 1000
		return self.location


class Sim:

	def __init__(self, num_cars, time):
		self.num_cars = num_cars
		self.time = time

	def make_car_list(self):
		car_list = []
		location_list = np.linspace(0, 100, num=self.num_cars)
		car_in_front = None
		location = 999
		for x in range(self.num_cars):
			make_car = Car(location, car_in_front)
			car_list.append(make_car)
			car_list[0].car_in_front = car_list[-1]
			location -= 33
			car_in_front = make_car
		return car_list

	def run_sim(self):
		cars_list = self.make_car_list()
		movement_list = []
		speed_list = []
		for y in range(self.time):
			car_movement = []
			car_speeds = []
			for x in range(len(cars_list)):
				yyz = cars_list[x].move_car()
				car_movement.append(yyz)
				zzy = car_list[x].speed
				car_speeds.append(zzy)
			movement_list.append(car_movement)
			speed_list.append(car_speeds)
		return movement_list
