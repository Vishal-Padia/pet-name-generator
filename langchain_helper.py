import os
from langchain.llms import HuggingFaceHub, OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")

load_dotenv()

# repo_id = "meta-llama/Llama-2-13b"
def generate_pet_name(animal_type, pet_color):
    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature":0.7}
    )

    llm = OpenAI(temperature=0.5)

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have an {animal_type} pet of {pet_color} color and I want a cool name for it. Suggest 5 cool for my pet."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

    response = name_chain({'animal_type' : animal_type, 'pet_color':pet_color})
    return response

def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )

    return result
if __name__ == '__main__':
    # langchain_agent()
    print(generate_pet_name("cat", "brown"))