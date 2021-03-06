# Imports
from empower import app
from flask import render_template, url_for, send_file, abort


'''
Views
'''


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


'''
Error Handelers
'''


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

'''
@app.errorhandler(500)
def server_error(e):
    return render_template('500.py'), 500
'''

'''
SEO
'''


@app.route('/robots.txt', methods=['GET'])
def robots():
    return send_file('templates/seo/robots.txt')


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    sitemap_xml = render_template('seo/sitemap.xml')
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response