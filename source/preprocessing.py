import numpy as np
import pandas as pd

def reshape_insole_data(insole_data):
    """
    Reshape the 1D insole data into 3D array (time, rows, cols)
    
    Args:
        insole_data: array of shape (n_timestamps, 1024)
    Returns:
        reshaped_data: array of shape (n_timestamps, 64, 16)
    """
    n_timestamps = insole_data.shape[0]