# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, print_function, unicode_literals
from Products.GSGroup.groupInfo import GSGroupInfo


class StatusGroupInfo(GSGroupInfo):
    def __init__(self, userInfo, group):
        self.userInfo = userInfo
        super(StatusGroupInfo, self).__init__(group)
        self.show = False
