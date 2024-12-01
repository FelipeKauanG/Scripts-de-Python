import keyboard
import threading
import time

# Função para escutar eventos de teclado
def listen_for_keys():
    while True:
        key = keyboard.read_key()  # Espera a tecla ser pressionada
        print(f"Tecla pressionada: {key}")
        if key == "esc":  # Caso a tecla Esc seja pressionada, sai do loop
            print("Saindo...")
            break

# Função para simular outra tarefa que acontece ao mesmo tempo
def do_other_tasks():
    while True:
        print("Fazendo outra coisa...")
        time.sleep(2)  # Fazendo outra coisa, mas a cada 2 segundos

# Criando threads para execução simultânea
thread1 = threading.Thread(target=listen_for_keys)
thread2 = threading.Thread(target=do_other_tasks)

# Iniciando as threads
thread1.start()
thread2.start()

# Espera as threads terminarem
thread1.join()
thread2.join()
