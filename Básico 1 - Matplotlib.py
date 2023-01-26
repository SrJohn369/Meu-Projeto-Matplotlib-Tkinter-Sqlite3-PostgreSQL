# Importa biblioteca matplotlib.pyplot para criar a figura
import matplotlib.pyplot as plt

# Criando a figura com a quantidade de eixos para uma figura 2d
figura, eixo = plt.subplots()
# Especificando os dados dos eixos y, x respectivamente com listas
# As especificações devem sempre ter correspondentes, ou seja, se houver 2 elementos em y também deverá ter em x
# A cor da linha e estilos são plotados com as configurações padrões
eixo.plot([1, 4, 6, 7, 9], [2, 5, 7, 9, 10], label='linha azul padrão, plot 1')
# Especificações da segunda linha
# Assinaturas de chamadas:
# plot([x], y, [fmt], *, data=None, **kwargs)
# plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
# O parâmetro opcional fmt é uma maneira conveniente de definir o básico formatação como cor, marcador e estilo de linha
# É uma cadeia de caracteres de atalho
eixo.plot([2, 5, 7, 9, 10], [1, 4, 6, 7, 9], 'r', label='linha vermelha, plot 2')
# Um exemplo desse parâmetro opcional, que segue esse padrão [color][marker][line] 'yo' marcador circulo amarelo
# os caracteres com suas referencias no fim do código
eixo.plot([2, 5, 7, 9, 10], [1, 4, 6, 7, 9], 'yo', label='Circulo amarelo, plot 3')
# Define as labels do gráfico, legendas para p eixo y e x
eixo.set_ylabel("eixo y")
eixo.set_xlabel("eixo x")
# Define a Label de titulo do gráfico(figura)
eixo.set_title("TITULO")
# Chama legenda definida na label dos plots
eixo.legend()
# plt.show() mostrará uma janela com gráfico criado
plt.show()