class Resultado:
    def __init__(self,array,valor):
        self.conjunto=array
        self.valor=valor
        self.resultado=[]
        self.sumaResto=self.sumaInicial()
        #print self.subconjunto
        subconjunto=[]
        self.solucion(0,0,self.sumaResto,subconjunto)
        print self.resultado
    def sumaInicial(self):
        suma = 0
        for i in range(0,len(self.conjunto)):
            suma+=self.conjunto[i]
        return suma
    #def formatoConjunto(self,conjunto):
    #   array=[]
    #  for in in
    def solucion(self,indiceBusqueda,total,resto,conjunto):
        if((total+resto>=self.valor) and  (total<=self.valor)):
            if(total==self.valor):
                self.resultado.append(conjunto)
            for i in range(indiceBusqueda,len(self.conjunto)):
                nuevoConjunto=conjunto+[i]
                resto-=self.conjunto[i]
                self.solucion(i+1,total+self.conjunto[i],resto,nuevoConjunto)
            
        
            
            
    


conjunto= [3, 34, 4, 12, 5, 2]
valor = 9

Resultado(conjunto,valor)

