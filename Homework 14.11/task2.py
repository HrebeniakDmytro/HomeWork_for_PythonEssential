class English:
    def greeting(self):
        return "Hello, my friend!"

class Spanish:
    def greeting(self):
        return "Hola, mi amigo!"

def hello_friend(language1, language2):
    print(language1.greeting())
    print(language2.greeting())

english_greeting = English()
spanish_greeting = Spanish()

hello_friend(english_greeting, spanish_greeting)
