from ast import literal_eval
import os
import getpass
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


model = ChatAnthropic(model="claude-3-5-sonnet-20240620")


def format_time_series(time_series: list[tuple[str, str]]) -> str:
    if type(time_series) != list:
        time_series = literal_eval(time_series)
    return "\n".join([f"({date}, {value})" for date, value in time_series])


def get_api_key(key_name: str = "ANTHROPIC_API_KEY") -> str:
    if os.environ.get(key_name):
        return os.environ[key_name]
    return getpass.getpass("Enter your API key: ")


def get_gemini_llm(temp: float):

    '''Creates an instance of the ChatGoogleGenerativeAI class using gemini 1.5 pro LLM with the specified temperature.'''

    api_key = get_api_key("GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=temp,
        max_retries=2,
        api_key=api_key,
    )
    return llm


def get_openai_llm(temp: float):

    '''Creates an instance of the ChatOpenAI class using gpt-4o-mini LLM with the specified temperature.'''

    api_key = get_api_key("OPENAI_API_KEY")
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temp,
        max_retries=2,
        api_key=api_key,
    )
    return llm


def get_anthropic_llm(temp: float):

    '''Creates an instance of the ChatAnthropic class using claude 3.5 sonnet LLM with the specified temperature.'''

    api_key = get_api_key("ANTHROPIC_API_KEY")
    llm = ChatAnthropic(
        model="claude-3-5-sonnet-20241022",
        temperature=temp,
        max_retries=2,
        api_key=api_key,
    )

    return llm


def create_policy_chain(llm):

    '''Creates a pipeline that prompts the LLM to identify a policy based on a description of the policy and a time series.'''
    
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are given a time series from real world data, its description and its summary. You are responsible for"
                "identifying a policy that may have affected the time series."
                "You may reason in a block enclosed by <SCRATCH></SCRATCH>. Afterwards, only the description of the"
                "policy should be returned.",
            ),
            (
                "user",
                "Identify a policy that may have affected this time series."
                "Description:\n{description}\n"
                "Time Series Data:\n{time_series}"
                "Policy Summary: \n{policy_summary}",
            ),
        ]
    )

    chain = prompt | llm

    return chain

def summarize_policy_chain(llm):
    
    '''Creates a pipeline that prompts the LLM to summarize a policy based on a description of the policy.'''
    
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are given a description of a policy and are responsible for summarizing the policy."
                "You may reason in a block enclosed by <SCRATCH></SCRATCH>. Afterwards, only the summary of the"
                "policy should be returned.",
            ),
            (
                "user",
                "Summarize the policy described below:\n{policy_description}",
            ),
        ]
    )

    chain = prompt | llm

    return chain