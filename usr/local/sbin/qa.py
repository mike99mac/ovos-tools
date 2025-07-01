#!/usr/bin/python3
#
# File: qa.py - answer questions with Ollama  
# Usage: qa.py <your question>
#
import sys
import requests

def answer_question(question: str):
  # keep answers short by prepending: "short answer:" before the question
  # TO DO: get the Ollam server and the model from Minimy config file
  hub = "papabear"                         # host name of Ollama server
  model = "gemma3"                         # AI model
  info = {"model": f"{model}", 
          "prompt": f"short answer: {question}", 
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
    question = " ".join(sys.argv[1:])      # question is all arguments
    answer_question(question)              # get the answer

