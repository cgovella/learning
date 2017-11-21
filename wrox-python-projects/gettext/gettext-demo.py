import gettext
import locale as loc 

# Set up the locale and translation mechanism
#############################
loc.setlocale(loc.LC_ALL,'')
filename = "res/messages_{}.mo".format(loc.getlocale()[0][0:2])

trans = gettext.GNUTranslations(open(filename,'rb'))
trans.install()

# Now the main program with gettext markers
#############################
print(_("Hello World"))


