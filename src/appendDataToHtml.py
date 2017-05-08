class AppendDataToHTML:
    
    def filterTags(self, tags, data):
        for i in range(len(data['outputs'][0]['data']['concepts']) - 1):
            if data['outputs'][0]['data']['concepts'][i]['value'] > 0.8800:
                tags += str(data['outputs'][0]['data']['concepts'][i]['name']) + " "
                #print data['outputs'][0]['data']['concepts'][i]['name']
        return tags
    def appendToHTML(self, tags, picLink):
        picLink = """<img src=""" + picLink + """>"""

        message = """<html>
        <head></head>
          <body>
            <p1>""" +  picLink + """ </p1>
            <p2>Picture is of: """ + tags + """</p2>
          </body>
        <br>
        <br>
        <br>
        </html>"""
        return message

    # def closeHTML(f):
    #     f.write(message)
    #     f.close()


