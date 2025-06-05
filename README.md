# exercício-mapa
Resolver os problemas encontrados no código

# 🐄 Sistema de Controle de Fila — Açougue Bom Preço

Este repositório contém um exercício prático sobre **estrutura de dados do tipo Fila (FIFO)** com aplicação em um sistema real de atendimento, desenvolvido como parte de um estudo sobre boas práticas e organização de filas utilizando a linguagem Python.

---

## 📚 Parte 1 — Contextualização Teórica

A **Fila** é uma estrutura de dados fundamental que segue o princípio FIFO (*First In, First Out*), onde o primeiro elemento a entrar é o primeiro a sair. Segundo Cormen et al. (2012, p. 238):

> “As filas são estruturas fundamentais que permitem organizar dados em uma sequência linear, possibilitando operações de inserção em uma extremidade e remoção em outra.”

Seu uso é essencial em contextos como:
- Sistemas de atendimento (hospitais, bancos, supermercados)
- Filas de impressão
- Processamento de tarefas

> “O uso adequado das filas proporciona um controle eficiente no fluxo de dados ou de pessoas, melhorando a experiência do usuário e otimizando os processos de atendimento.”  
> — Ziviani (2011, p. 54)

---

## 🧪 Parte 2 — Estudo de Caso

O **Supermercado Bom Preço** enfrentava confusões no setor do açougue por falta de organização no atendimento. O gerente, Sr. Cláudio Menezes, solicitou um sistema simples para retirada de senhas, de forma que os clientes fossem chamados por ordem de chegada.

Um aluno chamado **Murilo Luz** desenvolveu uma versão funcional inicial, porém com diversos problemas no código.

---

## ❌ Problemas Identificados no Código Original

1. Linha 22: Sempre reiniciava o contador de senha com 1.  
   🔧 **Correção**: `contador_senha += 1` para gerar novas senhas sequenciais.
2. Linha 24: Método incorreto `fila.end()`.  
   🔧 **Correção**: Substituído por `fila.append(senha)`.
3. Linha 30: `popleft()` usado sem referenciar a fila.  
   🔧 **Correção**: Utilizado `senha_chamada = fila.popleft()`.
4. Linha 38: `fila.list` não existe.  
   🔧 **Correção**: Utilizado `print(fila)` para mostrar a fila atual.

---

🛠 Tecnologias Utilizadas

Python 3.10+

Módulo collections.deque

📁 Como Executar

bash
Copiar
Editar
git clone https://github.com/seu-usuario/fila-acougue.git
cd fila-acougue
python fila_acougue.py

📖 Referências

CORMEN, T. H.; LEISERSON, C. E.; RIVEST, R. L.; STEIN, C. Algoritmos: Teoria e Prática. 3. ed. Rio de Janeiro: Elsevier, 2012.

ZIVIANI, N. Projeto de Algoritmos: com Implementações em Pascal e C. 3. ed. Cengage Learning, 2011.

✍️ Autor

Desenvolvido por Rômulo Echevenguá como exercício prático de estrutura de dados em Python.
