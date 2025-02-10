from typing import List, Any


def listContains(subList: List[Any], testList: List[Any]) -> bool:
    """

    :param subList:
    :param testList:
    :return:
    """
    counter = 0
    res = False
    for item in subList:
        if item in testList:
            counter += 1
    if counter == len(subList):
        res = True
    return res