from flask import Flask, render_template
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

deroos = {'active':[
                 {'scholar_name': 'alhabib',
                  'sex': 'm',
                  'topic': 'Tazkeyah',
                  'title': 'Kabas Al Noor Al Mobeen Men Ihyaa Uloom Al Deen',
                  'location': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d29355.758025942734!2d31.246216399673987!3d30.04779539037385!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMzDCsDAyJzUyLjEiTiAzMcKwMTUnNDkuNCJF!5e1!3m2!1sen!2sus!4v1521598252622',
                  'schedule':
                                {'weekly_or_monthly': 'w',
                                 'week_day': 'Mon',
                                 'am_pm': 'PM',
                                 'start_time': '9:00',
                                 'end_time' : '10:00'
                                }
                  },
                  
                { 'scholar_name': 'muhammad mehanna',
                  'sex': 'm',
                  'topic': 'Tazkeyah',
                  'title': 'shar7 ketab Ihyaa Uloom Al Deen',
                  'location': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3669.5478245093313!2d31.260496415259176!3d30.04568798188196!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x145840a2f3fd21f5%3A0x676752c74b1e52e8!2sAl-Azhar+Mosque!5e1!3m2!1sen!2sus!4v1521598500037',
                  'schedule':
                                {'weekly_or_monthly': 'm',
                                'week_day': 'Tue',
                                'am_pm': 'AM',
                                'start_time': '9:00',
                                'end_time' : '10:00'
                                }
                  },
                { 'scholar_name': 'ali gomaa',
                  'sex': 'm',
                  'topic': 'Iftaa',
                  'title': 'Magles el gomaa',
                  'location': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3672.106349357143!2d30.979733965257697!3d29.976550381906968!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1458572a278e4c25%3A0x12ccf9e8eab22aec!2sFadel+Mosque%2C+Giza+Governorate%2C+Egypt!5e1!3m2!1sen!2sus!4v1521598451261',
                  'schedule':
                                {'weekly_or_monthly': 'm',
                                'week_day': 'Tue',
                                'am_pm': 'AM',
                                'start_time': '9:00',
                                'end_time' : '10:00'
                                }
                  },
                 {'scholar_name': 'mo3ez mas3ood',
                  'sex': 'm',
                  'topic': 'falsafah',
                  'title': 'ketab 2bn 3ata2 allah',
                  'location': 'https://goo.gl/maps/zj7RqYZAcqk',
                  'schedule':
                                {'weekly_or_monthly': 'm',
                                 'week_day': 'Tue',
                                 'am_pm': 'AM',
                                 'start_time': '9:00',
                                 'end_time' : '10:00'
                                }
                  }],

          'inactive':[
                  {'scholar_name': 'amr elwerdany',
                  'sex': 'm',
                  'topic': 'fiqh',
                  'title': 'ketab 2bn 3ata2 allah',
                  'location': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3672.106349357143!2d30.979733965257697!3d29.976550381906968!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1458572a278e4c25%3A0x12ccf9e8eab22aec!2sFadel+Mosque%2C+Giza+Governorate%2C+Egypt!5e1!3m2!1sen!2sus!4v1521598451261',
                  'schedule':
                                {'weekly_or_monthly': 'm',
                                 'week_day': 'Tue',
                                 'am_pm': 'AM',
                                 'start_time': '9:00',
                                 'end_time' : '10:00'
                                }
                  }]
        }

@app.route('/')
def home():
    return render_template('index.html')

      # return 'zakeeha API v1.0 - This is an attempt to collect information around available/active\n'\
      # 'islamic sessions/seminars and serve them in a RESTful API available for consumption by anyone for free.\n\n'\
      # 'The following is a list of available GET endpoints (so far):\n'\
      # '- /all_deroos (returns all available lists of deroos whether active or not\n'\
      # '- /active_deroos (returns a list of active deroos only\n'\
      # '- /inactive_deroos (return a list of inactive deroos only\n'\
      # '- /scholar_names (retruns a list of names for all available scholars\n'\
      # '- /all_deroos/<scholar_name> returns a list of all deroos by scholar_name'

class all_deroos(Resource):
    def get(self):
        return deroos

class active_deroos(Resource):
    def get(self):
        return deroos['active']

class inactive_deroos(Resource):
    def get(self):
        return deroos['inactive']

class scholar_names(Resource):
    def get(self):
        scholar_names = []
        for dars in (deroos['active'] + deroos['inactive']):
                if dars['scholar_name'] not in scholar_names:
                        scholar_names.append(dars['scholar_name'])

        return scholar_names

class deroos_by_scholar_name(Resource):
    def get(self, scholar_name):
        if scholar_name not in scholar_names.get(self):
            abort(404, message="Scholar {} doesn't exist".format(scholar_name))

        deroos_by_scholar_name = []
        for dars in (deroos['active'] + deroos['inactive']):
            if dars['scholar_name'] == scholar_name:
                deroos_by_scholar_name.append(dars)

        return deroos_by_scholar_name


#api.add_resource(welcome, '/')
api.add_resource(all_deroos, '/all_deroos')
api.add_resource(active_deroos, '/active_deroos')
api.add_resource(inactive_deroos, '/inactive_deroos')
api.add_resource(scholar_names, '/scholar_names')
api.add_resource(deroos_by_scholar_name, '/all_deroos/<scholar_name>')


if __name__ == '__main__':
    app.run(debug=True)
