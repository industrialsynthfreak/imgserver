import asyncore
import socket
import logging
import sys

from client.image_tag_parser import ImageTagParser


class BasicClient(asyncore.dispatcher):
    client_log = '../client.log'

    def __init__(self, host='localhost', port=80, path='/', log=True):
        asyncore.dispatcher.__init__(self)

        self.log = log
        if log:
            logging.basicConfig(filename=self.client_log,
                                format='%(asctime)-15s: %(message)s',
                                level=logging.INFO, filemode='w')

        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.buffer = 'GET %s HTTP/1.0\r\n\r\n' % path
        if sys.version[0] != '2':
            self.buffer = bytes(self.buffer, 'ascii')
        self.tag_parser = ImageTagParser()

    def handle_connect(self):
        if self.log:
            logging.info('Connected!')

    def handle_read(self):
        data = self.recv(8192)
        if sys.version[0] != '2':
            data = data.decode('ascii')
        self.tag_parser.feed(data)
        if self.log and self.tag_parser.url:
            logging.info('Fetched %s' % self.tag_parser.url)

    def writable(self):
        return len(self.buffer) > 0

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

    def handle_close(self):
        self.close()
        if self.log:
            logging.info('Disconnected!')
