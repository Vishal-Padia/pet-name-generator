import os
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")

load_dotenv()

repo_id = "databricks/dolly-v2-3b"

def generate_pet_name(num_names=5):
    llm = HuggingFaceHub(
        repo_id=repo_id,
        model_kwargs={"temperature": 0.5,
                      "max_length": 64}
    )
    name = llm("I have a dog pet and I want a cool name for it. Suggest me a five cool names for my pet dog.")
    return name

if __name__ == '__main__':
    print(generate_pet_name())