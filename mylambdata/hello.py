#TODO: import enlarge
from pandas import DataFrame

from mylambdata.mymod import enlarge

print("HELLO")

print(enlarge(8))

df = DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())