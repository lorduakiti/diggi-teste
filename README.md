# Diggi
Estudo de Caso - [Cientista de Dados]() - [diggi]()


## Objetivo:
Estudo de caso para que o candidato possa demonstrar seus conhecimentos de Ciência de Dados. A partir dos atributos apresentados é possível entender as características dos clientes, bem como a performance (inadimplência dos mesmos).  A performance dos clientes foi realizada através de backtest, seguindo a descrição de cada um dos atributos de performance. As informações confidenciais e de identificação dos clientes foram omitidas.

## Resultados:
[Apresentação - Versão 1.0](/Diggi%20-%20Estudo%20de%20Caso.pdf) 

[Exploração de Dados](/estudo_de_caso_diggi/analises/exploracao_de_dados.ipynb) 

[Exploração de Dados (Power BI)](/exploracao_de_dados.pdf) 

[Análise utilizando árvore de decisão](/estudo_de_caso_diggi/analises/analise_arvore_de_decisao.ipynb) 

[Análise utilizando árvore randômica](/estudo_de_caso_diggi/analises/analise_arvore_randomica.ipynb) 

[Análise com autoML](/estudo_de_caso_diggi/analises/analise_autoML.ipynb) 

[Análise de Classificação de Clientes](/estudo_de_caso_diggi/analises/analise_classificacao.ipynb) 




## Bases:
Para este teste utilize o seguinte dataset, considerando os arquivos listados a seguir, enviados junto a este teste:
* Base teste_Cientista de Dados_diggi.xlsx

## Descrição da Base:
O arquivo Excel que você recebeu possui uma amostra de 10 mil clientes com 19 atributos.  

## Descrição dos Atributos:
| # | Atributos | Descrição |
| ------ | ------ | ------ |
| 1 | N° do Cliente | Número interno de identificação do cliente |
| 2 | Safra | Data de aprovação do cliente |
| 3 | Estado | Estado de nascimento do cliente |
| 4 | Renda Mensal | Renda mensal estimada |
| 5 | Endividamento | Faixa de endividamento em relação ao salário mensal |
| 6 | Quantidade de Cheques sem Fundo |  |
| 7 | Quantidade de Restritivos |  |
| 8 | Valor dos Restritivos |  |
| 9 | Quantidade de Protestos |  |
| 10 | Valor dos Protestos |  |
| 11 | Modelo Score 1 | Pontuação do modelo (quanto maior melhor, ou seja, menor risco de crédito) |
| 12 | Modelo Score 2 | Pontuação do modelo (quanto maior melhor, ou seja, menor risco de crédito) |
| 13 | Modelo Score 3 | Pontuação do modelo (quanto maior melhor, ou seja, menor risco de crédito) |
| 14 | Modelo Score 4 | Pontuação do modelo (quanto maior melhor, ou seja, menor risco de crédito) |
| 15 | Performance 30D3M EVER | MAU = cliente apresentou atraso > 30 dias em 3 meses de observação |
| 16 | Performance 60D6M EVER | MAU = cliente apresentou atraso > 60 dias em 6 meses de observação |
| 17 | Performance 60D9M EVER | MAU = cliente apresentou atraso > 60 dias em 9 meses de observação |
| 18 | Performance 90D9M EVER | MAU = cliente apresentou atraso > 90 dias em 9 meses de observação |
| 19 | Performance 90D12M EVER | MAU = cliente apresentou atraso > 90 dias em 12 meses de observação |


## Entregáveis:
1. Storytelling: em poucos slides, preparar uma apresentação para descrever o processo de análise, etapas do estudo e resultados obtidos
2. Análise descritiva: apresentar uma análise descritiva da base
3. Árvore de decisão: aplicar a árvore de decisão para construir um algoritmo com o objetivo de reduzir a inadimplência dos clientes a serem aprovado. 

**Observação:** o principal objetivo do estudo de caso é construir um material que será utilizado para auxiliar na fase final de entrevista. Não existe resposta certa. A apresentação pode ser bastante simples, o mais importante são as técnicas que serão aplicadas. 
