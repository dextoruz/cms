

import matplotlib.pyplot as plt

class SimRomeoJuliet():
    def __init__(self):
        """
            Simulation Of Romeo And Juliet:
        
        """
        self.ROMEO = 20
        self.JULIET = 10
        self.SIM_LENGTH = 10
        self.DT  = 0.2
        self.iterations = int(self.SIM_LENGTH/self.DT)


    def set_values(self, data):
        
        self.R_a = data[0]
        self.R_b = data[1]
        self.J_c = data[2]
        self.J_d = data[3]

        
    def getValues(self,a,b,c,d,sL,dt):
        rom , jul,time = [],[],[0]
        R = self.R
        J = self.J
        rom.append(R)
        jul.append(J)
        
        iterations = int(sL/dt)
        for i in range(iterations):
            dR = (a*R + b*J)*dt
            dJ = (c*R + d*J)*dt
            R += dR
            J += dJ
            rom.append(R)
            jul.append(J)
            time.append(dt*(1+i))
        return time,rom,jul
    def get_values(self):
        romeo, juliet, t = [], [], [0]
        
        r = self.ROMEO
        j = self.JULIET
        
        romeo.append(r)
        juliet.append(j)
        
        for i in range(self.iterations):
            dR = (self.R_a * r + self.R_b * j) * self.DT
            dJ = (self.J_c * r + self.J_d * j) * self.DT
            
            r += dR
            j += dJ
            
            romeo.append(r)
            juliet.append(j)
            t.append( self.DT * (1+i) )
        
        return t, romeo, juliet
    
    def plot_1(self, x , y, title):

        plt.plot(x,y)
        plt.title(title)
        plt.ylabel('J(t)')
        plt.xlabel('R(t)')
        plt.savefig("1-" +title+".jpeg")
        plt.show()
            
        
    def plot_2(self, x, y, t, title):
        
        plt.plot(t,x,color='b',label='R(t)')
        plt.plot(t,y,color='r',label='J(t)')
        plt.xlabel("Time")
        plt.ylabel("R(t) / J(t)")
        plt.title(title)
        plt.legend()
        plt.savefig("2-" +title+".jpeg")
        plt.show()
    
    
if __name__ == "__main__":
    
    obj = SimRomeoJuliet()
    
    data = [5, 2, -2, -5]
    title = "Eager Beaver & Hermit Self Priority"
    obj.set_values(data)
    t , r, j = obj.get_values()
    obj.plot_2(r, j, t, title)
    obj.plot_1(r, j, title)
    
    
    data = [2, 5, -5, -2]
    title = "Eager Beaver & Hermit Others Priority"
    obj.set_values(data)
    t , r, j = obj.get_values()
    obj.plot_2(r, j, t, title)
    obj.plot_1(r, j, title)
    
    
    data = [5,-2, 2, -5]
    title = "Narcisstic Nerd & Cautious Lover Self Priority"
    obj.set_values(data)
    t , r, j = obj.get_values()
    obj.plot_2(r, j, t, title)
    obj.plot_1(r, j, title)
    
    
    data = [2, -5, 4, -2]
    title = "Narcisstic Nerd & Cautious Lover Others Priority"
    obj.set_values(data)
    t , r, j = obj.get_values()
    obj.plot_2(r, j, t, title)
    obj.plot_1(r, j, title)
    
    
    data = [0, 5, 3, 0]
    title = "Lovers"
    obj.set_values(data)
    t , r, j = obj.get_values()
    obj.plot_2(r, j, t, title)
    obj.plot_1(r, j, title)
    
    data = [0, -5, -3, 0]
    title = "Nerds"
    obj.set_values(data)
    t , r, j = obj.get_values()
    obj.plot_2(r, j, t, title)
    obj.plot_1(r, j, title)

    data = [0, -3, 3, 0]
    title = "Nerd and Lover"
    obj.set_values(data)
    t , r, j = obj.get_values()
    obj.plot_2(r, j, t, title)
    obj.plot_1(r, j, title)
    
        