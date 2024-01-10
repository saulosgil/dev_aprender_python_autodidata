# importa o módulo e as funcionalidades contidas no módulo
from imagem import tirar_foto, qualidade_maxima, Camera

# Testa a função
tirar_foto()

# testa a variavel
print(qualidade_maxima)

# testa a classe criada
camera = Camera()
camera.testar_camera()

# importa o módulo e a função criada
from video import iniciar_gravacao

# Testa a função
iniciar_gravacao()

# Outro exemplo
from video import iniciar_gravacao

# testa a função
iniciar_gravacao()
