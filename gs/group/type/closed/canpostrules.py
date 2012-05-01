# coding=utf-8
from zope.cachedescriptors.property import Lazy
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

