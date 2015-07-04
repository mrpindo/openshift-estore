#!/usr/bin/env python
#This housekeeping process is replacement of the one prepared within root views, cause there may be
#a security breach issue if it run with views.
#This is suppose to be run from command python shell!
# python manage.py shell
# import housekeep
# housekeep.run()

import os
from shop.models import Product

def run(verbose=True):
    #init list
    mainimage = []
    thumbimage = []

    #walk main directories do the work
    for filenames in os.walk('../../wsgi/static/media/products/main/'):
      for filename in filenames[2]:
        filenpath = 'products/main/'+ str(filename)
        if Product.objects.filter(imgfile=filenpath).first():
          pass
        else:
          mainimage.append(filename)

    for image in mainimage:
      filenpath = '../../wsgi/static/media/products/main/'+ str(image)
      os.remove(filenpath)


    #walk thumbnails directories do the work
    for thumbnames in os.walk('../../wsgi/static/media/products/thumbnails/'):
      for thumbname in thumbnames[2]:
        thumbnpath = 'products/thumbnails/'+ str(thumbname)
        if Product.objects.filter(imgthumb=thumbnpath).first():
          pass
        else:
          thumbimage.append(thumbname)

    for timage in thumbimage:
      thumbnpath = '../../wsgi/static/media/products/thumbnails/'+ str(timage)
      os.remove(thumbnpath)

    print ('Done, I think. **imgfile been deleted:'+ str(mainimage) +'. **imgthumb been deleted:'+ str(thumbimage) )

