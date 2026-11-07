# LYALLPUR GOLD GYM

A Django-based gym management system for managing members, enquiries, membership plans, and gym equipment from one staff dashboard.

## Features

- Staff authentication with protected dashboard routes
- Live dashboard counters for members, plans, equipment, and enquiries
- Member management with plan assignment, joining date, expiry date, gender, age, and initial payment
- Enquiry management with DataTables search, sorting, export buttons, and delete actions
- Membership plan management with add, list, and protected delete actions
- Equipment management with price, unit, quantity, purchase date, condition, and description
- Responsive Bootstrap navigation for public and staff users
- About Us page with gym image and structured content
- Contact page with opening hours, phone number, address, and Google Maps link
- SQLite database for local development

## Technology Stack

- Python 3.12+
- Django 6.1
- Bootstrap 5
- DataTables
- SQLite
- HTML, CSS, and JavaScript

## Local Setup

1. Clone the repository:

   ```powershell
   git clone https://github.com/shahzaib-javed-python-backend/lyallpur-gold-gym.git
   cd lyallpur-gold-gym
   ```

2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```powershell
   python manage.py migrate
   ```

5. Create a staff administrator:

   ```powershell
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```powershell
   python manage.py runserver
   ```

Open `http://127.0.0.1:8000/` in your browser.

## Main Routes

| Page | URL |
| --- | --- |
| Admin dashboard | `/` |
| Admin login | `/admin_login/` |
| About Us | `/about/` |
| Contact Us | `/contact/` |
| Members | `/members/` |
| Add member | `/members/add/` |
| Enquiries | `/enquiry/` |
| Plans | `/plans/` |
| Equipment | `/equipment/` |
| Django admin | `/admin/` |

## Security Notes

- The SQLite database is ignored by Git for local development.
- Keep `SECRET_KEY`, passwords, and environment-specific settings out of public repositories.
- Use environment variables and a production database before deployment.
- `DEBUG` should be disabled in production.

## License

This project is intended for educational and local gym-management use.
