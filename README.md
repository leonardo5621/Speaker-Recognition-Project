# LRM_4_Voice
Repositório do projeto de Pesquisa: Sistema de Controle de Acesso Baseado em Reconhecimento de Voz

Este projeto consiste na proposta de um sistema de reconhecimento de voz,mais especificamente para reconhecimento de locutor e independente de texto, para ser utilizada como uma ferramenta de controle de acesso.
Python é a linguagem utilizada.

As principais técnicas exploradas são:

-Coeficientes de Frequência Mel-Cepstrais(MFCC)
-Modelo de Mistura de Gaussianas(GMM-UBM)

Até o momento foram realizados testes utilizando a base de dados ELSDSR, onde foi obtida uma Taxa de Falsa Rejeição de 0% dentre 22 tentativas, e uma de Falsa Aceitação de 2% dentre 50 tentativas.

Extensões do Python sendo utilizadas: python speech features, sklearn,scipy,numpy,matplotlibpyaudio,pydub
