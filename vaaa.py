x=[2,4,6]
y=[50,70,60]
m=(y[1]-y[0])/(x[1]-x[0])
c=y[0]-(m*x[0])
print("Slope:", m)
print("Intercept:", c)
def predict(x):
    return(m*x)+c

print("Score for 3 hours:", predict(3))
print("Score for 5 hours:", predict(5))
