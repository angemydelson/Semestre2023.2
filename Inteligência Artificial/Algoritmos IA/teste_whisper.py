import whisper
# Instruções de uso e instalação em https://github.com/openai/whisper
# Lembre de instalar a ffmpeg no seu sistema operacional https://ffmpeg.org/
model = whisper.load_model("medium")
result = model.transcribe("musica.mp3")
#result2 = model.transcribe("musica2.mp3")
#result3 = model.transcribe("musica3.mp3")
print(result["text"])
#print(result2["text"])
#print(result3["text"])