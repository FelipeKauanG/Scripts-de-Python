import math
import os
from random import randint
import re
import sys


num = randint(1, 100)

if num == 2 or num == 4 or num >=20 and num %2 ==0:
    print("Not Weird")
else:
    print("Weird")
