import os
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub


llm = ChatOpenAI(model="gpt-3.5-turbo")

query = """
Vou viajar para Madrid em Setembro de 2024. 
Quero que faça um roteiro de viagem para mim com os os eventos que irão ocorrer na data da viagem e com os preços de passagem de São Paulo para Madrid
"""

def researchAgent(query, llm):
    tools = load_tools(['ddg-search', 'wikipedia'], llm= llm)
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt, verbose=True)
    webContext = agent_executor.invoke({"input": query})
    return webContext['output']

print(researchAgent(query, llm))