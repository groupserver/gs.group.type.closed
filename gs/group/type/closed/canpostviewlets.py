# coding=utf-8
from zope.cachedescriptors.property import Lazy
from gs.group.member.canpost import RuleViewlet
from canpostrules import ClosedGroup as ClosedGroupRule

class ClosedGroup(RuleViewlet):
    weight = ClosedGroupRule.weight
    
    @Lazy
    def show(self):
        retval = self.canPost.statusNum == self.weight
        assert type(retval) == bool
        return retval

