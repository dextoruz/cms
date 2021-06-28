import math

import random
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
class MonteCarloSimulation:
    def __init__(self):
        self.cardsDeck = [
                'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
                'AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
                'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC',
                'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD'
            ]
    def monte_carlo_simulation(self, func, xmin, xmax):
        numSteps = 100000
        ymin = func(xmin)
        ymax = ymin
        for i in range(numSteps):
            x = xmin + (xmax - xmin) * i/numSteps
            y = func(x)
            if y < ymin: ymin = y
            if y > ymax: ymax = y

        rectArea = (xmax - xmin) * (ymax - ymin)
        numPoints = 100000
        ctr = 0
        for j in range(numPoints):
            x = xmin + (xmax - xmin) * random.random()
            y = ymin + (ymax - ymin) * random.random()
            if func(x) > 0 and y > 0 and y <= func(x):
                ctr += 1
            if func(x) < 0 and y < 0 and y >= func(x):
                ctr += 1

        area = rectArea * float(ctr) / numPoints
        return area


    def cos(self,x):
        return math.sqrt((math.cos(x)**2) + 1)
        
    def epsilon(self,x):
        return(math.e**(x**2))
        
    def volume_sphere(self,N):
    
        radius = 1
        volume_cube = 2*2*2
        ctr = 0

        for i in range(N):
            x = round(random.uniform(-1, 1), 2)
            y = round(random.uniform(-1, 1), 2)
            z = round(random.uniform(-1, 1), 2)

            distance = math.sqrt(x**2 + y**2 + z**2 )

            if distance < radius :
                ctr += 1
        
        volume = (ctr/N) * volume_cube
        
        return volume

    def estimate_integral(self, n):
        '''
        
        h(x) ==> sin(x^2)
       x range => 0-8
       y range => -1 - 1
       
        '''
        ymin = -1
        ymax = 1
        
        xmin = 0
        xmax = 8
        
        target_area =(1) * (ymax - ymin)
        count = 0
        
        for i in range(n):
            x = round(random.uniform(xmin, xmax), 2)
            y = round(random.uniform(ymin, ymax), 2)
            
            real_y = math.sin(x**2)
            
            if y >= 0 and real_y >= 0:
                if y <= real_y:
                    count += 1
            if y < 0 and real_y < 0:
                if y > real_y:
                    count += 1
                    
        area = (count/n) * target_area
        return area

    def monte_carlo_deck_of_cards(self, cards='Q'):
            
        random.shuffle(self.cardsDeck)
        success = 0
        for i in range(len(self.cardsDeck)-1):
            if cards == 'Q_K':
                if ((self.cardsDeck[i][0] == 'Q' and self.cardsDeck[i+1][0] == 'K') or (self.cardsDeck[i][0] == 'K' and self.cardsDeck[i+1][0] == 'Q')):
                    success += 1
            if cards == 'Q':
                if self.cardsDeck[i][0] == 'Q' and self.cardsDeck[i+1][0] == 'Q':
                    success += 1

        return success

    def get_probability(self, N, cards='Q'):
        success = 0
        for i in range(N):
            success += self.monte_carlo_deck_of_cards(cards)
        print("Cards: {}, Iterations: {}, Probability: {}".format(cards, N, success/N))
        return success/N

    def start(self):

        area = self.monte_carlo_simulation(self.cos, 0, 2)
        print("a) Area (using cos function): {} unit^2".format(area))
        area = self.monte_carlo_simulation(self.epsilon, 0, 1)
        print("b) Area (using epsilon): {} unit^2".format(area))

        print("c) Volume of Sphere: {} unit^3".format( self.volume_sphere(10000)))
        print("d) Area (estimate integral): {} unit^2\n".format( self.estimate_integral(10000)))

        x, y = self.get_data_for_plot(self.get_probability, 'Q')
        x1, y1 = self.get_data_for_plot(self.get_probability, 'Q_K')

        self.plot([x,y,x1,y1])

    def get_data_for_plot(self, func, cards='Q'):
        x = []
        y = []
        
        for i in range(1, 20):  ## no of iterations
            x.append(1000*i)
            y.append(func(1000*i, cards))

        return x, y

    def plot(self, data): 

        plt.plot(data[0],data[1],color='b',label='Queen_Queen')
        plt.plot(data[2],data[3],color='g',label='Queen_King')
        plt.xlabel("N")
        plt.ylabel("Prob")
        plt.title("Probabilities and iterations")
        plt.legend()
        plt.savefig("prob-vs-n.jpeg")
        plt.show()

if __name__ == "__main__":
    obj = MonteCarloSimulation()
    obj.start()
    print("Observation: Running multiple times, the probability in each case has increased slightly\nas the number of iterations are increased.")
