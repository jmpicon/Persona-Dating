# app/model_training.py
from flask import Flask, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments
import os

app = Flask(__name__)

def fine_tune_model(filtered_text, model_path="gpt2", output_dir="fine_tuned_model"):
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    model = GPT2LMHeadModel.from_pretrained(model_path)

    temp_file_path = "temp_text.txt"
    with open(temp_file_path, 'w') as f:
        f.write(filtered_text)

    train_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=temp_file_path,
        block_size=128,
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
    )

    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
    )

    trainer.train()
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)

    os.remove(temp_file_path)

@app.route('/train', methods=['POST'])
def train():
    text = request.json.get('text')
    fine_tune_model(text)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
