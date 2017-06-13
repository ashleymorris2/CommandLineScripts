from setuptools import setup

setup(
   name='time_formatter',
   version='0.1.0',
   py_modules=['time_formatter'],
   description='Formats the millisecond time into human readable',
   author='Ashley Morris',
   author_email='foomail@foo.com',
   install_requires=['click', 'moment'], #external packages as dependencies
   entry_points='''
       [console_scripts]
       format_millis=time_formatter:format_time
   ''',
)