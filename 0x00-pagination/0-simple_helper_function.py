#!/usr/bin/env python3
'''A module that contains a function named index_range that takes two integer'''

def index_range(page: int, page_size: int) -> tuple:
    '''A function that return a tuple of size two containing a start index and an end index'''
    end_idx = page * page_size
    start_idx = end_idx - page_size
    return start_idx, end_idx