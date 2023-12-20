# exemplo para o calculo de raiz usando falsa posicao

def falsa_pos(f,x0,x1,eps):
    x2=x0 - f(x0)*(x1-x0)/(f(x1)-f(x0))
    while abs(f(x2))> eps:
        if (f(x0)*f(x2)>0): x0=x2
        else : x1=x2
        x2=x0 - f(x0)*(x1-x0)/(f(x1)-f(x0))
    return x2

def f(x):
    return x**2 - 1

print(falsa_pos(f, 0, 2, 0.001))