import os
import time

#Funções 
    #Função cadastrar-------------------------------------------------
def cadastrar():
    nome_empresa = input('Digite o nome da empresa: ')
    cnpj = input('Digite sua cnpj: ')
    uf = input('Insira sua UF: ')
    t = int(input('Digite seu telefone: '))
    e = input('Digite seu email: ')
    agenda = open('%s_%s.txt' %(nome_empresa,cnpj),'a')
    agenda.write('%s %s,%s, %d, %s\n'%(nome_empresa, cnpj, uf, t, e))
    agenda.close()
    
    #Função Buscar---------------------------------------------------
    
def buscar():
    nome_empresa = input('Digite o nome da empresa a ser pesquisado: ')
    cnpj = input('Digite a cnpj do contato a ser pesquisado: ')

    if os.path.isfile('%s_%s.txt'%(nome_empresa,cnpj)):
          agenda = open('%s_%s.txt'%(nome_empresa,cnpj),'r')
    
          for x in agenda.readlines():
                print(x)
          agenda.close()

    else:
       print('Contato não encontrado.') 
    
    #Função deletar-------------------------------------------------
    
def deletar():
    nome_empresa = input('Digite o nome que deseja apagar: ')
    cnpj = input('Digite o sobrenome que deseja apagar: ')
    os.remove('%s_%s.txt'%(nome_empresa, cnpj))

    #Função MENU---------------------------------------------------
def main():
    print(' MENU')
    print('1. Cadastrar')
    print('2. Buscar')
    print('3. Apagar')
    print('0. Sair')
    op = 1
    while op!=0:
        op = int(input('\nDigite a opção: '))
        if op==1:            
            cadastrar()            
        elif op==2:
            buscar()
        
        elif op==3:
            deletar()            
        elif op==0:
            print('Programa finalizado.')
            break
        else:
            print('Opção incorreta, tente novamente. ')
main()