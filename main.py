from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from os import curdir, sep

try:
    from RPi import GPIO

    rpi_import = True
except ImportError:
    rpi_import = False
from py_data.ext_check import ext_check
from py_data.replace_check import dataReplace


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            if self.path.find("?") != -1:
                args = self.path.split('?', 1)[1]
                path = self.path.split('?', 1)[0]
            else:
                path = self.path
            if path == "/" or path == "":
                path = "index.html"
            if len(path.split(".")) == 1:
                if path[-1] == "/":
                    path += "index.html"
                else:
                    path += "/index.html"
            elif path.split(".")[1] != "html":
                ext = path.split(".")[1]
                self.send_header("Content-Type", ext_check(ext))

            self.end_headers()
            url = urllib.parse.urlparse(self.path)
            print(url.path)

            f = open(curdir + sep + path, 'rb')
            out = False
            # args split;
            if self.path.find("?") != -1:
                args = args.replace("\&", "0927JUHNDG152")
                args = args.split("&")
                for i in range(0, len(args)):
                    args[i] = args[i].replace("0927JUHNDG152", "\&")
                    args[i] = {"name": args[i].split("=", 1)[0], "value": args[i].split("=", 1)[1]}

                # args use;
                for i in range(0, len(args)):
                    print(path)
                    if rpi_import:
                        if args[i]['name'] == "light" and path == "/index.html":
                            GPIO.setmode(GPIO.BCM)
                            GPIO.setup(23, GPIO.OUT)

                            print(args[i]['value'].lower())
                            get_r = args[i]['value'].lower()
                            if get_r[-1] == "/":
                                get_r = get_r[:-1]
                            if get_r == "true":
                                GPIO.output(23, True)
                                print(True)
                            elif get_r == "false":
                                GPIO.output(23, False)
                                print(False)
                            elif get_r == "status":
                                out = True
                                self.wfile.write(('{"result" :' + str(GPIO.input(23)) + '}').encode("UTF-8"))
                            # GPIO.cleanup()
            if out != True:
                self.wfile.write(dataReplace(f.read()))
            f.close()
            print(self.path)

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


address = ('localhost', 8800)
http = HTTPServer(address, myHandler)

http.serve_forever()
