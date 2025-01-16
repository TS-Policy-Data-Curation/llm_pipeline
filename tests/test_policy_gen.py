import argparse
import pandas as pd
from utils.inference import create_policy_chain, format_time_series
from utils.inference import get_anthropic_llm, get_gemini_llm, get_openai_llm
import logging
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    logger = logging.getLogger()
    logging.basicConfig(filename="policy_gen.log", level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("split_fred_path", type=str, help="Path to the split FRED data")
    args = parser.parse_args()
    data = pd.read_csv(args.split_fred_path)

    llms = {
        "gemini": get_gemini_llm(0.8),
        "openai": get_openai_llm(0.8),
        "anthropic": get_anthropic_llm(0.8),
    }

    for name, llm in llms.items():
        print(name)
        logger.info(name)
        print(llm)
        logger.info(llm)

        policy_chain = create_policy_chain(llm)
        results = []
        for i, row in data.iterrows():
            print(i)
            time_series = format_time_series(row["history"])
            description = row["title"]

            logger.info(description)
            logger.info(time_series)

            res = policy_chain.invoke(
                {"description": description, "time_series": time_series}
            )

            print(res.content)
            logger.info(res.content)
            if i > 0:
                break
