# import pulp 
# import pandas as pd
# import pulp.solverdir
# import logging

import numpy as np
print(np.__version__)

# problem = pulp.LpProblem("simple_LP_problem",pulp.LpMaximize)
# x= pulp.LpVariable("x",lowBound=0)
# y= pulp.LpVariable("y",lowBound=0)

# problem+= 4 * x + 3 * y

# problem+= 2*x+y<=20
# problem += 4*x-5*y>=-10
# problem += -x+2*y>=-2

# solver = pulp.PULP_CBC_CMD(msg=True)

# problem.solve(solver)

# print(f"status:{pulp.LpStatus[problem.status]}")
# print(f"x = {pulp.value(x)}")
# print(f"y={pulp.value(y)}")
# print(f"objective:{pulp.value(problem.objective)}")
# # print(f"")

