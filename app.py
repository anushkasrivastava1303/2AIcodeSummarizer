# app.py
from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import ast
import re

app = Flask(__name__)

model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-base")
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-base")

def extract_functions(code):
    tree = ast.parse(code)
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node)

    return functions

def get_function_code(code, function_node):
    function_code = ast.get_source_segment(code, function_node)
    function_code = re.sub(r'\n\s*\n', '\n', function_code)
    function_code = function_code.strip()

    return function_code

def summarize_code(code_snippet):
    inputs = tokenizer.encode("Summarize this Python code: " + code_snippet,
                              return_tensors="pt", max_length=512, truncation=True)

    outputs = model.generate(inputs, max_length=64,
                             num_beams=4, no_repeat_ngram_size=2)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    code_snippet = request.form['code']
    
    print("Received code snippet:", code_snippet)

    functions = extract_functions(code_snippet)
    summaries = []

    for func in functions:
        func_code = get_function_code(code_snippet, func)
        summary = summarize_code(func_code)
        print(summary)
        summaries.append((func.name, summary))

    print("Summaries:", summaries)

    return jsonify({'summaries': summaries})

if __name__ == "__main__":
    app.run(debug=True)
