# Event Management System

## Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `POST /api/auth/token/`: Get JWT tokens
- `GET /api/events/`: List all public events
- `POST /api/events/`: Create a new event
- `POST /api/events/{id}/rsvp/`: RSVP to an event
- `POST /api/events/{id}/reviews/`: Add a review for an event

## Testing

Run tests with:
```bash
python manage.py test
```
