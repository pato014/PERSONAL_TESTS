# import os
#
# import openai
#
#
# class Chatbot:
#     def __init__(self):
#         openai.api_key = "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"
#
#     def get_response(self, user_input):
#         response = openai.Completion.create(
#             engine="davinci",
#             prompt=user_input,
#             max_tokens=50,
#             api_key="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"
#         ).choices[0].text
#
#         return response

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit

import openai

class ChatBotApp(QMainWindow):
    def __init__(self, api_key):
        super().__init__()

        self.api_key = api_key

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chat Bot')
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(50, 50, 700, 400)

        self.send_button = QPushButton('Send', self)
        self.send_button.setGeometry(50, 480, 100, 50)
        self.send_button.clicked.connect(self.get_bot_response)

    def get_bot_response(self):
        user_input = self.text_edit.toPlainText()

        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input,
            max_tokens=50,
            api_key=self.api_key
        )

        bot_reply = response.choices[0].text.strip()
        self.text_edit.append(f'Bot: {bot_reply}')

def main(api_key):
    app = QApplication(sys.argv)
    window = ChatBotApp(api_key)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    # Replace "YOUR_API_KEY" with your actual API key
    api_key = "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"
    main(api_key)