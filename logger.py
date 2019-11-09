import logging

# Prior to v3.6 string formatting was limited to "%s" or string.format().
#
# "%s" is the oldest and has limitations with tuples and dictionaries.
# "My name is %s and I am %s years old" % (name, age)
#
# string.format() came in v2.6
# "My name is {} and I am {}".format(name, age)
# Curly brackets could also include numbers to specify order or
# names which would be given to format's params or unpacked with **
#
# person = {'name': 'Eric', 'age': 74}
# "Hello, {name}. You're {age}.".format(name=person['name'], age=person['age'])
# "Hello, {name}. You're {age}.".format(**person)


# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="", level=logging.DEBUG,
                    format=LOG_FORMAT, filemode='w')


logger = logging.getLogger()  # Default param name: root
