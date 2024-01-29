#modelo 1
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Sample data: You should replace this with the actual data and variables considered by the Fed
# For simplicity, let's assume you have a dataset with columns 'Inflation', 'Unemployment', and 'GDP'
data = {
    'Inflation': [2.0, 2.5, 1.8, 2.2, 1.5, 1.2, 2.0, 1.8, 2.5, 2.8],
    'Unemployment': [5.0, 4.8, 5.2, 4.5, 5.5, 5.0, 4.2, 4.0, 4.8, 5.2],
    'GDP': [2.5, 3.0, 2.8, 3.2, 2.0, 2.5, 3.5, 3.0, 2.2, 2.8],
}

df = pd.DataFrame(data)

# Econometric model
X = sm.add_constant(df[['Inflation', 'Unemployment', 'GDP']])
y = df['InterestRate']  # This is a hypothetical dependent variable representing the interest rate

model = sm.OLS(y, X).fit()

# Print the model summary
print(model.summary())


#modelo 2
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Sample data: You should replace this with the actual data from the Brazilian Central Bank
# For simplicity, let's assume you have a dataset with columns 'Inflation', 'GDP', and 'InterestRate'
data = {
    'Inflation': [3.5, 4.2, 3.8, 5.1, 4.0, 3.6, 4.5, 4.8, 5.0, 5.2],
    'GDP': [2.0, 2.5, 1.8, 1.2, 2.8, 2.0, 1.5, 1.0, 1.2, 2.5],
    'InterestRate': [5.0, 4.8, 5.2, 4.5, 5.5, 5.0, 4.2, 4.0, 4.8, 5.2]
}

df = pd.DataFrame(data)

# Econometric model
X = sm.add_constant(df[['GDP', 'InterestRate']])
y = df['Inflation']

model = sm.OLS(y, X).fit()

# Print the model summary
print(model.summary())


"""