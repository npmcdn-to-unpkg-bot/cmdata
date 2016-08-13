import os
import glob
from settings import STATIC_DIR
from apps.site.models import BusinessArea, User
from faker import Factory
from application import bcrypt

fake = Factory.create('en_US')

def create_data():

    ################################
    # Remove any pics in images/   #
    ################################
    print 'Removing images...'
    [os.remove(p) for p in glob.glob(os.path.join(STATIC_DIR, 'images/*'))]

    ###############################
    ### Create basic users    #####
    ###############################
    user = User()
    user.first_name = 'Miles'
    user.last_name = 'Granger'
    user.username = 'milesg'
    user.password = bcrypt.generate_password_hash('test')
    user.save()

    ###############################
    ### Create business areas #####
    ###############################
    print 'Building Business Areas...'
    for i in range(3):
        BusinessArea.create(
            title=fake.text(25),
            introduction=fake.paragraph(),
            image_path=fake.text(25)
        )

    return True