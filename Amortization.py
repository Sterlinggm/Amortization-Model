import pandas
import numpy as np
from datetime import date
#Define variables below for specific property
Interest_Rate = .04
Years = 30
Payments_Year = 12
Principal = 200000
Addl_Princ = 50
start_date = (date(2016,1,1))
#Function below
pmt = np.pmt(Interest_Rate/Payments_Year, Years*Payments_Year, Principal)
print pmt

per = 1
ipmt = np.ipmt(Interest_Rate/Payments_Year, per, Years*Payments_Year, Principal)
ppmt = np.ppmt(Interest_Rate/Payments_Year, per, Years*Payments_Year, Principal)
print(ipmt, ppmt)

