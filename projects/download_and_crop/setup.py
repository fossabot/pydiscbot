import requests
import os

name_dir = "Dand_Crop"
first_dir = os.getcwd()

try:
  os.mkdir(name_dir)
except FileExistsError:
  pass

os.chdir(name_dir)
one_path = os.getcwd()

file_names = ['random_neko_list.py', 'main.py', 'setup.py', 'keep_module.py']
file_names_main = ['LICENSE', 'README.md']


def download_file_from_github(url_id, file_name):
  url_main = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/{file_name}"
  url_files = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/{file_name}"

  if url_id == 0:
    url = url_files
  if url_id == 1:
    url = url_main

  try:

    def download_file(url):
      local_filename = url.split('/')[-1]
      with requests.get(url, stream=True, allow_redirects=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
      return local_filename

    file_name = download_file(url)
    pass
  except Exception as err:
    return err


def update():

  for file_name in file_names:
       download_file_from_github(0, file_name)
  for file_name in file_names_main:
      download_file_from_github(1, file_name)



update()

with open("start.bat", "w") as outfile:
  outfile.write(f"python main.py")
  pass

print("Установка завершена!")
import time

os.chdir(first_dir)
try:
  time.sleep(2)
  os.remove(__file__)
except:
  pass
