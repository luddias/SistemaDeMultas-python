#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MultasDeTransito.py
#  
#  Copyright 2021 Ludmila Dias
#  
# ----------------------------------------------------------------------

#IMPORTAÇÃO DE BIBLIOTECAS
import os
import pickle

#FUNÇÃO PARA LIMPAR A TELA
def limpaTela():
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")

#FUNÇÃO QUE SALVO OS DADOS DO RECORDE
def salvarDados(m,v,i,n): 
    with open("multas.bin", "wb") as f:
        pickle.dump(m,f)
        pickle.dump(v,f)
        pickle.dump(i,f)
        pickle.dump(n,f)

#FUNÇÃO PARA LER OS DADOS SALVOS DE RECORDE
def lerDados(m,v,i,n): 
    if os.path.isfile("multas.bin"):
        with open("multas.bin", "rb") as f:
            m=pickle.load(f)
            v=pickle.load(f)
            i=pickle.load(f)
            n=pickle.load(f)
    else:
        m={}
        v={}
        i=[]
        n={}

    return m,v,i,n

#FUNÇÃO PARA CADASTRO DO MOTORISTA
def cadastrarMotorista(motoristas):
    dataNasc=()
    limpaTela()
    cnh=input("digite a CNH: ")
    
    if verificarDicionario(cnh,motoristas)==True:
        print("Erro: CNH já cadastrado.")
    else:
        nomeMotorista= input("Insira o nome do motorista: ")
        print("Insira a sua data de nascimento: ")
        dia=int(input("DIA: "))  
        mes=int(input("MÊS: "))
        ano=int(input("ANO: "))
        dataNasc=(dia,mes,ano)
        motoristas[cnh]=(nomeMotorista,dataNasc)
        limpaTela()
        print("Motorista Cadastrado com sucesso!\n")

#FUNÇÃO PARA ALTERAR O PROPRIETARIO DE UM VEICULO
def alterarProprietario(veiculos, motoristas):
    
    placaDesejada=input("Insira a placa do veiculo: ")
    CNHnovoProp=input("Digite a CNH do novo proprietário: ")
    if verificarDicionario(placaDesejada, veiculos)==False and verificarDicionario(CNHnovoProp, motoristas)==False:
        limpaTela()
        print("Erro: Veiculo e Motorista não cadastrados.")
    elif verificarDicionario(placaDesejada, veiculos)==False:
        limpaTela()
        print("Erro: Veiculo não cadastrado.")
    elif verificarDicionario(CNHnovoProp, motoristas)==False:
        limpaTela()
        print("Erro: Motorista não cadastrado.")
    else:
        _, modelo, cor= veiculos[placaDesejada]
        veiculos[placaDesejada]=(CNHnovoProp,modelo,cor)
        limpaTela()
        print("Novo proprietario cadastrado com sucesso!")

#FUNÇÃO PARA VERIFICAR UMA INFORMACAO NO DICIONARIO
def verificarDicionario(info,dicionario):
    if info in dicionario:
        return True
    else:
        return False

#FUNÇÃO PARA CADASTAR UM VEICULO
def cadastrarVeiculo(veiculos):
    limpaTela()
    placa=input("digite a Placa do Veiculo: ")
    
    if verificarDicionario(placa,veiculos)==True:
        print("Erro: Placa já cadastrada.")
    else:
        cnhProprietario= input("Insira o CNH do proprietario: ")
        modelo=input("Insira o modelo do veiculo: ")
        cor=input("Insira a cor do veiculo: ")
        veiculos[placa]=(cnhProprietario, modelo,cor)
        limpaTela()
        print("Veiculo Cadastrado com sucesso!\n")

#FUNCAO PARA CADASTRAR UMA FUNCAO
def CadInfracoes(infracoes,naturezas):
    TuplaInfracao=()

    if len(infracoes)>0:
        # ultimo=infracoes[len(infracoes)-1]
        numInfracao,_,_,_=infracoes[(len(infracoes)-1)]
        numInfracao+=1
    else:
        numInfracao=0
    limpaTela()
    print("Insira a sua data da infracao: ")
    dia=int(input("DIA: ")) 
    mes=int(input("MÊS: "))
    ano=int(input("ANO: "))
    dataInfracao=(dia,mes,ano)
    placaInfracao=input("Insira a placa do veiculo: ")
    naturezaInfracao=int(input('''
    Insira o numero respectivo a natureza da infracao:

    1. Infracao Leve
    2. Infracao Media
    3. Infracao Grave
    4. Infracao Gravissima
    '''))

    if naturezaInfracao==1:
        TuplaInfracao=(numInfracao,dataInfracao,placaInfracao,"Leve")
    elif naturezaInfracao==2:
        TuplaInfracao=(numInfracao,dataInfracao,placaInfracao,"Media")
    elif naturezaInfracao==3:
        TuplaInfracao=(numInfracao,dataInfracao,placaInfracao,"Grave")
    elif naturezaInfracao==4:
        TuplaInfracao=(numInfracao,dataInfracao,placaInfracao,"Gravissima")

    infracoes.append(TuplaInfracao)
    limpaTela()
    print("Cadastro de nova infração efetuado com sucesso!")

#FUNCAO PRINCIPAL
def main():

    veiculos = {}
    infracoes = []
    naturezas = {}
    motoristas = {}
    menu='''
    Digite o número correspondente a ação que deseja realizar: 
    
    1. Cadastrar um novo motorista
    2. Cadastrar um novo veículo
    3. Alterar proprietário de um veículo
    4. Cadastrar uma nova infração
    5. Sair
    '''

    motoristas,veiculos,infracoes,naturezas=lerDados(motoristas,veiculos,infracoes,naturezas)
    opcao=int(input(menu))

    while opcao !=5:
        if opcao==1:
            cadastrarMotorista(motoristas)
        elif opcao==2:
            cadastrarVeiculo(veiculos)
        elif opcao==3:
            alterarProprietario(veiculos,motoristas)
        elif opcao==4:
            CadInfracoes(infracoes,naturezas)

        opcao=int(input(menu))

    salvarDados(motoristas,veiculos,infracoes,naturezas)

if __name__=='__main__':
    main()
