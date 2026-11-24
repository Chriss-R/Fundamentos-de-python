def resolverEcuacion ( a,b,c):
    xPositivo = (-b +(b**2- 4*a*c)**(1/2)) / (2*a)
    print(xPositivo)
    xNegativa = (-b -(b**2- 4*a*c)**(1/2)) / (2*a)
    print(xNegativa)
    print("La ecuacion tiene dos soluciones: ", round(xPositivo, 2), "y", round(xNegativa, 2))
resolverEcuacion(4,12,2)
