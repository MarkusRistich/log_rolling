""" The case for formatters was introduced in PEP282, which also defined a
    handful of replacement tokens in log formatting.
    The full list is available here: https://www.python.org/dev/peps/pep-0282/#formatters

    It is common to use {asctime} and {levelname} as standard formatting for log messages.

    Occasionally, it will be beneficial to use {name} and {pathname} for identifying the
    logging channel, as well as the location of the code that is logging (in case it is
    uncertain where code is being executed).
"""
