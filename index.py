import os
import sys

# Add the portfolio directory to the python path so 'myapp' can be found
sys.path.append(os.path.join(os.path.dirname(__file__), 'portfolio'))

from portfolio.wsgi import application

# This is the entry point for Vercel
app = application
