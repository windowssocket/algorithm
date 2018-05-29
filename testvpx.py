from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("-t", "--test", dest="test", help="testtest", default="default", action="store", metavar="helloworld")
parser.add_option("-v", "--verbose", dest="verbose", help="vvv", action="store_true", metavar="vvvvvvvvv")

(options, args) = parser.parse_args()

print os.path.join(os.path.sep, 'test')
print os.path.abspath(os.path.dirname(__file__)+ "/../../")


