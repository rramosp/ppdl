import sympy as sy

def gaussian(x, mu, sigma):
    """
    returns a sympy expression with the Gaussian distribution PDF
    
    x: sympy symbol for the PDF argument
    mu, sigma:  sympy symbols for the parameters of the distribution
    """
    
    return sy.exp(-0.5*((x-mu)/sigma)**2)/(sigma*sy.sqrt(2*sy.pi))
