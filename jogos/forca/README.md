# Jogo da Forca

Este projeto é uma implementação do clássico jogo da forca em Python.
 
## Requisitos
Python 3.x

## Estrutura do código
## O código possui várias funções:

1. mensagem_inicio(): Imprime a mensagem inicial do jogo da forca.

2. carrega_palavra_secreta(): Carrega palavras de um arquivo de texto chamado 'palavras.txt' e escolhe uma palavra aleatória do arquivo como a palavra secreta.

3. inicializa_letras_acertadas(palavra): Cria uma lista contendo '_' para cada letra na palavra secreta.

4. pede_chute(): Solicita ao usuário um palpite e retorna a letra em maiúsculas.

5. chute_correto(chute, letras_acertadas, palavra_secreta): Atualiza a lista de letras acertadas com o chute correto do usuário.

6. imprime_mensagem_perdedor(palavra_secreta): Imprime a mensagem e desenho de enforcado se o usuário perder o jogo.

7. imprime_mensagem_vencedor(): Imprime a mensagem e desenho de vencedor se o usuário ganhar o jogo.

8. desenha_forca(erros): Desenha a forca com base no número de erros.

9. jogar(): Função principal do jogo que gerencia o fluxo do jogo.

## Como jogar
1. Adicione um arquivo chamado palavras.txt no mesmo diretório do script jogo_da_forca.py. O arquivo deve conter uma lista de palavras, uma por linha.

2. Execute o script jogo_da_forca.py no terminal ou no seu ambiente de desenvolvimento Python.

3. O jogo apresentará uma lista de espaços em branco, representando as letras da palavra secreta.

4. O jogador deve adivinhar as letras da palavra secreta. Para isso, digite uma letra e pressione Enter.

5. Se a letra estiver correta, ela será revelada na posição correta. Caso contrário, uma parte do boneco será desenhada na forca.

6. O jogo continua até que o jogador adivinhe a palavra secreta ou o boneco seja enforcado.



