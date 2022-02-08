from typing import Optional
from pandas import DataFrame
import numpy as np
import pandas as pd

def flu_season_contact_sampler(n_samples: int = 1000, seed: Optional[int] = None) -> DataFrame:
    """
    Generate samples from the conditional distribution.

    Parameters
    ----------
    n_samples : int
        Number of samples to generate.
    seed : int, optional
        Random seed.

    Returns
    -------
    pd.DataFrame
        DataFrame with samples from the conditional distribution.
    """
    if seed is not None:
        state = np.random.get_state()
        np.random.seed(seed)
    cond_dist = pd.DataFrame({
        "x_1": ["winter", "spring", "summer", "autumn"] * 2,
        "x_2": [0] * 4 + [1] * 4,
        "Pygx_1x_2": [0.6, 0.1, 0.05, 0.4, 0.7, 0.2, 0.1, 0.5]
        })
    seasons = cond_dist.x_1.unique()

    samples = []
    for _ in range(n_samples):
        season = np.random.choice(seasons)
        x_2 = np.random.randint(2)
        prob = cond_dist.query("x_1 == @season & x_2 == @x_2").Pygx_1x_2.values[0]
        y = np.random.binomial(1, prob)
        samples.append((season, x_2, y))
    samples_df = pd.DataFrame(samples, columns=["x_1", "x_2", "y"])
    if seed is not None:
        np.random.set_state(state)
    return samples_df
