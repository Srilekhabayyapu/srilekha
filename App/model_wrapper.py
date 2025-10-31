import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class RecipeChatModel:
    def __init__(self, model_name="gpt2-small", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
        self.model_name = model_name

    def fine_tune(self, train_data_path: str, epochs: int = 1, lr: float = 5e-5):
        """
        Stub: implement fine-tuning logic on your recipes dataset.
        e.g., load dataset, tokenize, train loop, save model.
        """
        print(f"Fine-tuning model {self.model_name} on {train_data_path} for {epochs} epochs")
        # [Implement training loop]
        pass

    def generate_response(self, user_input: str, max_length: int = 200) -> str:
        prompt = f"User: {user_input}\nBot:"
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_length=inputs["input_ids"].shape[1] + max_length,
                                      pad_token_id=self.tokenizer.eos_token_id)
        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Extract only bot reply (naively):
        bot_reply = text.split("Bot:")[-1].strip()
        return bot_reply
