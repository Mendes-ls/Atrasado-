import speech_recognition as sr

rec = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())

mic = sr.Microphone()

with mic as source:
    rec.adjust_for_ambient_noise(source)
    print("Ajustando para o ruído ambiente...")
    rec.energy_threshold = 6000
    print("Pronto para ouvir...")
    audio = rec.listen(source)

try:
    text = rec.recognize_google(audio, language='pt-BR')
    print("Você disse: " + text)
except sr.UnknownValueError:
    print("Não consegui entender o áudio.")
except sr.RequestError as e:
    print("Erro ao se conectar ao serviço de reconhecimento de fala; {0}".format(e))