import re

parse = lambda line: list(map(int, re.split(';|,| |\t', line.replace('\n', ''))))
