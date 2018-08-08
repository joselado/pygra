
# module to handle different types of data 
import matplotlib.pyplot as plt



class Band():
  """ Data of a band structure"""
  dimension = 1
  x = []
  y = []
  z = None
  def plot(self):
    fig = plt.figure() # new figure
    fig.set_facecolor("white") # panel in white
    fig.scatter(self.x,self.y) # plot the data
    return fig
  def show(self):
    fig = self.plot() # get the figure
    plt.show() # show figure



