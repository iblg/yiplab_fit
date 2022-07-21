import pandas as pd
import numpy as np
def open_read_csv(file) -> pd.DataFrame:

    with open(file, 'r') as f:
        data = pd.read_csv(f)

    return data