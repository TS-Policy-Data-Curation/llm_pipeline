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
    api_key = get_api_key("GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=temp,
        max_retries=2,
        api_key=api_key,
    )
    return llm


def get_openai_llm(temp: float):
    api_key = get_api_key("OPENAI_API_KEY")
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temp,
        max_retries=2,
        api_key=api_key,
    )
    return llm


def get_anthropic_llm(temp: float):
    api_key = get_api_key("ANTHROPIC_API_KEY")
    llm = ChatAnthropic(
        model="claude-3-5-sonnet-20241022",
        temperature=temp,
        max_retries=2,
        api_key=api_key,
    )

    return llm


def create_policy_chain(llm):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are given a time series from real world data and its description. You are responsible for"
                "identifying a policy that may have affected the time series."
                "You may reason in a block enclosed by <SCRATCH></SCRATCH>. Afterwards, only the description of the"
                "policy should be returned.",
            ),
            (
                "user",
                "Identify a policy that may have affected this time series."
                "Description:\n{description}\n"
                "Time Series Data:\n{time_series}",
            ),
        ]
    )

    chain = prompt | llm

    return chain
