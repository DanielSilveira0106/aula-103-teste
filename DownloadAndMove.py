import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "DIGITE O CAMINHO DA PASTA DE DOWNLOAD (USE " / ") no VSC"
# to_dir = "DIGITE A PASTA DE CAMINHO DE DESTINO (USE " / ") no VSC"

from_dir = "C:/Users/Usuário/Downloads"
to_dir = "C:/Users/Usuário/Downloads/Aula103 2"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name , extension = os.path.splitext(event.src_path)

        time.sleep(1)

        for key , value in dir_tree.items():
            time.sleep(1)
            if extension in value:

                file_name = os.path.basename(event.src_path)

                print("Baixando" + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name
        
                if os.path.exists(path2):
                    print("Diretorio existe....")
                    print("Movendo" + file_name + "....")
                    shutil.move(path1,path3)
                    time.sleep(1)

                else:
                    print("Criando diretório....")
                    os.makedirs(path2)
                    print("Movendo" + file_name + "....")
                    shutil.move(path1,path3)
                    time.sleep(1) 
        print(event)
        print(event.src_path)


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()

try:

   while True:
    time.sleep(2)
    print("executando...")

except KeyboardInterrupt:
    print("Interrompido")
    observer.stop()
