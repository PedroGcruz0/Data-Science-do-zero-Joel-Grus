from matplotlib import pyplot as pt

years =[1970,1890,1578,1859]
gdp = [122.2,345.1,567.5,678.1]

pt.plot(years,gdp,color= 'green', marker ='o',linestyle='solid')
pt.title("Titulo do Gráfico")
#adicionar um rótulo no eixo y
pt.ylabel("Billions")
pt.show()


