# mandatory assignment 1
# exercise 2, solve eq(148) and eq(150) using both Picard and Newton iterations
# Use coupled system of equations for H and F
"""
toggle the solve function between H13 and H23 depending on
what equation set you wish to solve.
"""

from dolfin import *

L = 4

mesh = IntervalMesh(100, 0, L)
V = FunctionSpace(mesh, 'CG', 1)
W = MixedFunctionSpace([V, V])      # W = V*V

def start(x, on_boundary):
    return near(x[0], 0) and on_boundary
def end(x, on_boundary):
    return near(x[0], L) and on_boundary

BC = [DirichletBC(W.sub(0), 0, start), 
      DirichletBC(W.sub(1), 0, start), 
      DirichletBC(W.sub(0), 1, end)]

HFt = TestFunction(W)
HF_ = Function(W)

Ht, Ft = split(HFt)
H_, F_ = split(HF_)

H1 = -inner(grad(H_), grad(Ht))*dx + F_*H_.dx(0)*Ht*dx + Ht*dx - H_*H_*Ht*dx
H2 = -inner(grad(H_), grad(Ht))*dx + 2*F_*H_.dx(0)*Ht*dx + Ht*dx - H_*H_*Ht*dx
H3 = H_*Ft*dx - F_.dx(0)*Ft*dx

H13 = H1+H3
H23 = H2+H3

solve(H23 == 0, HF_, BC)
#wiz = plot(F_, interactive=False)
#wiz.write_png("ex2_newton_2")
plot(F_, interactive=True)

