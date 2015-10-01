import random
import numpy

# 1 kilometer = 1000 meters
# 3.6 km/h = 1 m/s
# 120 km/h = 33.33 m/s

class Road:

	def __init__(self, length):
		self.length = 1000  # meters

	def __str__(self):
		return self.length


class Car:

	def __init__(self, car_in_front):
		self.top_speed = 33  # meters per second
		self.accelerate_rate = 2  # meters per second
		self.decelerate_rate = 2  # meters per second
		self.length = 5  # meters
		self.speed = 0  # meters per second
		self.car_in_front = car_in_front

	def accelerate(self):
		if self.speed < self.top_speed:
			self.speed += self.accelerate_rate
		elif self.speed > self.top_speed:
			self.speed = self.top_speed
		return self.speed

	def decelerate(self):
		to_slow = random.randint(1, 10)
		if to_slow == 1:
			self.speed -= self.decelerate_rate
		elif self.speed < 0:
			self.speed = 0
		return self.current_speed

	def car_in_front_distance(self):
		pass
