from scipy.optimize import root_scalar

cash_flows = [-1000., 400., 400., 400.]
def npv(rate):
    return sum(cash / (1 + rate) ** year for year, cash in enumerate(cash_flows))
def derivative(rate):
    return sum(-year * cash / (1 + rate) ** (year + 1) for year, cash in enumerate(cash_flows) if year)

newton = root_scalar(npv, x0=0.1, fprime=derivative, method="newton")
secant = root_scalar(npv, x0=0.05, x1=0.2, method="secant")
print(f"Newton interest rate: {newton.root:.6%}; NPV={npv(newton.root):.3e}")
print(f"Secant interest rate: {secant.root:.6%}; NPV={npv(secant.root):.3e}")
