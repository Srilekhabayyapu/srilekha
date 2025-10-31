import argparse
from app.model_wrapper import RecipeChatModel

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_data", type=str, default="data/recipes_train.json", help="Path to fine-tune dataset")
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--lr", type=float, default=5e-5)
    args = parser.parse_args()

    model = RecipeChatModel(model_name="gpt2-small")
    model.fine_tune(train_data_path=args.train_data, epochs=args.epochs, lr=args.lr)
    # optionally save the model
    model.model.save_pretrained("fine_tuned_model")
    model.tokenizer.save_pretrained("fine_tuned_model")

if __name__ == "__main__":
    main()
