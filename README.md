# Chirper

Chirper is a social media platform where users can sign up, create chirps (messages up to 255 characters), like chirps, reply to others' chirps, and filter content based on their preferences. The platform supports rich text for chirps, allowing for images, videos, bold text, and more.

## Features

### Basic Features:
- **User Authentication**: Sign up and log in using Django All-Auth.
- **Chirps**: Create chirps of up to 255 characters.
- **Like**: Like chirps from other users.
- **Reply**: Reply to other users' chirps.

### Extended Features:
- **Rich Text Chirps**: Supports bold text, images, videos, and more via Trix or Quill.js.
- **Filter Chirps**: Filter chirps based on user preferences.

## Requirements
- Python 3.x
- `django.db.migrations`, `django.db.models`, `django.conf.settings`, `django.contrib.admin`, 
`django.apps.AppConfig`, `django.forms`, `django.utils.timezone`, `django.contrib.auth.models.User`, 
`django.test.TestCase`, `django.urls.path`, `chirp_view`, `home`, `profile`, `like_chirp`, 
`still_dev`, `django.views.generic.TemplateView`, `django.shortcuts.render`, `redirect`, 
`get_object_or_404`, `django.contrib.auth.decorators.login_required`, `ChirpForm`, `Chirp`, 
`Reply`, `UserFollowing`, `User`, `os`, `django.core.asgi.get_asgi_application`, 
`django.core.wsgi.get_wsgi_application` libraries

## Usage

### Example:
- Sign up on the website using your email.
- Once logged in, click on the "Create Chirp" button to post a chirp.
- If you see a chirp you like, click the heart icon to like it.
- You can reply to any chirp by clicking the "Reply" button below it.

### How to Connect to the Website:
1. Visit the website at [insert your deployed URL here].
2. Sign up or log in using your credentials.
3. Create a chirp by typing your message in the text box.
4. You can add rich text such as bold text, images, and videos using the editor.
5. You can like chirps you enjoy and reply to chirps from others.
6. Use the filter feature to customize the chirps you see.

## Instructions for Anyone to Use

1. **Sign Up**: Click on "Sign Up" on the homepage and enter your email, username, and password.
2. **Create Chirps**: After logging in, you can create chirps up to 255 characters. Use the rich text editor to include bold text, images, and videos.
3. **Like and Reply**: Browse through chirps and interact with them by liking or replying.
4. **Filter Chirps**: Use the filter option to refine the content you're seeing based on specific criteria (e.g., most liked, latest, etc.).

## How to Install

To run Chirper locally on your machine, follow these steps:

1. Clone the repository from GitHub.
2. Install the required dependencies from the `requirements.txt` file.
3. Start the development server using Django commands.
4. Open your browser and go to the local server address to access the website.

## Contact

If you encounter any issues or have any questions, please open an issue in the [GitHub repository](https://github.com/andrewfynaardt/chirper/issues).
