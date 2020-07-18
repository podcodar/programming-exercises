## Contagem regressiva!

Vamos construir uma contagem regressiva usando nosso conhecimento em Javascript e HTML?

Não? :( Então fica para a próxima

Sim? Então contagem regressiva para o enunciado:

10

9

8

7

6

5

4

3

2

1

![alt text](https://media.giphy.com/media/xT0xeHDVBcAulhRJRK/giphy.gif "BOOOM")

## Spoiler!
No final desse exercício teremos uma página semelhante a seguinte:

![alt text](https://imgur.com/1cDYv7y.gif "Olha o bruxo ai!")

## Preparação
Esse exercício será implementado utilizando os estilos presentes na biblioteca [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/). Antes de prosseguir para solução, dê uma familiarizada básica na documentação dela.

**Observação**: Os exercícios que iremos propor a vocês não incluirão apenas assuntos abordados nas **meetups**. Queremos que vocês sejam pró-ativos e tentem aprender outros assuntos por conta própria. Lembre-se, o Google é seu amigo e estamos disponíveis para tirar dúvidas nos nossos canais de comunicação.

## Racional

Esse tutorial está dividido em seções para facilitar a construção da página. Em geral, é uma boa prática dividirmos um projeto/problema em subjprojetos/problemas; pois assim diminuimos a complexidade de cada parte do problema que iremos resolver.

Antes de prosseguir para a implementação da página, faça um simples exercício e pense como você se organizaria para resolver o problema proposto. 

**.........**

Caso tenha confiança nesse planejamento, prossiga na sua resolução e depois confira a proposta sugerida a seguir. Se você não conseguiu encontrar uma forma clara para implementar a página, sem problemas, iremos mostrar passo a passo como fazê-lo.

## 1 - Dinâmica da página
Como você deve ter percebido, a dinâmica da página foi exibida através de um gif (é isso mesmo, ela só faz isso :). Podemos dividir essa página em três telas: **home**, **countdown** e **success**. 

Elas obedecem a sequência:

    home --> countdown --> success --|
    ^---------------------------------
**Observação**: apenas uma tela é exibida por vez.

Construa um **div** para cada tela e atributa o seu id com o nome da tela.  

Depois disso iremos definir as funções de transição para cada tela. São elas:
```javascript
// Equivale ao --> home no diagrama das telas.
// Essa função deve ser chamada quando a página é carregada ou quando o usuário apertar o botão "resetar" na tela de sucesso.
// Aqui devemos deixar visível apenas o conteúdo da tela "home" (as outras telas devem ficar invisíveis). Também é importante limparmos o conteúdo preexistente no campo "Tempo".
function startHome() {}

// Equivale ao --> countdown no diagrama das telas.
// Essa função deve ser chamada quando o usuário clicar no botão "iniciar" e o campo "tempo" tiver um número válido. Devemos executar essa função passando o valor númerico do campo "tempo" como parâmetro.
// Aqui devemos deixar visível apenas o conteúdo da tela "countdown" (as outras telas devem ficar invisíveis). Também é responsabilidade dessa função iniciar a contagem regressiva.
function startCountdown(time) {}

// Equivale ao --> success no diagrama das telas.
// Essa função deve ser chamada quando a contagem regressiva acabar.
// Aqui devemos deixar visível apenas o conteúdo da tela "success" (as outras telas devem ficar invisíveis).
function startSuccess() {}
```
Não é necessário implementar a lógica de cada função ainda, apenas as definam. Lembre-se que estamos dividindo o problema principal em problemas menores (cada coisa na sua hora).

## 2 - Construindo a tela "home"
Construa uma página semelhante a seguinte:
![alt text](https://i.imgur.com/Y9wWJKS.png "Página inicial")

Chegou a hora de implementar a função `startHome()` que descrevemos anteriormente.

**Observação**: Não se esqueça de utilizar os estilos do **bootstrap** para definir as telas.

### 2.1 - Validando o campo **Tempo**
O valor do campo **Tempo** deve aceitar apenas números inteiros. Quando o usuário clicar no botão "Iniciar" e o valor digitado no campo "Tempo" não for um inteiro, exiba um pop up com uma mensagem de erro:
![alt text](https://i.imgur.com/2sK4TLT.png "Mensagem de erro")

## 2.2 - Inicie a contagem regressiva
Ao clicar no botão "Iniciar" (caso o valor inserido no campo "Tempo" seja válido) devemos iniciar a contagem regressiva. Em outras palavras, chamaremos a função `startCountdown(time)` passando o valor do campo "Tempo" como parâmetro da função.

