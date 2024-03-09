from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from sentence_transformers import CrossEncoder

model_path = "./nli-deberta-v3-xsmall"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
cross_encoder = CrossEncoder(model_path)

classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer, cross_encoder=cross_encoder)

sent = "how is llama different than key?"
candidate_labels = ["key creation", "key deletion", "balance query", "price check", "transfer", "timed transfer"]

def check_query(input):
    res = classifier(input, candidate_labels)
    return {'label' : res['labels'][0], 'score' : res['scores'][0]}
    
def process_query(input):
    res = check_query(input)
    if not res['score'] < 0.8:
        if res['label'] == "key creation":
            print("key creation")
        elif res['label'] == "key deletion":
            print("key deletion")
        elif res['label'] == "balance query":
            print("balance query")
        elif res['label'] == "transfer":
            print("transfer")
        elif res['label'] == "timed transfer":
            print("timed transfer")
        else:
            print("price check")
    else:
        print("invalid prompt")

res = process_query(sent)