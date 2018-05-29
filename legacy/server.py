from twisted.internet import reactor
from twisted.internet.protocol import Protocol,Factory, ServerFactory
from twisted.protocols.basic import LineReceiver
from twisted.python import log
import sys


class SimpleLogger(LineReceiver):

    def connectionMade(self):
        self.client_ip = self.transport.client
        if len(self.factory.clients) >= self.factory.clients_max:
            log.msg("Too many connections. bye !")
            self.client_ip = None
            self.transport.loseConnection()
        else:
            print self.client_ip
            self.factory.clients.append(self.client_ip)

    def connectionLost(self, reason):
        print 'disconnected'

    def lineReceived(self, line):
        print line


class MyFactory(ServerFactory):
    protocol = SimpleLogger

    def __init__(self, clients_max=10):
        self.clients_max = clients_max
        self.clients = []

log.startLogging(sys.stdout)
reactor.listenTCP(10000, MyFactory(5))
reactor.run()
