import pandas as pd
stock_list = []

weight = 1
factor_vix = 15
price = 87

probability = weight*factor_vix


expect = price*probability
print(expect)