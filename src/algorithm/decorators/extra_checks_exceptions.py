__all__ = [
	'SingularMatrixException',
	'NotSquareMatrixException',
	'NotFloatCoefficientException',
	'NotEqualMatrixCoefficientsAndAnswerDimensionsException'
]


class SingularMatrixException(Exception):
	pass


class NotSquareMatrixException(Exception):
	pass


class NotFloatCoefficientException(Exception):
	pass


class NotEqualMatrixCoefficientsAndAnswerDimensionsException(Exception):
	pass
