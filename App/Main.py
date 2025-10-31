from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.model_wrapper import RecipeChatModel

app = FastAPI()
chat_model = RecipeChatModel(model_name="fine_tuned_model")  # or pretrained if no fine-tuning

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    user_input = req.user_input
    # optionally use req.context for multi-turn
    bot_response = chat_model.generate_response(user_input=user_input)
    # you might update context here
    return ChatResponse(bot_response=bot_response, context=None)
