#!/usr/bin/env python3
"""Pagination helper function.
"""
from flask import Flask, request, jsonify
# import pandas made problems in checker
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing a start and end index
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
