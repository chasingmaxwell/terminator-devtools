import terminatorlib.plugin as plugin
AVAILABLE = ['ChromeDevToolsURLHandler']
available = AVAILABLE

class ChromeDevToolsURLHandler(plugin.URLHandler):
    capabilities = ['url_handler']
    handler_name = 'devtools_url'
    nameopen = 'Open devtools'
    namecopy = 'Copy devtools URL'
    match = '\\bchrome-devtools:.*\\b'

    def callback(self, url):
        return(url)
