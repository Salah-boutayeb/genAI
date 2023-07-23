import json
from flask import Flask, request, jsonify
from utils.resumeClassificationGPT import extract_text_from_pdf, generate_data_prompt
from services.service import get_similarity, embed_text
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def query_records(name):

    return jsonify({'response': 'hello world'})


@app.route('/matching_internships', methods=['POST'])
def match_resume():
    cv = request.json['resume']
    resume_text = extract_text_from_pdf(cv)
    extracted_data = generate_data_prompt(resume_text)
    list_data = [extracted_data]
    top_3 = get_similarity([embed_text(list_data)])

    return jsonify({"recommanded": str(top_3)})


app.run(debug=True)
