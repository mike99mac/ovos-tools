#!/usr/bin/python3
#
# File: qaspeak.py - speak question asked and answer from Ollama  
# Usage: qaspeak.py <your question>
#
import requests
import subprocess
import sys

def speak_words(words: str):
  # speak the words passed in
   cmd = f"/usr/local/sbin/speak {words}"
   try:
     result = subprocess.check_output(cmd, shell=True)
     return 0             # success
   except subprocess.CalledProcessError as e:
     self.log.error(f"SimpleVoiceAssistant.mpc_cmd(): cmd: {cmd} returned e.returncode: {e.returncode}")
     return e.returncode

def answer_question(question: str):
  # keep answers short by prepending: "short answer:" before the question
  speak_words(f"question: {question}")     # speak question
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
    ans_text = answer.json().get("response", "No answer found")
    speak_words(f"answer: {ans_text}")     # speak answer
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
    question = " ".join(sys.argv[1:])      # question is all arguments
    answer_question(question)              # get the answer

