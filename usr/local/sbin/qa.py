#!/usr/bin/python3
#
# File: qa.py - answer questions with Ollama  
# Usage: qa.py <your question>
#
import sys
import requests
from framework.util.utils import Config

def answer_question(question: str, hub: str):
  # keep answers short by prepending: "short answer:" before the question
  # TO DO: get the Ollam server and the model from Minimy config file
  model = "llama3.2:3b"                    # AI model
  info = {"model": f"{model}", 
          "prompt": f"Be concise. Do not use symbols other than punctuation. {question}", 
          "keep_alive": -1,                # keep model loaded indefinitely
          "stream": False
         }
  try:                                     # 11434 is well-known port of ollama
    answer = requests.post(f"http://{hub}:11434/api/generate", json=info)
    answer.raise_for_status()
    print(answer.json().get("response", "No answer found"))
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  cfg = Config()                           # get config file
  cfg_val = "Basic.Hub"
  try:
    hub = cfg.get_cfg_val(cfg_val)
    if hub is None:
      print(f"ERROR {cfg_val} not found in config file: {cfg.config_file}")
      sys.exit(1)
  except Exception as e:
    print(f"ERROR calling cfg.get_cfg_val(Basic.Hub): {e}")
  question = " ".join(sys.argv[1:])        # question is all arguments
  answer_question(question, hub)           # get the answer
