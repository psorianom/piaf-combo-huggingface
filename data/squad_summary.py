import json
import sys

if len(sys.argv) < 2:
    print("You need to give at least a Squad filename to summarize!")
    exit()

file_name = sys.argv[1]
squad_file = json.load(open(file_name))

version = squad_file["version"]
print(f"Dataset version: {version}")

nb_documents = len(squad_file["data"])
print(f"Number of documents (articles if Wikipedia): {nb_documents}")

nb_paragraphs = 0
nb_questions = 0
nb_answers = 0
for docu in squad_file["data"]:
    for paragraph in docu["paragraphs"]:
        nb_paragraphs += 1
        for qas in paragraph["qas"]:
            nb_questions += 1
            for answer in qas["answers"]:
                nb_answers += 1

print(f"Number of paragraphs: {nb_paragraphs}")

print(f"Number of questions: {nb_questions}")

print(f"Number of answers: {nb_answers}")