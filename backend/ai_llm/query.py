from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from sentence_transformers import CrossEncoder
from .modules import price_check, create_key

model_path = "./ai_llm/nli-deberta-v3-xsmall"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
cross_encoder = CrossEncoder(model_path)

classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer, cross_encoder=cross_encoder)

# sent = "create a new key title John"

candidate_labels = ["key creation", "key deletion", "balance query", "price query", "transfer", "timed transfer", "address addition", "address removal"]

def check_query(input):
    res = classifier(input, candidate_labels)
    return {'label' : res['labels'][0], 'score' : res['scores'][0]}
    
async def process_query(input):
    _temp = check_query(str(input))
    if not _temp['score'] < 0.75:
        if _temp['label'] == "key creation":
            res = await create_key(input)
            return res
        elif _temp['label'] == "key deletion":
            print("key deletion")
        elif _temp['label'] == "balance query":
            print("balance query")
        elif _temp['label'] == "transfer":
            print("transfer")
        elif _temp['label'] == "timed transfer":
            print("timed transfer")
        else:
            res = await price_check(input)
            return res
    else:
        print(_temp)
    return "please try again with a different prompt"

# process_query("what is the price of Ethereum ?")