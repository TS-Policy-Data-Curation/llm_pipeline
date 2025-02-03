import argparse
import pandas as pd
from inference import create_policy_chain, format_time_series, summarize_policy_chain, create_autograder_chain
from inference import get_anthropic_llm, get_gemini_llm, get_openai_llm, get_deepseek_llm
from autograder_prompt import rubric_prompt, autograder_prompt
import logging
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    logger = logging.getLogger()
    logging.basicConfig(filename="autograder_scores.log", level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("split_fred_path", type=str, help="Path to the split FRED data")
    # parser.add_argument("gdelt_path", type=str, help="Path to the policy text data from Gdelt")
    args = parser.parse_args()
    time_series_data = pd.read_csv(args.split_fred_path)
    # policy_text = pd.read_csv(args.gdelt_path)

    llms = {
        # "gemini": get_gemini_llm(0.8),
        # "openai": get_openai_llm(0.8),
        # "anthropic": get_anthropic_llm(0.8),
        "deepseek": get_deepseek_llm(0.8),
    }

    for name, llm in llms.items():
        print(name)
        logger.info(name)
        print(llm)
        logger.info(llm)

        # Create the summarization chain using the selected LLM.
        summary_chain = summarize_policy_chain(llm)
        
        # Concatenate all policy texts into a single string.
        # Here we assume that each policy is contained in the "title" column.
        # You could also use bullet points for better separation:
        # all_policy_descriptions = "\n".join(f"- {desc}" for desc in time_series_data["title"].tolist())
        # all_policy_descriptions = "\n".join(policy_text["title"].tolist())

        # Summarize all policies in one go.
        # combined_policy_summary = summary_chain.invoke({
        #     "policy_description": all_policy_descriptions
        # }).content

        # logger.info("Combined Policy Summary:")
        # logger.info(combined_policy_summary)

        # Create the policy generation chain.
        policy_chain = create_policy_chain(llm)
        # results = []
        
        autograder_chain = create_autograder_chain(llm)
        
        for i, row in time_series_data.iterrows():
            print(i)
            
            time_series = format_time_series(row["history"])
            description = row["title"]
            
            # Instead of summarizing per row, use the combined summary.
            # policy_summary = combined_policy_summary
            policy_summary = ""

            # logger.info("Description: %s", description)
            # logger.info("Time Series: %s", time_series)
            # logger.info("Policy Summary: %s", policy_summary)

            # Invoke the policy generation chain with the time series, individual description,
            # and the combined policy summary.
            res = policy_chain.invoke({
                "description": description,
                "time_series": time_series,
                "policy_summary": policy_summary
            })

            # print(res.content)
            # logger.info("Result: %s", res.content)
            
            score = autograder_chain.invoke({
                "rubric_prompt": rubric_prompt,
                "llm_response": res.content
            })
            
            print(f"Time Series: {description} \n Score: {score.content}")
            score_log = "Time Series: " + description + "\n Score: " + score.content
            logger.info("Autograder Score: %s", score_log)
            # Example: break early for testing purposes.
            break
