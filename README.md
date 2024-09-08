# HacknChill

## Overview

**HacknChill** is a Django-based application designed to assist students and educators with the following features:

1. **Roadmap Visualization:** Generate and display interactive roadmaps for various topics to aid in understanding and planning.
2. **Text-to-Animation Conversion:** Convert textual notes into engaging animations to enhance learning and make notes more interactive.

![HacknChill Overview](images/overview.png)

## Features

- **Roadmap Generation:**
  - Create visual roadmaps for any topic with interactive elements.
  - Easy navigation and customization options.

- **Text-to-Animation Conversion:**
  - Convert text-based notes into animations with narration and visual effects.
  - Enhance learning through interactive and animated content.

## Installation

To set up **HacknChill** on your local machine, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/hacknchill.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd hacknchill
    ```

3. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install Required Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Database Migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser account for accessing the Django admin panel.

7. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

### Roadmap Generation

1. Access the roadmap feature through the web interface.
2. Enter the topic and customize your roadmap.
3. View and interact with the generated roadmap.

### Text-to-Animation Conversion

1. Prepare your text notes in the supported format (e.g., `.txt`).
2. Access the text-to-animation feature through the web interface.
3. Upload the text file and configure animation options.
4. Convert the text into animations and view or download them.

![Text-to-Animation Example](videos/)

## Contributing

We welcome contributions to **HacknChill**. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please reach out to:

- **Your Name** - [your-email@example.com](mailto:your-email@example.com)
- **GitHub** - [https://github.com/your-username](https://github.com/your-username)

