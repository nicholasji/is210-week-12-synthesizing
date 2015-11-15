#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 Synthesizing Task 01."""


class BaseError(Exception):
    """Exception class named BaseError which simply extends Exception"""
    pass


class StringError(BaseError, TypeError):
    """StringError, subclassed to BaseError and TypeError"""
    pass


class NumberError(BaseError, TypeError):
    """NumberError, subclassed to BaseError and TypeError"""
    pass


class NonZeroError(NumberError):
    """NonZeroError, subclassed to NumberError"""
    pass
