
dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]
dados_quase = [10 , 20 , 30 , 40 , 50 , 15 , 25, 29, 39]

def limpar_dados () :
    pass

def calcular_media () :
    pass

def calcular_mediana(dados):
    sorted(dados)
    m = len(dados) / 2
    print(m)
    if not m.is_integer(): # Se esse valor não for um int
        mCerto = int(m) #Ele transforma em int
        print(mCerto)
        result = (dados[mCerto] + dados[mCerto+1]) / 2 #calcula a media desses dois
    else: result = m; pass
    print(f"A mediana destes dados é, {result}")

def calcular_variancia () :
    pass

def obter_extremos () :
    pass

calcular_mediana(dados_quase)
#dados = limpar_dados ( dados_sujos )

#print ( f" Dados processados : { dados }")
print(f"Arquivo auditado por: Matheus-Pieroni")