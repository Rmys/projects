#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2008 Gürer Özen
# This code is licensed under the GNU General Public License.
#

"""
Bu, kamera görüntüsünde bir yüz görünmediğinde ekranı kitleyen
bir panel uygulamasıdır. Aynı zamanda birden fazla yüz göründüğünde
ilk desktop'a geçer.
"""

import os
import sys
import time

# Temel OpenCV fonksiyonları
from opencv.cv import *
# OpenCV GUI ve Camera API fonksiyonları
from opencv.highgui import *

from qt import *
from kdecore import *
from kdeui import *

I18N_NOOP = lambda x: x


class FaceDetector:
    # Haar yöntemiyle tanıma için kullanılacak özellik dosyası.
    # Tanınacak nesnenin bölgeleri arasındaki kontrastları tanımlar.
    #
    # Burada önden görünüş yüz için çeşitli örneklerden hesaplanarak oluşturulmuş
    # veri dosyasını kullanıyoruz, opencv ile gelen dosyalardan mesela
    # haarcascade_profileface.xml ile yandan profil yüz tanıma yapabilirsiniz.
    #
    # Cascade (basamak, şelale) deniyor, çünkü basit özelliklerden başlayıp
    # görüntü ile uyuştuğu sürece daha yukarı aşama özellikleri test eden
    # bir sınıflama yöntemi kullanılıyor.
    cascade_path = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
    # Kamera görüntüsünü küçültme oranı, daha büyük = daha hızlı ve daha az başarılı tanıma
    scale = 1.4
    
    def __init__(self, cam_no=0):
        self.storage = cvCreateMemStorage(0)
        # Bu fonksiyon obsolete ama cvLoad'un değerini HaarClassifierCascade'e cast
        # edemiyoruz diye mecburen kullanıyoruz
        self.cascade = cvLoadHaarClassifierCascade(self.cascade_path, cvSize(1, 1))
        self.capture = cvCreateCameraCapture(cam_no)
    
    def detect(self):
        # Görüntüden bir kare al
        frame = cvQueryFrame(self.capture)
        copy = cvCreateImage(cvSize(frame.width, frame.height), IPL_DEPTH_8U, frame.nChannels)
        if (frame.origin == IPL_ORIGIN_TL):
            cvCopy(frame, copy)
        else:
            cvFlip(frame, copy, 0)
        
        # Gri tonlamalı ve küçültülmüş hale getir
        small_img = cvCreateImage(cvSize(cvRound(copy.width / self.scale), cvRound(copy.height / self.scale)), 8, 1)
        gray = cvCreateImage(cvSize(copy.width, copy.height), 8, 1)
        cvCvtColor(copy, gray, CV_BGR2GRAY)
        cvResize(gray, small_img, CV_INTER_LINEAR)
        cvEqualizeHist(small_img, small_img)
        
        cvClearMemStorage(self.storage)
        
        # Yüz tanıma işlemi
        t = cvGetTickCount()
        haar_scale = 1.2
        min_neighbors = 2
        faces = cvHaarDetectObjects(
            small_img,
            self.cascade,
            self.storage,
            haar_scale,
            min_neighbors,
            CV_HAAR_DO_CANNY_PRUNING,
            # Minimum yüz boyutu
            cvSize(30, 30)
        )
        t = cvGetTickCount() - t
        #print "detection time = %gms" % (t/(cvGetTickFrequency()*1000.))
        return faces
    
    def count(self):
        faces = self.detect()
        # Tanınan yüz sayısını döndür
        if faces:
            # Malesef opencv binding len(faces) işlemini desteklemiyor
            count = 0
            for face in faces:
                count += 1
            return count
        else:
            return 0


class FaceThread(QThread):
    # Yüz tanıma işlemi için süreç
    def run(self):
        FACE, NOFACE, GOING, LOCK = range(4)
        faced = FaceDetector()
        last_state = None
        state = FACE
        boss = 0
        while True:
            time.sleep(0.2)
            count = faced.count()
            if count == 0:
                boss = 0
                if state == FACE:
                    last_state = time.time()
                    state = NOFACE
                diff = time.time() - last_state
                if state == NOFACE and diff > 0.4:
                    state = GOING
                    event = QCustomEvent(QEvent.User + 1)
                    QApplication.postEvent(self.poster, event)
                if state == GOING and diff > 3:
                    state = LOCK
                    event = QCustomEvent(QEvent.User + 3)
                    QApplication.postEvent(self.poster, event)
            else:
                if count > 1:
                    boss += 1
                    if boss > 3:
                        event = QCustomEvent(QEvent.User + 4)
                        QApplication.postEvent(self.poster, event)
                else:
                    boss = 0
                if state != FACE:
                    state = FACE
                    event = QCustomEvent(QEvent.User + 2)
                    QApplication.postEvent(self.poster, event)


class Signaller(QObject):
    def customEvent(self, qEvent):
        etype = qEvent.type()
        if etype == QEvent.User + 1:
            self.emit(PYSIGNAL("goingToLock"), (True,))
        elif etype == QEvent.User + 2:
            self.emit(PYSIGNAL("goingToLock"), (False,))
        elif etype == QEvent.User + 3:
            self.emit(PYSIGNAL("lockDesktop"), ())
        elif etype == QEvent.User + 4:
            self.emit(PYSIGNAL("bossKey"), ())


class Applet(KSystemTray):
    def __init__(self, app):
        KSystemTray.__init__(self)
        # Panel ikonlarımızı hazırlayalım
        self.pix1 = self.loadIcon("user")
        self.pix0 = KIconEffect().apply(self.pix1, KIconEffect.ToGray, 1, QColor(), False)
        self.setPixmap(self.pix1)
        self.connect(self, SIGNAL("quitSelected()"), self.slotQuit)
        self.app = app
        self.facet = FaceThread()
        # Malesef PyQt3 te QThread sınıfı QObject'ten türemiyor ve thread-safe
        # olarak sinyal emit edemiyor. Applet için KDE kullandığımızdan PyQt4 de
        # bir seçenek değil.
        # Sinyal verebilmek için QThread içinden post edilen eventlere göre sinyal
        # emit eden bu ara nesneyi kullanıyoruz.
        self.facet.poster = Signaller()
        self.connect(self.facet.poster, PYSIGNAL("lockDesktop"), self.slotLockDesktop)
        self.connect(self.facet.poster, PYSIGNAL("goingToLock"), self.slotGoingToLock)
        self.connect(self.facet.poster, PYSIGNAL("bossKey"), self.slotBoss)
        # Thread yüz tanıma işine başlıyor
        self.facet.start()
    
    def slotQuit(self):
        self.app.quit()
    
    def slotGoingToLock(self, is_going):
        if is_going:
            self.setPixmap(self.pix0)
        else:
            self.setPixmap(self.pix1)
    
    def slotLockDesktop(self):
        # API den de yapabilirdik bu çağrıları ama böyle kolay oldu :)
        os.system("dcop kdesktop KScreensaverIface lock")
    
    def slotBoss(self):
        os.system("dcop kwin KWinInterface setCurrentDesktop 1")


def main(args):
    about = KAboutData(
        "facelock-applet",
        I18N_NOOP("Facelock Applet"),
        "0.1",
        None,
        KAboutData.License_GPL,
        "(C) 2008 Gürer Özen",
        None,
        None,
        "gurer@pardus.org.tr"
    )
    KCmdLineArgs.init(args, about)
    KUniqueApplication.addCmdLineOptions()
    app = KUniqueApplication(True, True, True)
    
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    
    applet = Applet(app)
    applet.show()
    app.exec_loop()


if __name__ == "__main__":
    main(sys.argv)
