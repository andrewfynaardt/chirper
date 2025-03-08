# Chirper

Chirper is a social media platform where users can sign up, create chirps, like chirps, reply to others' chirps, and filter content based on their preferences. The platform supports rich text for chirps.

## Features

### Basic Features:
- **User Authentication**: Sign up and log in using Django All-Auth.
- **Chirps**: Create chirps of up to 255 characters.
- **Like**: Like chirps from other users.
- **Reply**: Reply to other users' chirps.

### Extended Features:
- **Custom Styling**: The application includes custom CSS, scripts, and Google Fonts to enhance the user interface and provide a visually appealing experience.  
- **HTMX Integration**: Utilizes HTMX for dynamic content updates, allowing interactions without full-page reloads.  
- **AJAX-Based Liking**: Users can like chirps instantly without needing to refresh the page, improving responsiveness and user experience.
- **Chirp Filtering**: Users can chose the order to view the chirps.


## Requirements
- Python >= 3.12
- `django.db.migrations`, `django.db.models`, `django.conf.settings`, `django.contrib.admin`, 
`django.apps.AppConfig`, `django.forms`, `django.utils.timezone`, `django.contrib.auth.models.User`, 
`django.test.TestCase`, `django.urls.path`, `chirp_view`, `home`, `profile`, `like_chirp`, 
`still_dev`, `django.views.generic.TemplateView`, `django.shortcuts.render`, `redirect`, 
`get_object_or_404`, `django.contrib.auth.decorators.login_required`, `ChirpForm`, `Chirp`, 
`Reply`, `UserFollowing`, `User`, `os`, `django.core.asgi.get_asgi_application`, 
`django.core.wsgi.get_wsgi_application` libraries.

## How to Install

To run Chirper locally on your machine, follow these steps:

To run Chirper locally on your machine, follow these steps:

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/andrewfynaardt/chirper.git
   
2. Navigate into the project directory:
   ```bash
   cd chirper

3. Sync dependencies:
   ```bash
   uv sync
   
4. Run the migrations to set up the database:
   ```bash
   uv run python manage.py migrate

5. Start the development server using Django:
   ```bash
   uv run python manage.py runserver

6. Open your browser and go to the local server address to access the website:
   http://127.0.0.1:8000/chirper/home/
   
## How to Use the Website

1. **Sign Up**: 
   - Visit [http://127.0.0.1:8000/] and click on "Sign Up".
   - Enter your necessary information to create an account.
   - If you already have an account, click "Log In" and use your credentials.

2. **Create Chirps**: 
   - After logging in, click on the "Create Chirp" button to post a chirp.
   - You can type up to 255 characters and use the rich text editor.

3. **Like and Reply**: 
   - Browse through chirps from other users and interact with them.
   - Click the heart icon to like a chirp.
   - To reply, click the "Reply" button below the chirp you want to respond to.

4. **Filter Chirps**: 
   - Use the filter feature to customize the chirps you see.
   - Filter by criteria like most liked, latest posts, or other options available.

## Example Usage
- **Sign up** on the website using your email.
- **Post a chirp** by clicking "Create Chirp".
- **Like chirps** you enjoy by clicking the heart icon.
- **Reply to chirps** using the "Reply" button.

## Contributing

Contributions are welcome! To contribute to the project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure the code is working correctly.
4. Submit a pull request with a description of your changes.

Please ensure that your code follows the existing style and includes tests for any new features.

## Contact

If you encounter any issues or have any questions, please open an issue in the [GitHub repository](https://github.com/andrewfynaardt/chirper/issues).
