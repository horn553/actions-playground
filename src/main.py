# isort で整列されていないコード
import re
import abc

type(abc)
type(re)

# flake8 を通過しないコード
print('short line')
print('long long long long long long long long long long long long long long line')

# mypy を通過しないコード
number: int = 100
number = '200'
