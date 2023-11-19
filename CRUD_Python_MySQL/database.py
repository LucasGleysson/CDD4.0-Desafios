import mysql.connector

campos_bases = {
    "alunos": {
        "campos": ["nome", "cpf", "idade", "telefone", "email"],
        "val": "%s,%s,%d%,%s,%s",
    },
    "funcionario": {
        "campos": ["nome", "cpf", "idade", "telefone", "email"],
        "val": "%s,%s,%d%,%s,%s",
    },
    "personal": {
        "campos": ["nome", "cpf", "cref", "endereco", "email", "telefone"],
        "val": "%s,%s,%s,%s,%s,%s",
    },
    "modalidades": {"campos": ["nome", "turno", "duracao"], "val": "%s,%s,%s"},
}


def open_db():
    banco = mysql.connector.connect(
        host="localhost", user="root", password="12345", database="academiaturmac"
    )
    return banco


def create_cursor(banco):
    cursor = banco.cursor()
    return cursor


def close_cursor(cursor):
    cursor.close()


def close_banco(banco):
    banco.close()


def creater(op_tabela):
    banco = open_db()
    cursor = create_cursor(banco)

    # Dados
    nome = input("Nome: ")
    cpf = input("CPF:")
    idade = input("Idade: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    dados = (nome, cpf, idade, telefone, email)

    # Query
    tabela = campos_bases[op_tabela]
    campos = ", ".join(tabela["campos"])
    val = tabela["val"]
    sql = f"INSERT INTO {op_tabela} ({campos}) VALUES ({val})"

    # Commit
    cursor.execute(sql, dados)
    banco.commit()
    novo_id = cursor.lastrowid

    close_cursor(cursor)
    close_banco(banco)
    return novo_id


def reader(op_tabela):
    banco = open_db()
    cursor = create_cursor(banco)

    # Query
    tabela = campos_bases[op_tabela]
    sql = f"SELECT * from {op_tabela};"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    close_cursor(cursor)
    close_banco(banco)


def delete(op_menu_tabela):
    return None
