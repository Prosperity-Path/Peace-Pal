from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class PredictEmotion(metaclass=SingletonMeta):
    def __init__(self):
        self.tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
        self.model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")
        self.emotion = pipeline('sentiment-analysis', 
                    model='arpanghoshal/EmoRoBERTa')

    def label_emotion(self, text):
        return self.emotion(text)
