import shutil
import os

username = (os.getlogin())

path = f'C:\\Users\\{username}\\Downloads'
files = os.listdir(path)

dirs_exts = {
    'documents': ['docx', 'doc'],
    'pdf': ['pdf'],
    'audio': ['mp3', 'flac', 'wav', 'ogg'],
    'executable': ['exe', 'msi'],
    'images': ['png', 'jpeg', 'jpg'],
    'compressed': ['zip', 'rar', 'tar', 'gz'],
    'code': ['py', 'c', 'php', 'html', 'css', 'js'],
    'video': ['mp4'],
    'presentation': ['pptx', 'ppt']
}


def move_which_dir(file, extension):
    for dir in dirs_exts.items():
        if extension in dir[1]:
            move(file, str(dir[0]))
            break


def move(file, dir):
    if os.path.exists(f'{path}/{dir}'):
        shutil.move(f'{path}/{file}', f'{path}/{dir}/{file}')
    else:
        try:
            os.makedirs(f'{path}/{dir}')
            shutil.move(f'{path}/{file}', f'{path}/{dir}/{file}')
        except:
            pass


def exec():
    for file in files:
        extension = os.path.splitext(file)[1]
        extension = extension[1:]
        move_which_dir(file, extension)


exec()
