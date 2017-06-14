from setuptools import setup

setup(
   name='time_formatter',
   version='0.1.1',
   py_modules=['format_milliseconds', 'time_between'],
   description='Formats the millisecond time into human readable',
   author='Ashley Morris',
   author_email='foomail@foo.com',
   install_requires=['click', 'moment'], #external packages as dependencies
   entry_points='''
       [console_scripts]
       format_milliseconds=format_milliseconds:format_millis
       time_between=time_between:between
   ''',
)