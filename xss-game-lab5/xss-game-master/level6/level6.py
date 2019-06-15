import webapp2 as webapp
import os
import jinja2

def render(tpl_path, context = {}):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)

class MainPage(webapp.RequestHandler):
 
    def get(self):
        if self.request.path == "/gadget.js":
            with open('gadget.js', 'r') as file:
                data = file.read()
                self.response.out.write(data)
        else:
            self.response.out.write(render('index.html'))
 
application = webapp.WSGIApplication([ ('.*', MainPage) ], debug=False)

def main():
    from paste import httpserver
    httpserver.serve(application, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()