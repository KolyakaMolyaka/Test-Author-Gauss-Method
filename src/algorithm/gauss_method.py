"""
Код функции взят с сайта: https://www.articleshub.net/2023/04/metod-gaussa-python.html
Автор заявляет, что: "Предложенная функция может быть использована для решения систем уравнений
					  с любым количеством переменных и уравнений."
"""

from src.algorithm.decorators.extra_checks import *


@validate_matrix_and_answers
@singular_matrix_decorator
def gauss_method(matrix: list[list[float]], vector: list[float]) -> list[float]:
	"""
	Решение системы линейных уравнений методом Гаусса.
	:param matrix: Матрица коэффициентов уравнений.
	:param vector: Вектор столбец значений уравнений.
	:return: Вектор значений аргументов x, являющихся решением системы уравнений.
	"""

	n = len(matrix)
	for i in range(n):
		max_el = abs(matrix[i][i])
		max_row = i
		for k in range(i + 1, n):
			if abs(matrix[k][i]) > max_el:
				max_el = abs(matrix[k][i])
				max_row = k

		matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
		vector[i], vector[max_row] = vector[max_row], vector[i]

		for k in range(i + 1, n):
			c = -matrix[k][i] / matrix[i][i]
			for j in range(i, n):
				if i == j:
					matrix[k][j] = 0
				else:
					matrix[k][j] += c * matrix[i][j]
			vector[k] += c * vector[i]

	x = [0 for _ in range(n)]
	for i in range(n - 1, -1, -1):
		x[i] = vector[i] / matrix[i][i]
		for k in range(i - 1, -1, -1):
			vector[k] -= matrix[k][i] * x[i]
	return x

# A = [[1, 2], [1, 2]]
# b = [3, 3]
# res = gauss_method(A, b)
# print(res)