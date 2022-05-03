# pip install arviz numpy pymc3
import arviz as az
import numpy as np
import pymc3 as pm


if __name__ == '__main__':
    # Example from https://docs.pymc.io/en/v3/about.html
    # Set style
    az.style.use("arviz-darkgrid")

    # Data
    n = np.ones(4)*5
    y = np.array([0, 1, 3, 5])
    dose = np.array([-.86,-.3,-.05,.73])

    with pm.Model() as bioassay_model:

        # Prior distributions for latent variables
        alpha = pm.Normal('alpha', 0, sigma=10)
        beta = pm.Normal('beta', 0, sigma=1)

        # Linear combination of parameters
        theta = pm.invlogit(alpha + beta * dose)

        # Model likelihood
        deaths = pm.Binomial('deaths', n=n, p=theta, observed=y)

    with bioassay_model:

        # Draw samples
        trace = pm.sample(1000, tune=2000, cores=2)
        # Plot two parameters
        az.plot_forest(trace, var_names=['alpha', 'beta'], r_hat=True)