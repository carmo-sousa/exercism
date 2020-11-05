# Tradução

Dado um diagrama, determine por quais plantas cada criança na classe do
jardim de infância é responsável.

A classe do jardim de infância está aprendendo sobre o cultivo de plantas.
O professor achou que seria uma boa ideia dar-lhes sementes de verdade,
plantá-las em terra de verdade e cultivar plantas de verdade.

Eles optaram por cultivar grama, trevo, rabanetes e violetas.

Para isso, as crianças colocaram copinhos ao longo do peitoril das janelas e
plantaram um tipo de planta em cada copo, escolhendo aleatoriamente entre os
tipos de sementes disponíveis.

```text
[janela][janela][janela]
........................ # cada ponto representa uma xícara
........................
```

Existem 12 crianças na classe:

Alice, Bob, Charlie, David,
Eva, Fred, Ginny, Harriet,
Ileana, Joseph, Kincaid e Larry.
Cada criança recebe 4 xícaras, duas em cada linha. A professora distribui
as xícaras para as crianças em ordem alfabética de seus nomes.

O diagrama a seguir representa as plantas de Alice:

```text
[janela][janela][janela]
VR......................
RG......................
```

Na primeira fila, mais próxima das janelas, ela tem uma violeta e um rabanete.
Na segunda linha ela tem um rabanete e um pouco de grama.

Seu programa receberá as plantas da esquerda para a direita, começando com a
linha mais próxima das janelas. A partir disso, ele deve ser capaz de determinar quais plantas pertencem a cada aluno.

Por exemplo, se for dito que o jardim é assim:

```text
[janela][janela][janela]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
```

Então, se solicitado pelas plantas de Alice, ele deve fornecer:

Violetas, rabanetes, violetas, rabanetes
Ao pedir as plantas de Bob produziria:

Trevo, grama, trevo, trevo

## Metas

1. Receber uma string com as sementes
2. Receber um array com os alunos
3. Ordenar os alunos por ordem alfabética
4. Separar as sementes de cada aluno
5. Retornar um array com as sementes do aluno pedido

## Plantas
