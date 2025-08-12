"""Função é um bloco de código que executa uma tarefa específica e 
pode ser reutilizado sempre que você precisar como uma "receita" 
que você chama pelo nome, em vez de escrever o mesmo código 
várias vezes."""
#1️⃣ Estrutura básica de uma função

"""def nome_da_funcao(parametros_opcionais): # → palavra-chave para dizer “estou criando uma função”
    # nome_da_funcao → nome que você escolhe para chamar essa função depois.
    # parametros_opcionais → valores que você pode passar para a função trabalhar.
    # código que a função executa
    return resultado_opcional # → envia um resultado de volta (opcional)."""
    

def saudacao():
    print("Olá! Seja bem-vindo(a).")

# Chamando a função
saudacao()

#2️⃣ Parâmetros e argumentos

def somar (a, b):
    resultado = a + b
    return resultado

print(somar(5, 3)) # saída: 8	

#3️⃣ Vantagens de usar funções
"""Organização → seu código fica mais limpo.

Reutilização → você escreve uma vez e usa várias.
Facilidade de manutenção → 
se precisar mudar algo, muda só na função."""