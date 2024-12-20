import pandas as pd
from datetime import datetime

def save_results_table(results_table):
    """
    Saves the results table to Excel with a unique filename.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"utilities/results/results_{timestamp}.xlsx"
    results_table.to_excel(filename, index=False)
    print(f"Results saved to {filename}")
