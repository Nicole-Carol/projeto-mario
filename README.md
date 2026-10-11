🎮 Projeto Mario — Visão Computacional
Projeto de visão computacional aplicado ao clássico Super Mario World, utilizando captura e processamento de imagens em tempo real.

📖 Sobre o Projeto
Este projeto tem como objetivo aplicar técnicas de visão computacional para analisar e interagir com o jogo Super Mario World (SNES) executado no emulador Snes9x. A partir da captura da tela do jogo, são realizadas etapas de processamento de imagem para identificar elementos como o personagem, inimigos e obstáculos.

O projeto combina conhecimentos de:

Captura e processamento de imagens

Detecção de objetos e padrões

Automação de tarefas em tempo real

✨ Funcionalidades
🎥 Captura da tela do emulador em tempo real

🖼️ Processamento de frames com OpenCV

🎯 Detecção de elementos do jogo (Mario, inimigos, moedas, etc.)

🤖 Base para criação de um agente automatizado (bot)

📊 Registro de métricas e resultados do processamento

🛠️ Tecnologias Utilizadas
Tecnologia	Descrição
Python	Linguagem principal do projeto
OpenCV	Processamento de imagens e visão computacional
NumPy	Manipulação de arrays e matrizes
Snes9x	Emulador de SNES utilizado para executar o jogo
Git/GitHub	Controle de versão
📁 Estrutura do Projeto
text
projeto-mario/
├── mario_branco_template.png   # Template para detecção (Mario branco)
├── mario_template.png          # Template para detecção (Mario)
├── snes9x-x64.exe              # Emulador Snes9x
├── snes9x.conf                 # Configurações do emulador
├── readme-windows.txt          # Instruções originais do emulador
├── stderr.txt                  # Log de erros
├── stdout.txt                  # Log de saída
└── super-mario-world-usa_202406_archive.torrent  # Arquivo do jogo
💡 Sugestão: Se você adicionar scripts Python (ex: main.py, detector.py), inclua-os aqui na estrutura.

🚀 Como Executar
Pré-requisitos
Python 3.8 ou superior

OpenCV instalado: pip install opencv-python

NumPy instalado: pip install numpy

Emulador Snes9x (já incluído no repositório)

ROM do jogo Super Mario World

Passos
Clone o repositório:

bash
git clone https://github.com/Nicole-Carol/projeto-mario.git
cd projeto-mario

Crie um ambiente virtual (recomendado):

bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
Instale as dependências:

bash
pip install opencv-python numpy
Execute o emulador e carregue a ROM:

Abra o snes9x-x64.exe

Carregue o arquivo da ROM do Super Mario World

Execute o script de visão computacional:

bash
python main.py
🧠 Como Funciona
Captura: A tela do emulador é capturada continuamente.

Pré-processamento: A imagem é convertida para escala de cinza, binarizada e filtrada.

Detecção: Técnicas como template matching são usadas para localizar o Mario e outros elementos.

Ação: Com base nos resultados, o sistema pode tomar decisões (movimentar, pular, etc.).

📌 Próximos Passos
□ Implementar detecção de inimigos em tempo real
□ Adicionar lógica de tomada de decisão (bot)
□ Criar interface gráfica para acompanhamento
□ Documentar métricas de acurácia da detecção
🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

📄 Licença
Este projeto é de uso educacional. O emulador Snes9x possui sua própria licença (GPL). Consulte o arquivo readme-windows.txt para mais informações.

👩‍💻 Autora
Nicole Carol

GitHub: @Nicole-Carol
