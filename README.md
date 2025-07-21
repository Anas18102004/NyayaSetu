# Legal Case Management System

A comprehensive legal case management system featuring AI-powered document analysis and appointment scheduling, built with FastAPI and React.

## Features

### Document Summarizer
- Upload and analyze legal documents (PDF, TXT)
- AI-powered summarization using Google's Gemini API
- Extract key points and important information
- Clean and intuitive user interface

### AI Appointment Booking
- Intelligent scheduling with AI assistance
- Real-time availability checking
- Appointment management (create, view, cancel)
- Email notifications (optional)

### Core Technologies
- **Backend**: FastAPI, Python 3.9+
- **Frontend**: React, TypeScript, Tailwind CSS
- **AI**: Google Gemini API
- **Database**: PostgreSQL
- **Deployment**: Docker, Nginx

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ and npm
- Python 3.9+
- Google Gemini API key

### Local Development

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Law_full
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. Start the development environment:
   ```bash
   # Start backend
   cd backend
   pip install -r requirements.txt
   uvicorn app:app --reload

   # In a new terminal, start frontend
   cd frontend
   npm install
   npm run dev
   ```

### Production Deployment

1. Build and start containers:
   ```bash
   docker-compose up --build -d
   ```

2. Run database migrations (if any):
   ```bash
   docker-compose exec backend alembic upgrade head
   ```

3. Access the application:
   - Frontend: http://localhost
   - Backend API: http://localhost/api
   - API Documentation: http://localhost/api/docs

## API Endpoints

### Document Summarizer
- `POST /api/summarize/text` - Summarize text content
- `POST /api/summarize/file` - Summarize uploaded file
- `GET /api/summarize/history` - Get summarization history

### Appointment Booking
- `POST /api/appointments/suggest` - Get suggested time slots
- `POST /api/appointments/book` - Book an appointment
- `GET /api/appointments` - List user's appointments
- `DELETE /api/appointments/{appointment_id}` - Cancel an appointment

## Project Structure

```
.
├── backend/                 # FastAPI application
│   ├── app.py              # Main application
│   ├── requirements.txt     # Python dependencies
│   ├── routers/            # API routes
│   ├── services/           # Business logic
│   └── models/             # Database models
│
├── frontend/               # React application
│   ├── public/             # Static files
│   ├── src/                # Source code
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Page components
│   │   └── App.tsx         # Main component
│   └── package.json        # Node.js dependencies
│
├── nginx/                  # Nginx configuration
├── docker-compose.yml      # Docker Compose configuration
└── .env.example           # Example environment variables
```

## Configuration

### Environment Variables

#### Backend
- `GEMINI_API_KEY`: Google Gemini API key (required)
- `DATABASE_URL`: PostgreSQL connection URL
- `SECRET_KEY`: Secret key for JWT tokens

#### Frontend
- `VITE_API_URL`: Base URL for API requests

## Usage

1. **Document Summarizer**:
   - Navigate to the dashboard
   - Upload a document or paste text
   - View the generated summary and key points

2. **Appointment Booking**:
   - Go to the appointments section
   - Select your preferred date and time
   - Confirm your appointment details
   - Receive confirmation and reminders
   - Retrieve relevant legal precedents
   - Generate AI lawyer responses
   - Evaluate judge interventions when necessary

## Technical Details

- **Document Processing**: Uses LlamaIndex with BAAI/bge-large-en-v1.5 embeddings
- **Vector Storage**: Qdrant for efficient semantic search
- **Multi-Agent System**: Separate prompts and logic for AI Lawyer and AI Judge
- **Memory Management**: Maintains debate context across turns
- **Source Attribution**: Preserves metadata from legal documents

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT
