import os
import json
import random
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.web import url


class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        face_pics = ['cat.gif', 'fere.gif', 'lion.gif']
        img_name = random.choice(face_pics)
        self.render('index.html', img_path=self.static_url('images/' + img_name))

#サーバサイドでメインの処理
#waitersとmessagesに接続している人と送られてきたメッセージを記録
class ChatHandler(tornado.websocket.WebSocketHandler):

    waiters = set()
    messages = []

#接続してきた人の登録と、その人に対して今までのログを送信
    def open(self, *args, **kwargs):
        self.waiters.add(self)
        self.write_message({'messages': self.messages})
        
#メッセージが送られてきたときに送られてきたメッセージを自分以外の参加者にブロードキャスト
#このとき送られてきたメッセージはログに追加
    def on_message(self, message):
        message = json.loads(message)
        self.messages.append(message)
        for waiter in self.waiters:
            if waiter == self:
                continue
            waiter.write_message({'img_path': message['img_path'], 'message': message['message']})

#接続が切断されたときにwaitersから接続者を削除
#切断された人にはメッセージをブロードキャストしないようにする
    def on_close(self):
        self.waiters.remove(self)


class Application(tornado.web.Application):

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        tornado.web.Application.__init__(self,
                                         [
                                         url(r'/', IndexHandler, name='index'),
                                         url(r'/chat', ChatHandler, name='chat'),
                                         ],
                                         template_path=os.path.join(BASE_DIR, 'templates'),
                                         static_path=os.path.join(BASE_DIR, 'static'),
                                         )


if __name__ == '__main__':
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
