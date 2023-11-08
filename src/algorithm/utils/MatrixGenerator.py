import numpy as np
import random


class NotSingularGeneratedMatrix:
	@property
	def det(self):
		return self._det

	@property
	def matrix(self):
		return self._matrix

	def __init__(self, n: int = 5, rand_from: float = 0, rand_to: float = 100):
		"""
		Генерирование невырожденной матрицы размером NxN со значениями в диапазоне [rand_from; rand_to]
		:param n: размерность матрицы
		:param rand_from: начало диапазона генерации значений
		:param rand_to: конец диапазона генерации значений
		"""

		self._det = 0
		while self.det == 0:
			self._generate_matrix(n, rand_from, rand_to)
			self._det = np.linalg.det(self._matrix)

	def _generate_matrix(self, n: int, rand_from: float, rand_to: float):
		"""
		Генерирование матрицы размерностью NxN со значениями в диапазоне [rand_from; rand_to]
		:param n: размерность матрицы
		:param rand_from: начало диапазона генерации значений
		:param rand_to: конец диапазона генерации значений
		"""

		self._matrix = []
		for i in range(n):
			row = []
			for j in range(n):
				random_val = random.uniform(rand_from, rand_to)
				row.append(random_val)
			self._matrix.append(row)

	def __str__(self):
		return f'{self.matrix}'
