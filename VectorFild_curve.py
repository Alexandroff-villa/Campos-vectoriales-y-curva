
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

sp.init_printing()
X, Y, t = sp.symbols('X Y t')

class VectorFielf():
    def __init__(self,xinf,xsup,yinf,ysup):
        self.x = np.linspace(xinf,xsup,40)
        self.y = np.linspace(yinf,ysup,40)

    def mallado(self,U,V):
        self.X, self.Y = np.meshgrid(self.x,self.y)
        self.U = sp.parse_expr(U)
        self.V = sp.parse_expr(V)
        U = np.zeros((40,40))
        V = np.zeros((40,40))
        for i in range(len(self.x)):
            for j in range(len(self.y)):
                xij = self.U.subs([(X,self.X[i,j]),(Y,self.Y[i,j])])
                yij = self.V.subs([(X,self.X[i,j]),(Y,self.Y[i,j])])
                U[i,j] = xij
                V[i,j] = yij

        return self.X, self.Y, U, V

class Curvas():
    def __init__(self,tinf,tsup,Xt,Yt):
        self.t = np.arange(tinf,tsup,0.1)
        self.Xt = sp.parse_expr(Xt)
        self.Yt = sp.parse_expr(Yt)

    def curva(self):
        Xt = np.zeros(len(self.t))
        Yt = np.zeros(len(self.t))
        for i in range(len(self.t)):
            Xt[i]=self.Xt.subs(t,self.t[i])
            Yt[i]=self.Yt.subs(t,self.t[i])
        return Xt, Yt

    


if __name__ == '__main__':
    campo = VectorFielf(-4,4,-4,4)
    X, Y, U, V = campo.mallado("Y","-X")
    curva = Curvas(-1.4,1.4,"t","t")
    xt, yt = curva.curva()
    plt.quiver(X,Y,U,V, linewidth=0.1,color='b')
    plt.plot(xt,yt,c="r")
    plt.title("vector field")
    plt.show()