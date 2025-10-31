Project 1: Name Matching System  
### Features  
- Maintains a list of candidate names (e.g., 30+ names).  
- Accepts a user-entered name and computes similarity scores against the list.  
- Returns:  
  - The “best match” (highest similarity) with score.  
  - A ranked list of top N matches with their scores.

### Getting Started  
#### Prerequisites  
- Python 3.x  
- Recommended: `pip`  
- Python package: `rapidfuzz`

#### Installation  
```bash
pip install rapidfuzz
Usage
bash
Copy code
python name_matcher.py
The script will load a predefined list of names.

You will be prompted to input a name (or type quit to exit).

The system will display the best match and ranked list of similar names with scores.

Examples
matlab
Copy code
Enter a name (or ‘quit’ to exit): Geetha Reddy
Input Name : Geetha Reddy  
Best Match : geetha reddy (score 100%)  
Other Top Matches:  
  geetha reddy — 100%  
  geetha reddy rao — 90%  
  geetha k — 72%  
  …  
Notes & Future Improvements
The normalization logic is basic (lowercasing, stripping whitespace). You may extend it to remove diacritics, punctuation, map nicknames, etc.

You might experiment with different scorers from rapidfuzz.fuzz such as ratio, partial_ratio, token_sort_ratio depending on your dataset and variation patterns.

Consider reading the name list from an external file (CSV/JSON) instead of hard-coding.

If needed, expand to support batch input, JSON output, or integration into other applications.

Project 2: Local LLM Recipe Chatbot
Features
Load or fine-tune a local LLM model (for example from the Hugging Face Transformers library) on recipe dataset.

Expose an API endpoint via FastAPI which accepts a user message (e.g., “egg, onions”) and returns a JSON response with suggested recipe.

Provide a simple web UI (HTML/JS) to chat with the model.

Architecture & Components
model_wrapper.py: Handles loading of the model, tokenizer, inference logic.

fine_tune.py: Script to fine-tune the model on your dataset (data/recipes_train.json).

app/main.py: FastAPI server exposing /chat endpoint.

UI: ui/simple_web.html contains a basic chat interface that posts to the API and displays responses.

Dataset: In data/recipes_train.json, you provide recipe examples to train/fine-tune the model.

Getting Started
Prerequisites
Python 3.x

GPU recommended for fine-tuning (optional if using pretrained only).

Additional libraries: transformers, torch, fastapi, uvicorn, pydantic.

Installation
bash
Copy code
pip install -r requirements.txt
Contents of requirements.txt (example):

nginx
Copy code
fastapi
uvicorn
pydantic
transformers
torch
Training / Fine-Tuning
bash
Copy code
python fine_tune.py --train_data data/recipes_train.json --epochs 2 --lr 5e-5
This will load the base model (e.g., gpt2-small), fine-tune on your dataset, and save the model to fine_tuned_model/.

You may change --model_name, --epochs, --lr as per your hardware/resources.

Running the API Server
bash
Copy code
uvicorn app.main:app --reload
Default host: http://127.0.0.1:8000

API endpoint: POST http://127.0.0.1:8000/chat

Example request body:

json
Copy code
{
  "user_input": "egg, onions",
  "context": null
}
Example response:

json
Copy code
{
  "bot_response": "Here’s a simple omelette with egg and onions…",
  "context": null
}
Using the UI
Open ui/simple_web.html in your browser.

Enter ingredients in the input box (e.g., egg, onions) and click “Send”.

The chatbox will show your input and bot response.

Example Usage
Input: egg, onions

Bot Response: “Here’s a quick recipe: onion-egg stir-fry… [steps]”

Input: chicken, tomato, garlic

Bot Response: Suggests chicken-tomato-garlic dish.

Notes & Future Improvements
The fine-tuning logic in model_wrapper.py is basic — you may improve: data preprocessing, batching, validation, loss-tracking, checkpointing.

For better performance or larger dataset use a stronger model (e.g., gpt-neo, llama2, or quantised model depending on hardware).

You may extend context handling for multi-turn conversation.

The UI can be improved (React, WebSockets, streaming responses) and error handling added to API.

Consider deployment aspects (dockerisation, GPU vs CPU fallback, model size constraints).

Code Structure
text
Copy code
chatbot_project/
├── app/
│   ├── main.py            # FastAPI server
│   ├── model_wrapper.py   # model load + inference logic
│   └── schemas.py         # Pydantic request/response schemas
├── ui/
│   └── simple_web.html    # Basic web UI
├── data/
│   ├── recipes_train.json # Training dataset for fine-tuning
│   └── …                  # other data files
├── fine_tune.py           # Script to fine-tune model
├── name_matcher.py        # Script for name-matching system (Task 1)
├── requirements.txt       # Python dependencies
└── README.md              # This documentation
Setup Instructions (Windows / Linux)
Clone the repository.

bash
Copy code
git clone https://github.com/your-username/your-repo.git
cd your-repo
Create a virtual environment and activate it.

Linux/macOS:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Windows:

powershell
Copy code
python -m venv venv
.\venv\Scripts\activate
Install dependencies.

bash
Copy code
pip install -r requirements.txt
For Task 1 (Name Matching):

bash
Copy code
python name_matcher.py
Provide a name when prompted.

For Task 2 (Recipe Chatbot):

Optional: Fine-tune the model (if your dataset is ready).

bash
Copy code
python fine_tune.py --train_data data/recipes_train.json --epochs 2 --lr 5e-5
Start the API server.

bash
Copy code
uvicorn app.main:app --reload
Open ui/simple_web.html in your browser and chat.

Contributing
Contributions are welcome! You can help by:

Adding more names or datasets.

Improving normalization or similarity logic for Task 1.

Enhancing the fine-tuning process, UI, or multi-turn logic for Task 2.

Reporting bugs or suggesting features via Issues.

Forking the repository and submitting Pull Requests.

Please ensure your changes include documentation updates or sample data where applicable.

License
This project is open-source and licensed under the MIT License.
Feel free to use, modify, and distribute.

Contact
Your Name — your.email@example.com
GitHub: https://github.com/your-username

Thank you for exploring these projects! If you encounter any issues or have suggestions, feel free to open an issue or reach out.

pgsql
Copy code
