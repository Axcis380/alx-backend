#!/usr/bin/env python3
"""Pagination helpefunction.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves range from given page size.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
