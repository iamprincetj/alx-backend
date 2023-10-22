#!/usr/bin/env python3
'''
    Simple pagination.
'''
import csv
import math
from typing import List
import math


def index_range(page, page_size):
    '''
        Returns the range of indexes for a given page.
    '''
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:  # sourcery skip: identity-comprehension
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
            Returns a page of data.
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        mylist = self.dataset()

        print(f"here {math.ceil(len(mylist)/page_size)}")

        start, end = index_range(page, page_size)

        try:
            return mylist[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''
            Returns a dict of data.
        '''

        myDict = {}
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        mylist = self.dataset()

        total_page = math.ceil(len(mylist)/page_size)

        if page < total_page:
            next_page = page + 1
        else:
            next_page = None

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        start, end = index_range(page, page_size)

        try:
            data = mylist[start:end]
        except IndexError:
            return []

        myDict['page_size'] = page_size
        myDict['page'] = page
        myDict['data'] = data
        myDict['next_page'] = next_page
        myDict['prev_page'] = prev_page
        myDict['total_pages'] = total_page

        return myDict
