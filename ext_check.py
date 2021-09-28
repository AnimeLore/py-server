def ext_check(ext=""):
    ext_d = {"bz": "application/x-bzip", "bz2": "application/x-bzip2", "cda": "application/x-cdf",
             "csh": "application/x-csh", "css": "text/css; charset=utf-8",
             "csv": "text/csv; charset=utf-8", "doc": "application/msword",
             "docx": 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
             "eot": "application/vnd.ms-fontobject", "epub": "application/epub+zip",
             "gz": "application/gzip", "gif": "image/gif",
             "ico": "image/vnd.microsoft.icom", "ics": "text/calendar; charset=utf-8",
             "jar": "application/java-archive", "jpeg": "image/jpeg",
             "jpg": "image/jpeg", "js": "text/javascript; charset=utf-8",
             "mjs": "text/javascript; charset=uft-8", "json": "application/json",
             "jsonld": "application/ld+json", "mid": "audio/midi", "midi": "audio/midi",
             "mp3": "audio/mpeg", "mp4": "video/mp4", "mpeg": "video/mpeg",
             "mpkg": "application/vnd.apple.installer+xml",
             "odp": "application/vnd.oasis.opendocument.presentation",
             "ods": "application/vnd.oasis.opendocument.spreadsheet",
             "odt": "application/vnd.oasis.opendocument.text",
             "oga": "audio/ogg", "ogv": "video/ogg", "ogx": "application/ogg", "opus": "audio/opus",
             "otf": "font/otf", "png": "image/png", "pdf": "application/pdf",
             "php": "application/x-httpd-php", "ppt": "application/vnd.ms-powerpoint",
             "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
             "rar": "application/vnd.rar",
             "rtf": "application/rtf", "sh": "application/x-sh", "svg": "image/svg+xml",
             "swf": "application/x-shockwave-flash", "tar": "application/x-tar", "tif": "image/tiff",
             "tiff": "image/tiff",
             "ts": "video/mp2t", "ttf": "font/ttf", "txt": "text/plain; charset=utf-8",
             "vsd": "application/vnd.visio",
             "wav": "audio/wav", "weba": "audio/webm", "webm": "video/webm", "webp": "image/webp",
             "woff": "font/woff", "woff2": "font/woff2", "xhtml": "application/xhtml+xml",
             "xls": "application/vnd.ms-excel",
             "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
             "xml": "application/xml",
             "xul": "application/vnd.mozilla.xul+xml", "zip": "application/zip", "3gp": "video/3gpp",
             "3g2": "video/3gpp2", "7z": "application/x-7z-compressed"
             }
    if ext in ext_d:
        return ext_d[ext]
    else:
        return 'text/html; charset=utf-8'
