# pruebaSSI

1.Instalar Python 2
2. Crear ambiente virtual
  python3 -m venv myvenv
3. entrar al ambiente virtual
  source myvenv/bin/activate
4. Actualizar pip
  python3 -m pip install --upgrade pip
5. Instalar django con el archivo requeriments.txt
  pip install -r requirements.txt
  
6. Correr las migraciones
  python3 manage.py makemigrations
  python3 manage.py migrate
7. Correr el servidor
  python3 manage.py runserver
