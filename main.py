import pymysql.cursors


#CONEXÃO
def criar_conexao ():
    #Faça as mudanças necessarias para rodar em seu BD no sql
    try:
        conexao = pymysql.connect(
            host= 'localhost',
            user= 'root',
            password= '',
            database= 'loja',
            cursorclass= pymysql.cursors.DictCursor
        )

        print('Conexão criada com sucesso')
        return conexao
    except Exception as error:
        print(f'Falha na conexão!! Erro: {error}')




# Cursor

def inserir_produto(nome: str, preco: float, categoria: str):
    #Faça as mudanças necessarias para rodar em seu BD no sql

    try: 
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'INSERT INTO produtos (nome, preco, categoria) VALUES (%s, %s, %s)'
        cursor.execute(sql, (nome, preco, categoria))
        conn.commit()
        print('Dados inseridos com sucesso.')

    except Exception as error:
       
       print(f'Falha na conexão!! Erro: {error}')



def listar_produtos():
    #Faça as mudanças necessarias para rodar em seu BD no sql
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'SELECT * FROM produtos'
        cursor.execute(sql)
        dados = cursor.fetchall()
        print(dados)

    except Exception as error:
       
       print(f'Falha na conexão!! Erro: {error}')



def deletar_produto(id):
    
#Faça as mudanças necessarias para rodar em seu BD no sql
    try: 
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'DELETE FROM produtos WHERE codigo = %s'
        cursor.execute(sql, (id))
        conn.commit()
        print('Dados deletados com sucesso.')

    except Exception as error:
       
       print(f'Falha na conexão!! Erro: {error}')




def update_produto(nome: str,categoria: str, preco: float,codigo: int ):
    #Faça as mudanças necessarias para rodar em seu BD no sql

    try: 
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'UPDATE produtos SET nome = %s, categoria = %s, preco = %s WHERE codigo = %s'
        cursor.execute(sql, (nome,  categoria, preco, codigo))
        conn.commit()
        print('Dados alterados com sucesso.')

    except Exception as error:
       
       print(f'Falha na conexão!! Erro: {error}')


def listar_produtos_codigo(id):
    #Faça as mudanças necessarias para rodar em seu BD no sql
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'SELECT * FROM produtos WHERE codigo = %s'
        cursor.execute(sql,(id))
        dados = cursor.fetchall()
        print(dados)

    except Exception as error:
       
       print(f'Falha na conexão!! Erro: {error}')





#deletar_produto(1)
#listar_produtos()
#inserir_produto('asus notbook',3300.00,'laptop')
#update_produto('placa de video','periferico',799.99,2)
#listar_produtos_codigo(3)