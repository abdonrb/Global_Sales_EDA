from scripts.ClaseAbdon import DataFrameAnalyzer
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3]})
analyzer = DataFrameAnalyzer(df)
analyzer.describe_numeric()

