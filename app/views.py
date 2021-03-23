"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app.forms import UserForm
from app.models import UserProfile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Michael Beckford")

@app.route('/property', methods=['GET','POST'])
def addProperty():
    form= UserForm()
    if request.method == "POST":
        if form.validate_on_submit() == True:
            #Gets the user input from the form
            proptitle = form.propertytitle.data
            description = form.description.data
            noofrooms = form.noofrooms.data
            noofbathrooms = form.noofbathrooms.data
            price = form.price.data
            proptype = form.propertytype.data
            location = form.location.data
            filename = uploadPhoto(form.property_picture.data)

            #create user object and add to database
            user = UserProfile(proptitle,description,noofrooms,noofbathrooms,price,proptype, location, filename)
            db.session.add(user)
            db.session.commit()

             # remember to flash a message to the user
            flash('Property information uploaded successfully.', 'success')
        else:
            flash('Property information not uploaded', 'danger')
        return redirect(url_for("properties"))  # they should be redirected to a secure-page route instead
    return render_template("addproperty.html", form=form)



#Save the uploaded photo to a folder
def uploadPhoto(upload):
    filename = secure_filename(upload.filename)
    upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return filename


@app.route("/properties")
def properties():
    user_profiles = db.session.query(UserProfile).all()
    return render_template("propertylist.html", users=user_profiles)

@app.route("/property/<userid>")
def propertyId(userid):
    user = db.session.query(UserProfile).filter_by(id=int(userid)).first()
    return render_template("individual.html", user=user)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
