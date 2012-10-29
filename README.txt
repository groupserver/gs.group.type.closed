Introduction
============

A GroupServer_ group can be closed, so no one can post to it. There are a
couple of reasons for doing this:

#.  The group is no longer needed, but the members should still be able
    to retrieve their posts.
#.  The group is being *started*, and not everyone is a member yet.

See `Feature 449`_ For more information on the use-case.

This product supplies a `can post`_ rule to block posting to a closed
group. The rule is enabled by a `marker interface`_.

Can Post
========

The simple ``gs.group.type.closed.canpostrules.ClosedGroup`` class provides
a can-post rule that blocks all posting to the group [#canpost]_.

Marker Interface
================

A group is closed by changing the marker interface for the group folder to
``IGSClosedGroup``. This marker interface has the following inheritance
tree::

  gs.group.base.interfaces.IGSGroupMarker
      △
      │
  gs.group.type.closed.interfaces.IGSClosedGroup


Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.type.closed
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. [#canpost] See ``gs.group.member.canpost`` for more information:
   <https://source.iopen.net/groupserver/gs.group.member.canpost/>

.. _GroupServer: http://groupserver.org
..  _Feature 449: https://redmine.iopen.net/issues/449

