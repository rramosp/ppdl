import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def plot_pdf(d, n_samples=100000, n_steps=100,
             hist_args={"bins": 100, "alpha": 0.5, "color": "steelblue" }, 
             pdf_args={"lw": 2, "color": "black"}):
    """
    Plots the density and histogram of samples of a 1D distribution
    d: a TFP distribution
    n_samples: the number of samples
    n_steps: number of steps for pdf plot
    hist_args: arguments for plt.hist for samples
    pdf_args: arguments for plt.plot for pdf
    """
    
    s = d.sample(n_samples).numpy()
    xr = np.linspace(np.min(s), np.max(s), n_steps)
    plt.hist(s, density=True, **hist_args)
    plt.plot(xr, np.exp(d.log_prob(xr)), **pdf_args)
    

