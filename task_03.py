#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 Synthesizing Task 03."""


def exception_test(arg1, arg2, arg3):
    """Except clauses may match multiple types of
    exceptions saving unnecessary duplication and effort.
    Args:
        arg1, arg2, arg3.
    Attributes:
        caught(bool): Error if true.
    Returns:
        error
    Example:
        >>> exception_test(['apple'], 0,'p')
        False
        >>> exception_test(43, 1, 1)
        True
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except(TypeError, LookupError):
        caught = True

    return caught
