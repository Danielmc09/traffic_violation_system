# Traffic Violation System

## Descripción del Proyecto

El sistema de infracciones de tráfico es una API RESTful desarrollada con Django y Django REST framework que permite a los oficiales de policía registrar infracciones de tráfico y generar informes de infracciones asociadas a vehículos pertenecientes a personas específicas.

## Lenguajes y herramientas:

<img alt="Badge" style="float: left; margin-right: 10px;" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/> <img alt="Badge" style="float: left; margin-right: 10px;"  src="https://img.shields.io/badge/django-%230175C2.svg?&style=for-the-badge&logo=django&logoColor=white"/> <img alt="Badge" style="float: left; margin-right: 10px;"  src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/> <img alt="Badge" style="float: left; margin-right: 10px;"  src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img alt="Badge" style="float: left; margin-right: 10px;"  src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/> <img alt="Badge" style="float: left; margin-right: 10px;"  src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/> <img alt="Badge" style="float: left; margin-right: 10px;"  src="https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white"/> 


## Funcionalidades

- Registrar infracciones de tráfico.
- Generar informes de infracciones basados en el correo electrónico del propietario del vehículo.
- Autenticación mediante Token para oficiales.
- Admin de Django para gestionar los modelos.

## Requisitos

- Python 3.10 o superior
- Django 3.2 o superior
- Django REST framework
- PostgreSQL (opcional para producción, SQLite para desarrollo)

## Instalación

### 1. Clonar el Repositorio

Clona el repositorio desde GitHub a tu máquina local.

```bash
git clone https://github.com/Danielmc09/traffic_violation_system.git
cd traffic_violation_system
```

### 2. Crear y Activar un Entorno Virtual

Crea un entorno virtual para el proyecto y actívalo.

#### En Windows
```
python -m venv env
.\env\Scripts\activate
```

#### En macOS y Linux
```
python3 -m venv env
source env/bin/activate
```

### 3. Instalar las Dependencias

Instala las dependencias del proyecto.
```
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

Copia el archivo `.env.example` a un nuevo archivo `.env` en la raíz del proyecto y modifica las variables según tu configuración:

```bash
cp .env.example .env
```
Configuración con PostgreSQL (opcional)
```bash
pip install psycopg2-binary
```
Actualiza traffic_violation_system/settings.py para cargar las variables de entorno:
```
# Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}
```
Si prefieres usar SQLite por defecto para desarrollo, no es necesario realizar los pasos anteriores.

### 5. Migrar la Base de Datos

Primero, crea las migraciones necesarias para configurar la base de datos:

```bash
python manage.py makemigrations

python manage.py migrate
```
### 6. Crear Usuarios y Oficiales

Los datos de prueba para crear usuarios y oficiales se cargan automáticamente al generar las migraciones. Los datos por defecto están en las carpetas `fixtures`.

#### Datos de prueba:

- **Admin:**
  - Usuario: `admin1`
  - Contraseña: `admin1`

- **Officers:**
  - Usuario: `officer1`
  - Contraseña: `p4ssw0rd1`
  - Usuario: `officer2`
  - Contraseña: `p4ssw0rd2`

### 7. Ejecutar el Servidor de Desarrollo
Inicia el servidor de desarrollo de Django:
```bash
python manage.py runserver
```

## Uso

### Colecciones de Postman

En la carpeta `collection_postman`, encontrarás dos archivos:

1. `traffic_violation_system.postman_collection.json`: Contiene las solicitudes configuradas para la API.
2. `traffic_violations_system.postman_environment.json`: Contiene la configuración del entorno para la API.

#### Importar Colecciones de Postman

1. Abre Postman.
2. Haz clic en **"Import"** en la esquina superior izquierda.
3. Selecciona los archivos `collection_postman/traffic_violation_system.postman_collection.json` y `collection_postman/traffic_violations_system.postman_environment.json` desde la carpeta `collection_postman`.

#### Configurar el entorno importado

1. Después de importar los archivos, ve a la pestaña **"Environments"** en Postman.
2. Selecciona el entorno `traffic_violations_system`.
3. Asegúrate de que la variable `base_url` esté configurada correctamente, por ejemplo: `http://127.0.0.1:8000/api`.
4. La variable `auth_token` se actualizará automáticamente después de obtener el token de autenticación usando el endpoint `/api/officers/obtain-token/`.

### Endpoints de la API

| Endpoint                                  | Método | Descripción                                                                                      | Requiere Autenticación |
|-------------------------------------------|--------|--------------------------------------------------------------------------------------------------|------------------------|
| `/api/officers/obtain-token/`             | POST   | Obtener un token de autenticación para un oficial.                                               | No                     |
| `/api/violations/cargar_infraccion/`      | POST   | Registrar una nueva infracción de tráfico.                                                       | Sí                     |
| `/api/violations/generar_informe/<email>/`| GET    | Generar un informe de infracciones basadas en el correo electrónico del propietario del vehículo.| No                     |

#### `/api/officers/obtain-token/`

- **Método**: POST
- **Descripción**: Obtener un token de autenticación para un oficial.
- **Requiere Autenticación**: No
- **Parámetros**:
  - `username` (string): Nombre de usuario del oficial.
  - `password` (string): Contraseña del oficial.
- **Ejemplo de Solicitud**:
  ```json
  {
    "username": "officer1",
    "password": "p4ssw0rd1"
  }
  ```
- **Ejemplo de Respuesta**:
  ```json
  {
    "token": "your_generated_token_here"
  }
  ```

#### `/api/violations/cargar_infraccion/`

- **Método**: POST
- **Descripción**: Registrar una nueva infracción de tráfico.
- **Requiere Autenticación**: Sí
- **Parámetros**:
  - `placa_patente` (string): Placa patente del vehículo.
  - `timestamp` (string): Marca de tiempo de la infracción.
  - `comentarios` (string): Comentarios sobre la infracción.
- **Ejemplo de Solicitud**:
  ```json
  {
    "placa_patente": "ABC123",
    "timestamp": "2024-07-30T15:53:00Z",
    "comentarios": "Estacionado en lugar prohibido"
  }
  ```
- **Ejemplo de Respuesta**:
  ```json
  {
    "id": 5,
    "timestamp": "2024-07-30T15:53:00Z",
    "comments": "Estacionado en lugar prohibido",
    "vehicle": {
        "license_plate": "ABC123",
        "brand": "Toyota",
        "color": "Red"
    },
    "officer": {
        "name": "Officer One",
        "badge_number": "1001"
    }
  }
  ```

#### `/api/violations/generar_informe/<email>/`

- **Método**: GET
- **Descripción**: Generar un informe de infracciones basadas en el correo electrónico del propietario del vehículo.
- **Requiere Autenticación**: No
- **Parámetros**:
  - `email` (string): Correo electrónico del propietario del vehículo.
- **Ejemplo de Solicitud**:
  ```json
  {
    "email": "john@example.com"
  }
  ```
- **Ejemplo de Respuesta**:
  ```json
  [
    {
      "id": 1,
      "timestamp": "2024-07-30T15:53:00Z",
      "comments": "Dejo un perro adentro sin aire",
      "vehicle": {
        "license_plate": "ABC123",
        "brand": "Toyota",
        "color": "Red"
      },
      "officer": {
        "name": "Officer One",
        "badge_number": "1001"
      }
    },
    {
      "id": 2,
      "timestamp": "2024-07-30T15:53:00Z",
      "comments": "Estacionado en lugar prohibido",
      "vehicle": {
        "license_plate": "ABC123",
        "brand": "Toyota",
        "color": "Red"
      },
      "officer": {
        "name": "Officer Two",
        "badge_number": "1002"
      }
    }
  ]
  ```

Autor: <a href="https://www.linkedin.com/in/danielmendietadeveloper/">Angel Daniel Menideta Castillo</a> © 2023
