/* Copyright (C) 2003 by Sandro Giessl
 * based on the nice CVS KDesktop KShadowEngine class. thanks!
 * looking forward to see KShadowEngine in kdefx somewhen btw.. :)
 * ------------------------------------------------------------------------
 * these are the original copyright notes:
 * This file is proposed to be part of the KDE libraries.
 * Copyright (C) 2003 Laur Ivan <laurivan@eircom.net>
 *
 * Many thanks to:
 *  - Bernardo Hung <deciare@gta.igs.net> for the enhanced shadow
 *    algorithm (currently used)
 *  - Tim Jansen <tim@tjansen.de> for the API updates and fixes.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License version 2 as published by the Free Software Foundation.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public License
 * along with this library; see the file COPYING.LIB.  If not, write to
 * the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */

#ifndef __FX_SHADOW
#define __FX_SHADOW

#include <qpixmap.h>
#include <qimage.h>
#include <qcolor.h>

class ShadowEngine
{
    public:
        ShadowEngine();
        ~ShadowEngine();
        void setThickness(int thickness) { thickness_ = thickness; }
        void setMultiplicationFactor(double factor) { multiplicationFactor_ = factor; }
        QImage makeShadow(const QPixmap& textPixmap, const QColor &bgColor);
    private:
        double decay(QImage& source, int x, int y);

        int thickness_;
        double multiplicationFactor_;
};

#endif
