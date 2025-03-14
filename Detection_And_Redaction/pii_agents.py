from langchain.agents import initialize_agent,AgentType,Tool
from transformers import pipeline

ner_pipeline=pipeline(task="ner",model="dbmdz/bert-large-cased-finetuned-conll03-english")

@Tool
def detect_pii_with_agent(text):
    entities=ner_pipeline(text)
    pii_data=[entity['word'] for entity in entities if entity['entity'] in ["B-PER", "I-PER", "B-LOC", "B-ORG"]]
    for word in pii_data:
        text=text.replace(word,"[REDACTED]")
        return text

    pii_agent = initialize_agent(
        tools=[detect_pii_with_agent],  # Register our @Tool function
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
)






