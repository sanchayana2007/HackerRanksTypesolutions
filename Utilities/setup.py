from distutils.core import setup
import py2exe

setup(name='Distutils',
      version='1.0',
      description='Python Distribution Utilities',
      author='Saikat Saha',
      author_email='csaikat9@gmail.com',
      url='https://www.python.org',
     )

setup(console=["send_email_gui.py"])