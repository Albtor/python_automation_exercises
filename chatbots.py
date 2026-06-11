from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# pip install chatterbot chaterbot_corpus
def chatterbot_test():
    chatbot = ChatBot('SupportBot')
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english')

    def get_response(user_input):
        response = chatbot.get_response(user_input)
        return response

    while True:
        user_input = input('Enter a command: ')
        if user_input.lower() == 'exit':
            break
        print('Bot:', get_response(user_input))



def chatterbot_method():
    chatbot = ChatBot('CustomerServiceBot')
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english')

    def get_response(user_input):
        response = chatbot.get_response(user_input)
        return response

    def customer_service_bot():
        print("Hello, I'm your Customer Service Assistant. How can I help?")

    while True:
        user_input = input('You: ')
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Ciao pescao")
            break
        response = get_response(user_input)
        print('Bot:', response)


# RASA:  pip install rasa
# rasa init
# rasa train
# rasa shell

