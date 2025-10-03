from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_answer
from database import log_question_answer
from datetime import datetime

app = Flask(__name__, 
            template_folder='frontend/template',
            static_folder='frontend/static')
CORS(app)

@app.route('/')
def index():
    """Serve the main chat interface"""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    """API endpoint to handle question answering"""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        use_search = data.get('use_search', False)
        
        if not question:
            return jsonify({
                'status': 'error',
                'answer': 'Please provide a valid question.'
            }), 400
        
        answer = get_answer(question, use_search=use_search)
        timestamp = datetime.now()
        log_question_answer(question, answer, timestamp)
        
        return jsonify({
            'status': 'success',
            'answer': answer
        })
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'status': 'error',
            'answer': f'An error occurred: {str(e)}'
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    print("Starting Q&A System on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)