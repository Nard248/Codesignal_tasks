import pandas as pd

pp_old = pd.read_excel('pickuppoint.xlsx')
pp_new = pd.read_excel('pickuppoint_all.xlsx')
print(pp_new.shape, pp_old.shape)
