import speech_recognition as sr

# Inicializa o reconhecedor de fala
listener = sr.Recognizer()

# Verifica se há microfones disponíveis
mic_list = sr.Microphone.list_microphone_names()
if not mic_list:
    print("Nenhum microfone disponível. Verifique se o microfone está conectado corretamente.")
else:
    print(f"Mic OK")

try:
    # Usa o microfone como fonte de áudio
    with sr.Microphone() as source:
        print('Ajustando para o ruído ambiente...')
        listener.adjust_for_ambient_noise(source)
        
        while True:
            try:
                # Escuta o áudio do microfone
                voice = listener.listen(source)
                print('Processando áudio...')
                
                # Reconhece o comando usando o serviço de reconhecimento do Google
                command = listener.recognize_google(voice, language="en-US")
                print(f"Você disse: {command}")
                
                # Adiciona a condição para parar o loop com a frase "stop"
                if command.lower() == "stop":
                    print('Parando o programa...')
                    break
                
            except sr.UnknownValueError:
                # Não conseguiu entender o áudio
                pass
            except sr.RequestError as e:
                # Erro ao se conectar com o serviço de reconhecimento de fala
                print(f"Não foi possível se conectar ao serviço de reconhecimento de fala do Google; {e}")
            except Exception as e:
                # Captura qualquer outra exceção que possa ocorrer
                print(f"Um erro ocorreu durante o reconhecimento: {e}")

except Exception as e:
    print(f"Um erro ocorreu com o microfone: {e}")
