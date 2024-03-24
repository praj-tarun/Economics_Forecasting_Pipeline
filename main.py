from fredapi import Fred
import matplotlib.pyplot as plt

fred_key = "a85f52ab102ccf808744766693f330b4"

fred = Fred(api_key = fred_key)

sample_search = fred.search("india gdp")

print(sample_search)


def unemp_data(id='SLUEM1524ZSIND'):
    unemp = fred.get_series(id)
    unemp.plot()
    plt.show()

unemp_data()

