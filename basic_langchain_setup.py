from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

local_path = './models/gpt4all-converted.bin' 
callback_manager = [StreamingStdOutCallbackHandler()]
# Use the new "output_callback" keyword argument instead of "new_text_callback"

template = """Question: {question}

Answer: Let's think step by step.

"""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = GPT4All(model=local_path, verbose=True)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

llm_chain.predict(question, callbacks=callback_manager)

# from langchain import PromptTemplate, LLMChain
# from langchain.llms import GPT4All
# from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# local_path = './models/gpt4all-converted.bin'
# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# template = """Question: {question}

# Answer: Let's think step by step.

# """

# prompt = PromptTemplate(template=template, input_variables=["question"])
# llm = GPT4All(model=local_path,
#               callback_manager=callback_manager, verbose=True)
# llm_chain = LLMChain(prompt=prompt, llm=llm)

# question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

# # question = input("Enter your question: ")

# llm_chain.predict(question=question)