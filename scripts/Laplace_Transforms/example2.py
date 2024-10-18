from sympy import cos,sin,symbols,laplace_transform
import control as ctrl

# Define the function
#g(t)=4cos(4t)−9sin(4t)+2cos(10t)

t, s = symbols('t s')
g = 4*cos(4*t) - 9*sin(4*t) + 2*cos(10*t)
print(g)

# Compute the Laplace transform
G = laplace_transform(g, t, s)
# G = ctrl.laplace_transform()
print('G(s) = ', G)
print(G)