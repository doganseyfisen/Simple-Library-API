# Simple-Library-API

This project is created to build a simple library API. Used Django Rest Framework. The project aims to provide a simple API.

## Features

- Users can create, update, view, and delete orders.
- User-friendly interface and navigation.

## Installation

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/doganseyfisen/Simple-Library-API.git
   cd Simple-Library-API
   ```

2. Create a virtual environment and activate (optional but recommended):
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. Create admin so that you can Create, Read, Update and Delete from `admin/`:
   ```
   python manage.py createsuperuser
   ```

6. Start the application:
   ```
   python manage.py runserver
   ```

## Usage

- Once the application is running, open your web browser and go to `http://127.0.0.1:8000/admin/` and `http://127.0.0.1:8000/api/`.
- You can start managing library and books in it through the user-friendly interface.

## License

This project is distributed under the MIT License. For more information, see the [LICENSE](LICENSE) file.
