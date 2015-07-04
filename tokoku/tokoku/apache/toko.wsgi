import os
import sys
import django	#endik, May20, 2014
 
path = '/home/endik/Documents/WorkSpace/Python/endikApp/VENV/OPENSHIFT/toko/wsgi/tokoku/tokoku/apache'
if path not in sys.path:
    sys.path.insert(0, path)
  
sys.path.append('/home/endik/Documents/WorkSpace/Python/endikApp/VENV/OPENSHIFT/toko/wsgi/tokoku')
sys.path.append('/home/endik/Documents/WorkSpace/Python/endikApp/VENV/OPENSHIFT/toko/wsgi/tokoku/tokoku')

os.environ['DJANGO_SETTINGS_MODULE'] = 'tokoku.settings'

django.setup()		#endik, May20, 2014
  
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

