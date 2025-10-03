const questionForm = document.getElementById('questionForm');
const questionInput = document.getElementById('questionInput');
const chatBox = document.getElementById('chatBox');
const submitBtn = document.getElementById('submitBtn');
const btnText = document.getElementById('btnText');
const btnSpinner = document.getElementById('btnSpinner');
const useSearchCheckbox = document.getElementById('useSearch');

// Add message to chat
function addMessage(text, isUser) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'ai-message'}`;
    
    const label = document.createElement('div');
    label.className = `message-label ${isUser ? 'user-label' : 'ai-label'}`;
    label.textContent = isUser ? 'You' : 'AI Assistant';
    
    const content = document.createElement('div');
    content.textContent = text;
    
    messageDiv.appendChild(label);
    messageDiv.appendChild(content);
    chatBox.appendChild(messageDiv);
    
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Clear welcome message
function clearWelcome() {
    if (chatBox.querySelector('.text-muted')) {
        chatBox.innerHTML = '';
    }
}

// Handle form submission
questionForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const question = questionInput.value.trim();
    if (!question) return;
    
    clearWelcome();
    addMessage(question, true);
    
    questionInput.value = '';
    submitBtn.disabled = true;
    btnText.classList.add('d-none');
    btnSpinner.classList.remove('d-none');
    
    try {
        const response = await fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                question: question,
                use_search: useSearchCheckbox.checked
            })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            addMessage(data.answer, false);
        } else {
            addMessage('Error: ' + data.answer, false);
        }
        
    } catch (error) {
        addMessage('Connection error. Please try again.', false);
        console.error('Error:', error);
    } finally {
        submitBtn.disabled = false;
        btnText.classList.remove('d-none');
        btnSpinner.classList.add('d-none');
    }
});