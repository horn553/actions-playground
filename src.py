# isort に違反したコード
import re
import abc

type(re)
type(abc)

# flake8 に違反したコード
print('long long long long long long long long long long long long long long code')

# mypy に違反したコード
number: int = 100
list(number)
