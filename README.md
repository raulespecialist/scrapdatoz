# scrapdatoz
pequeño scraper con interfaces web

Se necesita tener instalado python3.6, pip3 y python3-venv

Primero clonamos el repositorio
git clone https://github.com/raulespecialist/scrapdatoz.git

Luego creamos un entorno virtual

python3 -m venv myvenv

Luego ingresamos al entorno virtual

source myenv/bin/activate
cd scrapdatoz

Se tiene que instalar los archivos necesarios 
pip3 install -r requirements.txt

luego creamos la base de datos

python3 manage.py makemigration
python3 manage.py migrate

Creamos el usuario de administracion

python3 manage.py createsuperuser

y por ultimo corremos el servicio
python3 manage.py runserver
