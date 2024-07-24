import pulp

model = pulp.LpProblem("Model Name", pulp.LpMinimize)  # Мінімізація
# або
model = pulp.LpProblem("Model Name", pulp.LpMaximize)  # Максимізація

x = pulp.LpVariable('x', lowBound=0, cat='Continuous')  # x ≥ 0
y = pulp.LpVariable('y', 3, 7)        # 3 ≤ y ≤ 7

model += 2 * x + 3 * y, "Problem"  # Мінімізувати або максимізувати 2x + 3y

model += x + 2 * y <= 8, "Constraint1"
model += y >= 2, "Constraint2"

model.solve()
pulp.LpStatus[model.status]

for variable in model.variables():
    print(f"{variable.name} = {variable.varValue}")

# Вартість цільової функції
print(f"Total cost = {pulp.value(model.objective)}")
