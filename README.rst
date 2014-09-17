========================
``gs.group.type.closed``
========================
~~~~~~~~~~~~~~~~~~~~~~~~~
Support for closed groups
~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-07-10
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

A GroupServer_ group can be closed, so no one can post to it. There are a
couple of reasons for doing this:

#.  The group is no longer needed, but the members should still be able
    to retrieve their posts.
#.  The group is being *started*, and not everyone is a member yet.

See `Feature 449`_ For more information on the use-case.

This product supplies a `can post`_ rule to block posting to a closed
group, and a `digest notifier`_. Both are enabled by a `marker interface`_.

Can Post
========

The simple ``gs.group.type.closed.canpostrules.ClosedGroup`` class provides
a can-post rule that blocks all posting to the group [#canpost]_.

Digest Notifier
===============

Closed groups have their own digest notifier [#digest]_:
``gs.group.type.closed.digest.ClosedGroupDigestNotifier``. It does nothing
when ``ClosedGroupDigestNotifier.notify()`` is called, preventing the group
members from receiving any digest message.

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

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

..  _Feature 449: https://redmine.iopen.net/issues/449

.. [#canpost] See ``gs.group.member.canpost`` for more information:
   <https://source.iopen.net/groupserver/gs.group.member.canpost/>

.. [#digest] See ``gs.group.messages.topicsdigest`` for more information:
   <https://source.iopen.net/groupserver/gs.group.messages.topicsdigest/>


