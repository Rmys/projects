#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():

    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --enable-silent-rules \
                         --enable-introspection \
                         --with-libjasper \
                         --with-included-loaders=png")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.remove("/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders.cache")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
