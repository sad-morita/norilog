from flask import Flask
application = Flask(__name__)

# （中略）

def main():
    application.run('127.0.0.1', 8000)

if __name__ == '__main__':
    # IPアドレス127.0.0.1の8000番ポートでアプリケーションを実行します
    application.run('127.0.0.1', 8000, debug=True)

