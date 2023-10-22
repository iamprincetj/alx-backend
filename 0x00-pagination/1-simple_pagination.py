#!/usr/bin/env python3
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''A function that return a tuple of size
       two containing a start index and an end index'''
    end_idx = page * page_size
    start_idx = end_idx - page_size
    return start_idx, end_idx


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''A method that takes two integer arguments '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        start, end = index_range(page, page_size)

        mylist = self.dataset()
        if mylist is None:
            return []
        return mylist[start:end]
