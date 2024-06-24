#!/usr/bin/env python3
"""Pagination helper function.
"""
from flask import Flask, request, jsonify
import pandas
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing a start and end index
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
