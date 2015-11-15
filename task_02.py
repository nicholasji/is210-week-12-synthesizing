#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 12 Synthesizing Task 02."""


class CustomError(Exception):
    """Custom exception class named CustomError subclassed to Exception"""

    def __init__(self, msg, cause):
        """constructor that calls Exception.__init__() but
        also takes a third parameter named cause and stores
        its value as self.cause
        Args:
            msg(str): user defined string
            cause(str): error causes
        Returns:
           None
        Examples:
        >>> myerr = CustomError('Whoah!', cause='Messed up!')
        >>> print myerr.cause
            Messed up!
        """
        Exception.__init__(self)
        self.cause = cause
        self.msg = msg
