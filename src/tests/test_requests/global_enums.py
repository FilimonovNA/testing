from enum import Enum


class GlobalErrorsMessages(Enum):
    WRONG_STATUS_CODE = "Received status code not equal to expected"
    WRONG_ELEMENT_COUNT = "Number of items not equal to expected"
