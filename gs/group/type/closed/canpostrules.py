# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
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
from __future__ import absolute_import, unicode_literals
from gs.group.member.canpost.rules import BaseRule


class ClosedGroup(BaseRule):
    u'''No one can post to a closed group.'''
    weight = 1

    def check(self):
        if not self.s['checked']:
            self.s['canPost'] = False
            self.s['status'] = u'the group is closed'
            self.s['statusNum'] = self.weight
            self.s['checked'] = True

        assert self.s['checked']
        assert type(self.s['canPost']) == bool
        assert type(self.s['status']) == unicode
        assert type(self.s['statusNum']) == int
