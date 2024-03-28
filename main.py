"""
Author: Adriano da Silva Angioletto


Questões - Target Sistemas

Agradeço a oportunidade, minha meta e melhorar cada vez mais!, dar o sangue, já que programação pramim é amor,
e tenho muita vontade de aprender, e curiosidade, não se trata sómente de salario, e sim de gostar do que faço,
minha meta e ficar na empresa, e subir para JR, solucionando problemas, e  sendo criativo!


"""

class Target:
    
    
    def pergunta_1(self) -> None:
              
        indice : int = 13
        soma : int = 0
        k : int = 0
        
        while(k < 13):
            
            k = k+1
            
            soma = soma+k
                  
        print(soma)  # resultante 91
        
    def pergunta_2(self) -> None:
        
        entrada = input('Digite um Numero') # se espera um int mas nunca vem né? kk..
        
        try:
            
            entrada_int : int = int(entrada) 
        
            
        except:  # criei except genérico pq nesse caso, não há necessidade de ser especifico.
            
            print('por favor digite apenas numeros')
            
            return # só pra não dar continuação no codigo.
            
            
        fibonacci: list = [0, 1]
        
        while fibonacci[-1] < entrada_int:
            
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

        print('Sequência de Fibonacci:', fibonacci)
        
        
        
    def pergunta_3(self) -> None:
        
        """ Respostas, em dict, assim fica mais legivel, estão em sequencia."""
        
        respostas : dict = {
        'pergunta_a': [1, 3, 5, 7, 9],
        'pergunta_b': [2, 4, 8, 16, 32, 64, 128],
        'pergunta_c': [0, 1, 4, 9, 16, 25, 36, 49],
        'pergunta_d': [4, 16, 36, 64, 100],
        'pergunta_e': [1, 1, 2, 3, 5, 8, 13],
        'pergunta_f': [2, 10, 12, 16, 17, 18, 19]
        
        }
        
        
        
        flag = True
                
        while flag:
            
            quer_saber = input('Quer ver o resultado das Perguntas? S/N: ').upper()
         
            if quer_saber == 'S':
               
                print(respostas)
               
                flag = False
                
                   
            elif quer_saber == 'N':
             
                print('Tchau :)')
             
                flag = False
                
              
                
            else:
                
                print('Resposta inválida. Digite apenas S ou N.')
                
                flag = True

                        
                    

            

        
    def pergunta_4(self)-> None:
            
            """ aqui terá somente a resposta, em texto"""
            
            """ 
            
            Acredito que isso seria um algoritmo lógico interessante. Algumas pessoas poderiam demorar um pouco para descobrir isso na prática, 
            mas ao longo do tempo fariam isso para otimizar o tempo. Afinal, com a prática, nós humanos temos essa tendência de descobrir 'macetes'. 
            Então, acredito que todos nós teríamos o mesmo resultado, mais cedo ou mais tarde.
            
            la vamos nós:
            
            
            a gente, liga o primeiro interruptor por algum tempo só para ele esquentar, depois desligamos o mesmo.
            agora ligamos o segundo interruptor.
            
            na segunda ida, vamos até sala das lâmpadas, a que eu deixei acesa, é claramente do segundo interruptor
            já a que está " quente " pelo fato de eu ter deixado ligado um tempo, é o primeiro interruptor!. já 
            o terceiro interruptor, por já ter cido eliminado tanto o primeiro, como o segundo, só sobra um então é ele.
            
            
            
            
            """
            
        
    def pergunta_5(self) -> None:
        
        entrada_texto = input('Digite uma string: ')

        try:
            self.entrada_texto_edit = float(entrada_texto)
            
            if isinstance(self.entrada_texto_edit, float):
                
                print("digitou numeros Por favor, digite apenas uma string.")    
                
        except: 
                      
            string_invertida = ''
            
            """
            revertendo a string, com -1 e range, seria bem mais facil com reverse ::
            porem foi dito que era pra evitar.. então ai está solução
            
            """
            for i in range(len(entrada_texto) - 1, -1, -1):  
                                                            
                
                string_invertida += entrada_texto[i]
                

            print("String invertida:", string_invertida)

                   
               
cla = Target()

cla.pergunta_1()

cla.pergunta_2()

cla.pergunta_3()

# cla.pergunta_4() só para ficar organizado, como é so texto não preciso invocar o  metodo.

cla.pergunta_5()