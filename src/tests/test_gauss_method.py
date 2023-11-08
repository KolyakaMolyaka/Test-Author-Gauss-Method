import unittest
import math
from copy import deepcopy

from src.algorithm.decorators.extra_checks_exceptions import *
from src.algorithm.gauss_method import gauss_method
from src.algorithm.utils.MatrixGenerator import NotSingularGeneratedMatrix


class TestGaussMethod(unittest.TestCase):

	@classmethod
	def check_solution(cls, A: list[list[[float]]], b: list[float], x: list[float], abs_tol=1e-02) -> None:
		"""
		Проверка корректности решения
		:param A: Матрица коэффициентов уравнения.
		:param b: Вектор столбец значений уравнений.
		:param x: Вектор значений аргументов x, являющихся решением системы уравнений.
		:param abs_tol: Погрешность сравнения равенства левых и правых частей системы уравнений.
		:return:
		"""

		for ind, row in enumerate(A):
			pairs = zip(row, x)
			row_sum = sum([coef * x for coef, x in pairs])
			equal = math.isclose(b[ind], row_sum, abs_tol=abs_tol)
			unittest.TestCase.assertTrue(cls, equal)

	def test_right_solution_passed(self):
		"""
		Тест, проверяющий работу функции.
		Failed: Функция решает СЛУ методом Гаусса неправильно.
		Passed: Функция решает СЛУ методом Гаусса правильно.
		Expected: Правильное решение системы линейных уравнений.
		"""

		A = [
			[3, 2, -1],
			[2, -2, 4],
			[-1, .5, -1]
		]
		b = [-1, -2, 0]

		A_copy = deepcopy(A)

		xs = gauss_method(A_copy, b[:])

		self.check_solution(A, b, xs)

	def test_singular_matrix_no_solution(self):
		"""
		Метод Гаусса не может работать с вырожденными матрицами.
		Failed: Функция не возбуждает исключение SingularMatrixException.
		Passed: Функция возбуждает исключение SingularMatrixException.
		Expected: Возбуждение исключения SingularMatrixException при решении СЛУ с вырожденной матрицей.
		"""

		A = [
			[1, 2, 3],
			[1, 2, 3],
			[1, 2, 3]
		]

		A_copy = deepcopy(A)

		with self.assertRaises(SingularMatrixException):
			vector = [1 for i in range(len(A))]  # заполнитель, может быть любым
			gauss_method(A_copy, vector)

	def test_not_square_matrix_raise_exception(self):
		"""
		Метод Гаусса работает только с квадратными матрицами.
		Failed: Функция не возбуждает исключение NotSquareMatrixException.
		Passed: Функция возбуждает исключение NotSquareMatrixException.
		Expected: Возбуждение исключения SingularMatrixException при решении СЛУ с неквадратной матрицей.
		:return:
		"""
		A = [
			[1, 2],
			[3]
		]
		b = [1, 1]

		with self.assertRaises(NotSquareMatrixException):
			gauss_method(A, b)

	def test_not_float_subset_coefficients_raise_exception(self):
		"""
		Метод Гаусса работает только с подмножествами вещественных чисел.
		Failed: Функция не возбуждает исключение NotFloatCoefficientException.
		Passed: Функция возбуждает исключение NotFloatCoefficientException.
		Expected: Возбуждение исключения NotFloatCoefficientException.
		"""
		tests = [
			([['1']], [1]),
			([[1]], ['1'])
		]

		for test in tests:
			A, b = test
			with self.assertRaises(NotFloatCoefficientException):
				gauss_method(A, b)

	def test_not_equals_coefficients_raise_exception(self):
		"""
		В методе Гаусса количество строк матрицы коэффициентов должно быть равно количеству элементов вектор-столбца ответа.
		Failed: Функция не возбуждает исключение NotEqualMatrixCoefficientsAndAnswerDimensionsException.
		Passed: Функция возбуждает исключение NotEqualMatrixCoefficientsAndAnswerDimensionsException.
		Expected: Возбуждение исключения NotEqualMatrixCoefficientsAndAnswerDimensionsException.
		"""
		tests = [
			([[1, 1], [0, 0]], [1]),
			([[1]], [1, 2])
		]

		for test in tests:
			A, b = test
			with self.assertRaises(NotEqualMatrixCoefficientsAndAnswerDimensionsException):
				gauss_method(A, b)

	def test_big_dimension_matrix_solution(self):
		"""
		Метод Гаусса долго работает большими матрицами, потому что его сложность O(n^3),
		однако, он должен найти ответ.
		Failed: Функция не может решить СЛУ.
		Passed: Функция может решить СЛУ.
		Expected: Решение СЛУ.
		"""

		n = 50
		A = NotSingularGeneratedMatrix(n)
		A_mat = deepcopy(A.matrix)
		x = [i for i in range(n)]

		b = []
		for row in A_mat:
			pairs = zip(row, x)
			row_sum = sum([coef * x for coef, x in pairs])
			b.append(row_sum)

		xs = gauss_method(A_mat, b.copy())
		self.check_solution(A.matrix, b, xs)

	def test_small_values_matrix_solution(self):
		"""
		Метод Гаусса работает маленькими значениями и способен найти ответ.
		Failed: Функция не может решить СЛУ.
		Passed: Функция может решить СЛУ.
		Expected: Решение СЛУ.
		"""
		n = 5
		A = NotSingularGeneratedMatrix(n, rand_from=1e-7, rand_to=1e-6)
		A_mat = deepcopy(A.matrix)
		x = [i for i in range(n)]

		b = []
		for row in A_mat:
			pairs = zip(row, x)
			row_sum = sum([coef * x for coef, x in pairs])
			b.append(row_sum)

		xs = gauss_method(A_mat, b.copy())
		self.check_solution(A.matrix, b, xs, abs_tol=1e-9)

	def test_big_values_matrix_solution(self):
		"""
		Метод Гаусса работает с большими значениями и способен найти ответ.
		Failed: Функция не может решить СЛУ.
		Passed: Функция может решить СЛУ.
		Expected: Решение СЛУ.
		"""
		n = 5
		A = NotSingularGeneratedMatrix(n, rand_from=1e6, rand_to=1e7)
		A_mat = deepcopy(A.matrix)
		x = [i for i in range(n)]

		b = []
		for row in A_mat:
			pairs = zip(row, x)
			row_sum = sum([coef * x for coef, x in pairs])
			b.append(row_sum)

		xs = gauss_method(A_mat, b.copy())
		self.check_solution(A.matrix, b, xs)
