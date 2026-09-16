# 🔊 Text-to-Speech em Python

Script simples em Python que converte texto em áudio (voz) utilizando a biblioteca **gTTS** (Google Text-to-Speech), gerando um arquivo MP3 a partir de um texto em português.

## ✨ Funcionalidades
- Conversão de texto para áudio (.mp3)
- Suporte ao idioma português (pt-br)
- Geração rápida e automática do arquivo de saída

## 🛠️ Tecnologias utilizadas
- Python 3
- [gTTS](https://pypi.org/project/gTTS/)

## 📦 Como executar

1. Clone o repositório:
```bash
git clone https://https://github.com/SammyBrook02/Voice.git
```

2. Instale as dependências:
```bash
pip install gtts
```

3. Execute o script:
```bash
python voice.py
```

O arquivo `ola.mp3` será gerado na pasta do projeto.

## 📄 Exemplo de código

```python
from gtts import gTTS

text = "Olá, tudo bem?"
tts = gTTS(text=text, lang='pt-br')
tts.save("ola.mp3")

print("Arquivo de áudio gerado com sucesso!")
```

## 🚀 Próximos passos
- [ ] Permitir entrada de texto via terminal
- [ ] Adicionar suporte a múltiplos idiomas
- [ ] Interface gráfica simples

## 📝 Licença
Este projeto está sob a licença MIT.
