#!/usr/bin/python3
#
# File: qaspeak.py - speak question asked and answer from Ollama  
# Usage: qaspeak.py <your question>
#
import requests
import subprocess
import sys
from framework.util.utils import Config

def speak_words(words: str):
  # speak the words passed in
   cmd = f"/usr/local/sbin/speak {words}"
   try:
     subprocess.check_output(cmd, shell=True)
     return 0                              # success
   except subprocess.CalledProcessError as e:
     return e.returncode

def answer_question(question: str, hub: str):
  # keep answers short by prepending: "short answer:" before the question
  speak_words(f"question: {question}")     # speak question
  model = "llama3.2:3b"                    # AI model
  info = {"model": f"{model}", 
          "prompt": f"Be concise. Do not use symbols other than punctuation. {question}", 
          "keep_alive": -1,                # keep model loaded indefinitely
          "stream": False
         }
  try:                                     # 11434 is well-known port of ollama
    answer = requests.post(f"http://{hub}:11434/api/generate", json=info)
    answer.raise_for_status()
    ans_text = answer.json().get("response", "No answer found")
    speak_words(f"answer: {ans_text}")     # speak answer
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
