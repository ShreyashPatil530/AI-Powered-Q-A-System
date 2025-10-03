# 🤖 AI-Powered Q&A System

A web-based Question & Answer system powered by OpenAI's GPT-3.5-turbo with optional web search integration and MySQL database logging.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Project Overview

This is an **AI Q&A Bot** built as part of an internship assignment to demonstrate problem-solving skills, resourcefulness, and the ability to build AI-powered applications from scratch.

### What It Does
Users can ask any question through a clean web interface, and the system provides intelligent answers using OpenAI's ChatGPT. Optionally, it can search the web for real-time information to enhance answers.

## ✨ Features

### Core Functionality
- ✅ **AI-Powered Answers**: Uses OpenAI GPT-3.5-turbo for intelligent responses
- ✅ **Web Search Integration**: Optional SerpAPI integration for current information
- ✅ **Chat Interface**: Clean, responsive UI with message history
- ✅ **Database Logging**: All Q&A pairs saved to MySQL database
- ✅ **RESTful API**: Easy-to-use endpoints for integration

### Stretch Goals Achieved 🎯
- ✅ **Full Web UI**: Built with Flask and Bootstrap (exceeded CLI requirement)
- ✅ **Database Integration**: Persistent storage with MySQL
- ✅ **Real-time Search**: Web search capability for up-to-date answers
- ✅ **Professional Design**: Modern, responsive interface
- ✅ **Error Handling**: Comprehensive error management

## 🛠️ Technology Stack

**Backend:**
- Python 3.8+
- Flask (Web Framework)
- OpenAI API (GPT-3.5-turbo)
- MySQL (Database)
- SerpAPI (Web Search)

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5.3
- Responsive Design

## 📁 Project Structure

```
qa-system/
│
├── app.py                 # Main Flask application & routes
├── chat.py                # OpenAI API & web search logic
├── database.py            # MySQL database operations
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # This file
│
└── frontend/
    ├── template/
    │   └── index.html     # Main UI template
    └── static/
        ├── app.js         # Frontend JavaScript
        └── style.css      # Custom styles
```

## 🚀 Installation & Setup

### Prerequisites
Before you begin, ensure you have:
- Python 3.8 or higher installed
- MySQL Server installed and running
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- SerpAPI key (optional) ([Get one here](https://serpapi.com/))

### Step 1: Clone the Repository
```bash
git clone https://github.com/shreyashpatil530/ai-qa-system.git
cd ai-qa-system
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory:
```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and add your credentials:
```
OPENAI_API_KEY=your_openai_api_key_here
SERPAPI_KEY=your_serpapi_key_here
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=qa_system
```

### Step 5: Configure Database
Update `database.py` with your MySQL credentials:
```python
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'your_password'),
    'database': os.getenv('DB_NAME', 'qa_system')
}
```

The database and tables will be created automatically on first run.

### Step 6: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

**You should see:**
```
Starting Q&A System on http://localhost:5000
Database and table created successfully
 * Running on http://0.0.0.0:5000
```

## 💻 Usage Guide

### Web Interface
1. Open your browser and go to `http://localhost:5000`
2. Type your question in the input box
3. (Optional) Check **"Enable web search"** for real-time information
4. Click **"Send"** to submit
5. View AI response in the chat interface

### Example Questions
- "What is machine learning?"
- "Explain quantum computing in simple terms"
- "What are the latest developments in AI?" (enable web search)

### API Usage

**Submit a Question:**
```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is artificial intelligence?",
    "use_search": false
  }'
```

**Response Format:**
```json
{
  "status": "success",
  "answer": "Artificial intelligence (AI) is..."
}
```

**Health Check:**
```bash
curl http://localhost:5000/health
```

## 📊 Database Schema

The system automatically creates this table structure:

```sql
CREATE TABLE qa_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    timestamp DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🎨 Interface Preview

The application features:
- **Clean Design**: Modern Bootstrap-based interface
- **Real-time Updates**: Loading indicators during API calls
- **Chat History**: Scrollable conversation view
- **Responsive Layout**: Works on desktop and mobile
- **Error Handling**: User-friendly error messages

## 🧠 How It Works

```
1. User submits question → 2. Web search (optional) → 3. OpenAI API call
                                                              ↓
6. Display in UI ← 5. Log to database ← 4. Generate answer ←┘
```

**Detailed Flow:**
1. User types question and clicks send
2. If web search enabled, SerpAPI fetches top 3 relevant results
3. Question + search context sent to OpenAI GPT-3.5-turbo
4. AI generates contextual answer (max 500 tokens)
5. Q&A pair logged to MySQL database with timestamp
6. Answer displayed in chat interface

## 🔧 Configuration

### Adjust AI Response Settings
In `chat.py`, modify these parameters:
```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=500,        # Response length (increase for longer answers)
    temperature=0.7        # Creativity: 0.0 (focused) to 1.0 (creative)
)
```

### Modify Web Search Results
In `chat.py`:
```python
params = {
    "q": query,
    "api_key": SERPAPI_KEY,
    "num": 3  # Change to get more/fewer search results
}
```

## 🚧 Challenges Faced & Solutions

### Challenge 1: Understanding Flask Project Structure
**Problem:** Initially confused about where to place templates and static files  
**Solution:** Read Flask documentation, learned about `template_folder` and `static_folder` parameters  
**Time Spent:** ~2 hours of research and testing

### Challenge 2: API Key Security
**Problem:** Didn't know how to handle API keys securely  
**Solution:** Researched environment variables, implemented `.env` file approach  
**Learning:** Never commit secrets to GitHub!

### Challenge 3: MySQL Connection Issues
**Problem:** Getting "Access denied" errors when connecting to MySQL  
**Solution:** Created proper user permissions, added error handling in connection function  
**Code Added:**
```python
def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None
```

### Challenge 4: Frontend-Backend Communication
**Problem:** Getting CORS errors when making fetch requests  
**Solution:** Installed and configured Flask-CORS  
**Learning:** Understanding cross-origin resource sharing

### Challenge 5: Handling Async Operations
**Problem:** UI freezing while waiting for API response  
**Solution:** Added loading states with spinner, disabled button during requests  
**Result:** Much better user experience

## 📚 What I Learned

### Technical Skills
- **API Integration**: Working with RESTful APIs (OpenAI, SerpAPI)
- **Full-Stack Development**: Connecting frontend, backend, and database
- **Database Management**: SQL queries, connection pooling
- **Web Development**: Flask routing, Jinja2 templates, static files
- **JavaScript**: Async/await, fetch API, DOM manipulation
- **Error Handling**: Try-catch blocks, graceful degradation

### Soft Skills
- **Problem Solving**: Using Google, Stack Overflow, and documentation
- **Persistence**: Debugging errors until finding solutions
- **Documentation**: Writing clear setup instructions
- **Time Management**: Balancing features vs. deadline

### Key Takeaways
1. **Start Simple**: Built CLI first, then added UI
2. **Test Frequently**: Caught issues early by testing each component
3. **Read Docs**: Official documentation > random tutorials
4. **Ask for Help**: Used ChatGPT and forums when stuck
5. **Version Control**: Git commits helped track progress

## 🎯 Future Improvements

**Short Term:**
- [ ] Add conversation history (multi-turn chat with context)
- [ ] Implement user authentication
- [ ] Add question categories/tags
- [ ] Export chat history (PDF/CSV)

**Long Term:**
- [ ] Deploy to cloud (Render/Heroku/AWS)
- [ ] Add support for multiple AI models (GPT-4, Claude, etc.)
- [ ] Implement voice input/output
- [ ] Create mobile app
- [ ] Add admin dashboard with analytics
- [ ] Implement caching for common questions
- [ ] Rate limiting per user
- [ ] Dark mode toggle

## 🔐 Security Considerations

**⚠️ IMPORTANT FOR PRODUCTION:**

This is a learning project. For production deployment:
- ✅ Use environment variables (implemented)
- ✅ Add `.gitignore` to exclude sensitive files
- ⚠️ Implement rate limiting (not yet done)
- ⚠️ Add user authentication (not yet done)
- ⚠️ Sanitize all user inputs (basic validation only)
- ⚠️ Use HTTPS in production
- ⚠️ Implement API key rotation
- ⚠️ Add request validation middleware

## 🤔 Reflection

### What Went Well
- Successfully integrated multiple APIs
- Created a working full-stack application
- Exceeded assignment requirements (CLI → Web App)
- Implemented proper error handling

### What Was Difficult
- Understanding Flask's folder structure initially
- Debugging MySQL connection issues
- Managing API keys securely
- Creating smooth async UI updates

### Time Breakdown
- Research & Planning: 3 hours
- Backend Development: 5 hours
- Frontend Development: 3 hours
- Database Integration: 2 hours
- Testing & Debugging: 4 hours
- Documentation: 2 hours
- **Total: ~19 hours**

### Would I Do Differently?
- Start with better project structure planning
- Use environment variables from day one
- Write tests alongside code
- Deploy earlier to catch issues

## 📝 Assignment Requirements Checklist

### Part 1: Setup ✅
- ✅ Installed Python
- ✅ Created GitHub repository
- ✅ Documented every step in README
- ✅ Included challenges and solutions

### Part 2: Core Task ✅
- ✅ Built AI Q&A Bot
- ✅ Uses OpenAI API for answers
- ✅ Fully functional application
- ✅ Error handling implemented

### Part 3: Stretch Goals ✅
- ✅ Added full web UI (Flask + Bootstrap)
- ✅ Database integration (MySQL)
- ✅ Went beyond minimum requirements
- ⏳ Deployment (in progress)

## 📄 License

This project is created for educational purposes as part of an internship assignment.

## 🙏 Acknowledgments

- **OpenAI** - For the GPT API and documentation
- **SerpAPI** - For web search capabilities
- **Flask Community** - For excellent documentation
- **Stack Overflow** - For debugging help
- **ChatGPT** - For explaining concepts when stuck
- **Bootstrap** - For UI components

## 👤 Author

**Shreyash Patil** 
- GitHub: [@yourusername](https://github.com/ShreyashPatil530)
- Email: shreyashpatil530@gmail.com
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/shreyash-patil-ba921737b/)

## 📞 Support

If you have questions or run into issues:
1. Check the [Issues](https://github.com/shreyashpatil530/ai-qa-system/issues) page
2. Create a new issue with details
3. Email me at: your.email@example.com

---

**Built with 💡 curiosity, 💪 effort, and lots of ☕ coffee!**

*"I didn't know how to do this when I started, but I figured it out. That's what matters."*
