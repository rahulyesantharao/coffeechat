from coffeechat import app
from coffeechat.config import Config

if __name__ == '__main__':
    app.run(host='localhost', port=Config.PORT, debug=Config.DEBUG)