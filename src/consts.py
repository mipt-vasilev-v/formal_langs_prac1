from enum import Enum

ALPHABET = {"a", "b", "c", "1"}
OPERATION_LIST = {".", '+', '*'}
class OPERATIONS(Enum):
    CONCATENATION = "."
    SUM = "+"
    REPEATING = "*"
