from gtts import gTTS

text = "Olá, tudo bem?"
tts= gTTS(text=text, lang='pt-br')
tts.save("ola.mp3")

print("Arquivo de áudio gerado com sucesso!")