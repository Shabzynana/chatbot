# import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot("ChatBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english510")
trainer.train("chatterbot.corpus.yoruba510")


@app.route("/")
def index():
    return render_template("chatbot.html")


@app.route("/get_response")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True,port=5005)
