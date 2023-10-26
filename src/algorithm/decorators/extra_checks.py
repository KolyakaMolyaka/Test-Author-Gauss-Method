from functools import wraps
import numpy as np

from src.algorithm.decorators.extra_checks_exceptions import *


def is_singular_matrix(matrix: list[list[float]]) -> bool:
	"""
	Определение вырожденности матрицы.
	Матрица считается вырожденной, если её определить равен нулю.
	:param matrix: матрица, вырожденность которой необходимо проверить
	:return: True - матрица вырожденная, False - матрица не вырожденная
	"""
	if np.linalg.det(matrix) == 0:
		return True
	return False


def singular_matrix_decorator(func):
	"""Возбуждение исключения, если матрица вырожденная."""

	@wraps(func)
	def decorator(matrix, vector):
		if is_singular_matrix(matrix):
			raise SingularMatrixException()
		return func(matrix, vector)

	return decorator


def validate_matrix_and_answers(func):
	"""
	Проверка корректности входных данных.
	Матрица коэффициентов должна быть квадратная, элементами которой являются вещественные числа.
	Размерности матрицы коэффициентов и вектора-столбца ответов должны совпадать.
	"""

	def decorator(matrix, vector):
		m_rows_len = len(matrix)
		for row in matrix:
			is_int_or_float_values = all([isinstance(coef, (float, int)) for coef in row])
			row_len = len(row)

			if m_rows_len != row_len:
				raise NotSquareMatrixException()

			if not is_int_or_float_values:
				raise NotFloatCoefficientException()

		v_len = len(vector)
		if m_rows_len != v_len:
			raise NotEqualMatrixCoefficientsAndAnswerDimensionsException()

		is_vector_int_or_float_values = all([isinstance(coef, (float, int)) for coef in vector])
		if not is_vector_int_or_float_values:
			raise NotFloatCoefficientException()

		return func(matrix, vector)

	return decorator
