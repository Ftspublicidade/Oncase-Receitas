# Oncase-Receitas
Repositório com todos os arquivos e códigos utilizados para realizar o desafio.

## Critérios

Avaliaremos - os quesitos não estão necessariamente em ordem de prioridade:

* Sua capacidade na compreensão e modelagem dos dados e problbemas;
* Qualidade e proeficiência codificando na linguagem de sua escolha (R, Python);
* Qualidade das soluções encontradas para responder às perguntas;
* Comunicação na hora de questionar itens que não estejam claros;
* Comunicação visual eficaz (escrita e gráficos) no embasamento as respostas;
* Utilização de métodos adequados para cada problema;
* Análise de estudo e performance quando a resposta envolver a criação de modelos;

Conta ponto também:

* Aspectos de organização de código;
* Aspectos que demonstrem alguma maturidade em Data engineering/DataOps
* Repetibilidade do notebook


# Exercício: Arquivo: receitas.json - Sample ao final

1. A categorias pertencem as comidas mais calóricas?
2. Quais os top 10 ingredientes contidos nas receitas mais calóricas?
3. Se você tivesse que recomendar 3 receitas baseando-se nos dados, quais seriam?
4. Alguma característica presente nos dados determina a alta nota de uma receita?
5. Considerando-se as categorias das top 100 receitas em avaliação, quantas receitas há atualmente no site https://www.epicurious.com para cada categoria.
6. [opcional] Construa um classificador para recomendar tags (categorias) para as receitas;

Sample:

```json
{
  "directions": [
    "Heat 2 tablespoons oil in heavy ...",
    "Place flour in shallow dish...",
    "Meanwhile, cook pasta in large pot of ...",
    "A dried herb ...."
  ],
  "sodium": 517,
  "date": "2004-08-20T04:00:00.000Z",
  "calories": 631,
  "categories": [
    "Milk/Cream",
    "Citrus",
    "Dairy",
    "Fish",
    "Garlic",
    "Pasta",
    "Sauté",
    "Quick & Easy",
    "Orange",
    "Snapper",
    "Summer",
    "Pan-Fry",
    "Bon Appétit"
  ],
  "desc": "Sharon Hooykaas of Los Alamitos, ...",
  "protein": 45,
  "fat": 24,
  "rating": 4.375,
  "title": "Snapper on Angel Hair with Citrus Cream ",
  "ingredients": [
    "4 tablespoons olive oil",
    "4 shallots, thinly sliced (about 1/2 cup)",
    "2 garlic cloves, chopped",
    "1 8-ounce bottle clam juice",
    "3/4 cup whipping cream",
    "1/2 cup white wine",
    "1/2 cup fresh orange juice",
    "2 tablespoons diced drained oil-packed sun-dried tomatoes",
    "1 tablespoon fresh lime juice",
    "1 teaspoon herbes de Provence* or salad herbs",
    "1 teaspoon Worcestershire sauce",
    "1/2 teaspoon grated orange peel",
    "1/2 teaspoon grated lime peel",
    "All purpose flour",
    "4 5- to 6-ounce red snapper fillets",
    "8 ounces angel hair pasta",
    "2 tablespoons thinly sliced fresh basil",
    "Additional minced orange peel"
  ]
}
```

#### Para finalizar gostaria de informar que essa solução pode ser melhorada, como por exemplo, conversando com uma pessoa da área do negócio, que nesse caso saõ alimentos e suas informações nutricionais, podendo assim, aplicar técnicas como substituição dos valores nulos por um número muito próximo da realidade. Podemos até mesmo aplicar ténicas estatísticas mais avançadas. Em um trabalho de ciência de dados é muito importante a participação do especialista do negócio para subsidiar o cientista de dados de informações que ele por não ser da área não possui conhecimento, evitando assim, as chances de criar um modelo ou relatório enviesado.
#### Com relação a questão opcional, devido ao tempo não foi possível criar a solução mas poderia ter sido feita aplicando técnicas de NLP para o tratamento das features e em seguida testando alguns classificadores através de pipelines e verificando qual obteve uma melhor acurácia, podendo aplicar uma engenharia de features caso o comportamento dos classificadores não estejam se saindo bem.


