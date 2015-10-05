import random
import numpy as np

# 1 kilometer = 1000 meters
# 3.6 km/h = 1 m/s
# 120 km/h = 33.33 m/s

class Road:

	def __init__(self, length):
		self.length = length # meters

	def __str__(self):
		return self.length


class Car:

	def __init__(self, location, car_in_front, top_speed, road_length):
		self.top_speed = top_speed  # meters per second
		self.accelerate_rate = 2  # meters per second
		self.decelerate_rate = 2  # meters per second
		self.length = 5  # meters
		self.speed = 0  # meters per second
		self.car_in_front = car_in_front
		self.location = location
		self.road_length = road_length

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
		road = Road(self.road_length)
		min_distance = int((self.car_in_front.location - 8) - self.location)
		if abs(min_distance) > self.speed:
			self.accel_and_decelerate()
			self.location += self.speed
			if self.location > road.length:
				self.location -= road.length
		else:
			self.speed = self.car_in_front.speed
			self.decelerate()
			self.location += self.speed
			if self.location > road.length:
				self.location -= road.length
		return self.location


class Sim:

	def __init__(self, num_cars, time, car_top_speed, road_length):
		self.num_cars = num_cars
		self.time = time
		self.car_top_speed = car_top_speed # meters per second
		self.road_length = road_length

	def make_car_list(self):
		road = Road(self.road_length)
		car_list = []
		location_list = np.linspace(0, road.length, num=self.num_cars)
		car_in_front = None
		for x in range(self.num_cars):
			location = location_list[x]
			make_car = Car(location, car_in_front, self.car_top_speed, self.road_length)
			car_list.append(make_car)
			car_list[0].car_in_front = car_list[-1]
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
				cars_making_moves = cars_list[x].move_car()
				car_movement.append(cars_making_moves)
				speed_of_cars = cars_list[x].speed
				car_speeds.append(speed_of_cars)
			movement_list.append(car_movement)
			speed_list.append(car_speeds)
		return movement_list, speed_list
