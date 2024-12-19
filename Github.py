import os
import subprocess
import shutil
import time
path_documents = "Pasta onde estão todos os projetos"
all_arquivers = os.listdir(path_documents)
path_arquivos = "Pasta onde ira armazenar o backup"
arquivos_bkp = os.listdir(path_arquivos)

#pego o tamanho da pasta, pega o tamanho de cada arquivo
def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            # Soma o tamanho de cada arquivo
            total_size += os.path.getsize(file_path)
    return total_size

#limite de 2Gb
limite = 2 * 1024 * 1024 * 1024  

#sobe para o Github
for arquiver in all_arquivers:
    
    path_complete = os.path.join(path_documents, arquiver)
    tamanho = get_directory_size(path_complete)
    if tamanho > limite:
        print(f"Arquivo {arquiver} ultrapassou o limite de {limite/1024/1024/1024:.2f} GB.")
    else:
        
        if arquiver != "bkp" and os.path.isdir(path_complete) and arquiver not in arquivos_bkp and arquiver != "GitHub":
            shutil.copytree(path_complete, os.path.join(path_arquivos, arquiver))
            print(f"Arquivo {arquiver} foi adicionado ao backup.")

            print("Backup realizado com sucesso!")
            time.sleep(5)

            os.chdir(path_arquivos)

            subprocess.run(["git", "init"], capture_output=True, text=True, check=True)
            print("Repositório iniciado com sucesso!")


            git_remote = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True, check=True)
            if "origin" not in git_remote.stdout:
                subprocess.run(["git", "remote", "add", "origin", "Repositório Git com o token de authenticação Exeplo:https://{Chave de authenticação}@github.com/{nome}/{repositório}.git"],capture_output=True, text=True, check=True)

                print("Remote configurado com sucesso.")
                

            git_status = subprocess.run(["git", "status"], capture_output=True, text=True, check=True)
            print("Status do repositório antes do pull:\n", git_status.stdout)            


            if "nothing to commit" not in git_status.stdout:
                subprocess.run(["git", "add", "."], capture_output=True, text=True, check=True)
                subprocess.run(["git", "commit", "-m", "Backup automático"], capture_output=True, text=True, check=True)
                print("Alterações locais commitadas.")
                

            try:
                subprocess.run(["git", "pull", "--rebase", "origin", "main"], capture_output=True, text=True, check=True)
                print("Pull realizado com sucesso!")
            except subprocess.CalledProcessError as e:
                print(f"Erro ao executar git pull: {e}")
                print(f"Saída de erro:\n{e.stderr}")
                if "CONFLICT" in e.stderr:
                    print("Conflitos detectados. Resolva manualmente ou faça merge automático.")
                    subprocess.run(["git", "merge", "--abort"], capture_output=True, text=True, check=False)


            subprocess.run(["git", "branch", "-M", "main"], capture_output=True, text=True, check=True)


            try:
                git_push = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True, check=True)
                print("Push realizado com sucesso!\n", git_push.stdout)
                print(f"Arqquivo Subido {arquiver}!")
                print(120*"-")
            except subprocess.CalledProcessError as e:
                print(f"Erro ao executar git push: {e}")
                print(f"Saída de erro:\n{e.stderr}")