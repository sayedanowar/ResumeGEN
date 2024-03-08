![ResumeGEN](https://raw.githubusercontent.com/sayedanowar/ResumeGEN/main/img/GitHub%20Repository%20Image.png)

# ResumeGEN

This is a Django project for creating and managing resumes. Users can sign up, fill in their details, and generate a professional resume in PDF format.

## Setup Instructions

1. Clone the repository:

   ```bash
   https://github.com/sayedanowar/ResumeGEN.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser (admin):

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Project Structure

- The `app` directory contains the main Django application for managing resumes.
- Templates are stored in the `templates` directory for rendering HTML pages.
- Static files (CSS, JavaScript) are stored in the `static` directory.

## Configuration

- Configure your email settings in `settings.py` to enable email functionality for user password reset. Replace `'YOUR_EMAIL_HERE'` with your actual email address and `'YOUR_APP_PASSWORD_HERE'` with an `App Password` (if using Gmail):

   ```bash
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_HOST_USER = 'YOUR_EMAIL_HERE'
   EMAIL_HOST_PASSWORD = 'YOUR_APP_PASSWORD_HERE'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   ```

- **Note :** To create an App Password in Gmail, follow these steps:

   - Go to your Google Account settings.
   - Enable 2FA Authentication in your Google Account.**
   - Search for App Passwords in your Google Account settings.
   - Enter a name that helps you remember where you’ll use the app password.
   - Select Create.
   - To enter the app password, follow the instructions on your screen. The app password is the 16-character code that generates on your device.
   - Select Done.

- Set up authentication backends and social authentication (e.g., GitHub) in `settings.py`. Replace `'YOUR_GITHUB_AUTH_KEY_HERE'` and `'YOUR_GITHUB_AUTH_SECRET_HERE'` with your GitHub OAuth App's credentials:

   ```bash
   SOCIAL_AUTH_GITHUB_KEY = 'YOUR_GITHUB_AUTH_KEY_HERE'
   SOCIAL_AUTH_GITHUB_SECRET = 'YOUR_GITHUB_AUTH_SECRET_HERE'
   ```

- Run these commands again:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

- Customize other settings such as `DEBUG`, `ALLOWED_HOSTS`, etc., as per your requirements.

## Features

- User Authentication
- Log In / Sign Up With GitHub
- Responsive Design
- Forgot Password Feature

## Tech Stack

**Front-End :** HTML, CSS, JavaScript

**Back-End :** Django

## Deployment

- For deployment, ensure to set `DEBUG = False` in your `settings.py` and configure a production-ready database (e.g., PostgreSQL).
- Use a service like Heroku, AWS, DigitalOcean, or Vercel to deploy your Django application.

## Contributing

Contributions are always welcome! Feel free to open an issue, fork the repository, and submit a pull request.

## Screenshots

### Desktop View

![App Screenshot](https://github.com/sayedanowar/ResumeGEN/blob/main/img/s2.png)

![App Screenshot](https://github.com/sayedanowar/ResumeGEN/blob/main/img/s3.png)

![App Screenshot](https://github.com/sayedanowar/ResumeGEN/blob/main/img/s4.png)

![App Screenshot](https://github.com/sayedanowar/ResumeGEN/blob/main/img/s5.png)

### Mobile View

![App Screenshot](https://github.com/sayedanowar/ResumeGEN/blob/main/img/s7.png)

![App Screenshot](https://github.com/sayedanowar/ResumeGEN/blob/main/img/s8.png)

![App Screenshot](https://github.com/sayedanowar/ResumeGEN/blob/main/img/s9.png)

![App Screenshot](https://github.com/sayedanowar/ResumeGEN/blob/main/img/s10.png)