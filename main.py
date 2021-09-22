from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from os import curdir, sep
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            if self.path.find("?") != -1:
                args = self.path.split('?', 1)[1]
                path = self.path.split('?', 1)[0]
            else:
                path = self.path
            if path == "/":
                path = "index.html"
            if len(path.split(".")) == 1:
                if path[-1] == "/":
                    path += "index.html"
                else:
                    path += "/index.html"
            elif path.split(".")[1] != "html":
                ext = path.split(".")[1]
                if ext == "bz":
                
                    self.send_header("Content-Type", 'application/x-bzip')
                elif ext == "bz2":
                    self.send_header("Content-Type", 'application/x-bzip2')
                elif ext == "cda":
                    self.send_header("Content-Type", 'application/x-cdf')
                elif ext == "csh":
                    self.send_header("Content-Type", 'application/x-csh')
                elif ext == "css":
                    self.send_header("Content-Type", 'text/css; charset=utf-8')
                elif ext == "csv":
                    self.send_header("Content-Type", 'text/csv; charset=utf-8')
                elif ext == "doc":
                    self.send_header("Content-Type", 'application/msword')
                elif ext == "docx":
                    self.send_header("Content-Type", 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                elif ext == "eot":
                    self.send_header("Content-Type", 'application/vnd.ms-fontobject')
                elif ext == "epub":
                    self.send_header("Content-Type", 'application/epub+zip')
                elif ext == "gz":
                    self.send_header("Content-Type", 'application/gzip')
                elif ext == "gif":
                    self.send_header("Content-Type", 'image/gif')
                elif ext == "ico":
                    self.send_header("Content-Type", 'image/vnd.microsoft.icom')
                elif ext == "ics":
                    self.send_header("Content-Type", 'text/calendar; charset=utf-8')
                elif ext == "jar":
                    self.send_header("Content-Type", 'application/java-archive')
                elif ext == "jpeg" or ext == "jpg":
                    self.send_header("Content-Type", 'image/jpeg')
                elif ext == "js" or ext == "mjs":
                    self.send_header("Content-Type", 'text/javascript; charset=utf-8')
                elif ext == "json":
                    self.send_header("Content-Type", 'application/json')
                elif ext == "jsonld":
                    self.send_header("Content-Type", 'application/ld+json')
                elif ext == "mid" or ext == "midi":
                    self.send_header("Content-Type", 'audio/midi')
                elif ext == "mp3":
                    self.send_header("Content-Type", 'audio/mpeg')
                elif ext == "mp4":
                    self.send_header("Content-Type", 'video/mp4')
                elif ext == "mpeg":
                    self.send_header("Content-Type", 'video/mpeg')
                elif ext == "mpkg":
                    self.send_header("Content-Type", 'application/vnd.apple.installer+xml')
                elif ext == "odp":
                    self.send_header("Content-Type", 'application/vnd.oasis.opendocument.presentation')
                elif ext == "ods":
                    self.send_header("Content-Type", 'application/vnd.oasis.opendocument.spreadsheet')
                elif ext == "odt":
                    self.send_header("Content-Type", 'application/vnd.oasis.opendocument.text')
                elif ext == "oga":
                    self.send_header("Content-Type", 'audio/ogg')
                elif ext == "ogv":
                    self.send_header("Content-Type", 'video/ogg')
                elif ext == "ogx":
                    self.send_header("Content-Type", 'application/ogg')
                elif ext == "opus":
                    self.send_header("Content-Type", 'audio/opus')
                elif ext == "otf":
                    self.send_header("Content-Type", 'font/otf')
                elif ext == "png":
                    self.send_header("Content-Type", 'image/png')
                elif ext == "pdf":
                    self.send_header("Content-Type", 'application/pdf')
                elif ext == "php":
                    self.send_header("Content-Type", 'application/x-httpd-php')
                elif ext == "ppt":
                    self.send_header("Content-Type", 'application/vnd.ms-powerpoint')
                elif ext == "pptx":
                    self.send_header("Content-Type", 'application/vnd.openxmlformats-officedocument.presentationml.presentation')
                elif ext == "rar":
                    self.send_header("Content-Type", 'application/vnd.rar')
                elif ext == "rtf":
                    self.send_header("Content-Type", 'application/rtf')
                elif ext == "sh":
                    self.send_header("Content-Type", 'application/x-sh')
                elif ext == "svg":
                    self.send_header("Content-Type", 'image/svg+xml')
                elif ext == "swf":
                    self.send_header("Content-Type", 'application/x-shockwave-flash')
                elif ext == "tar":
                    self.send_header("Content-Type", 'application/x-tar')
                elif ext == "tif" or ext == "tiff":
                    self.send_header("Content-Type", 'image/tiff')
                elif ext == "ts":
                    self.send_header("Content-Type", 'video/mp2t')
                elif ext == "ttf":
                    self.send_header("Content-Type", 'font/ttf')
                elif ext == "txt":
                    self.send_header("Content-Type", 'text/plain; charset=utf-8')
                elif ext == "vsd":
                    self.send_header("Content-Type", 'application/vnd.visio')
                elif ext == "wav":
                    self.send_header("Content-Type", 'audio/wav')
                elif ext == "weba":
                    self.send_header("Content-Type", 'audio/webm')
                elif ext == "webm":
                    self.send_header("Content-Type", 'video/webm')
                elif ext == "webp":
                    self.send_header("Content-Type", 'image/webp')
                elif ext == "woff":
                    self.send_header("Content-Type", 'font/woff')
                elif ext == "woff2":
                    self.send_header("Content-Type", 'font/woff2')
                elif ext == "xhtml":
                    self.send_header("Content-Type", 'application/xhtml+xml')
                elif ext == "xls":
                    self.send_header("Content-Type", 'application/vnd.ms-excel')
                elif ext == "xlsx":
                    self.send_header("Content-Type", 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                elif ext == "xml":
                    self.send_header("Content-Type", 'application/xml')
                elif ext == "xul":
                    self.send_header("Content-Type", 'application/vnd.mozilla.xul+xml')
                elif ext == "zip":
                    self.send_header("Content-Type", 'application/zip')
                elif ext == "3gp":
                    self.send_header("Content-Type", 'video/3gpp')
                elif ext == "3g2":
                    self.send_header("Content-Type", 'video/3gpp2')
                elif ext == "7z":
                    self.send_header("Content-Type", 'application/x-7z-compressed')
            else:
                self.send_header("Content-Type", 'text/html; charset=utf-8')
            self.end_headers()
            url = urllib.parse.urlparse(self.path)
            print(url.path)

            f = open(curdir + sep + path, 'rb')

            self.wfile.write(f.read())
            f.close()
            print(self.path)
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


address = ('localhost', 8800)
http = HTTPServer(address, myHandler)

http.serve_forever()
