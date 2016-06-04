######################
I Wrote A Test Article
######################

:date: 2016-06-01
:modified: 2016-06-03
:status: published
:tags: Test, Fluff
:summary:
    This is just an article I created to test things. It's really just a bunch
    or reST bits to learn how that works, and to populate an article with
    various HTML for styling purposes.

This is a paragraph in reST. It consists of several lines, which are all aligned
to the same column. If there is one thing to remember about paragraphs its that
they need to line up on their left side.

Oh look, a new paragraph! Let's try some inline business. This should become
*italic*, and **bold**, and ``literal``. Now lets try some interpreted text
roles. This should be :emphasis:`emphesized`, this :literal:`literal`, this
:code:`code()`, some math: :math:`A_\text{c} = (\pi/4) d^2`, this
:strong:`strong`, :sub:`subscript` and :sup:`superscript`. Right then, on to
lists and quote-like blocks.

* A bulleted list
* With a couple items

    #. And and auto numbered
    #. nested
    #. list

* A final list item

Definition List (what this thing is, with the *term* being on one line)
    Here is the definition.

    Consisting of any number of paragraphs.


Lets have a look at a quoted paragraph:

    It is simply indented from the previous paragraph. That is all.

| Oh, and line breaks
| How they're nice
| Just use a pipe
| There's no hype

Field lists, option lists, and literal blocks also look useful. BTW, here is a
literal block::

    It is just indented like and paragraph. Things like *this* are not
    emphesised.

***************
Linkages Abound
***************

.. _linkages paragraph:
.. _other link:

You know it. Time to open a new chapter and link to things. Interesting to note
the 'part' and 'chapter' titles both use level 2 header, whether or not they're
overlined. Anyhow, these things are really called *explicit markups*.

Footnotes
=========

Blah, bleh whatevs, then all of a sudden, a footnote [1]_. Also, you can totals
auto this stuff [#]_, oh you know [#]_.

These footnotes are labeled [#silly]_ automatically [#label]_. Hmmm, looks like
footnotes create a table in HTML.

.. [1] Note there's no colon after the footnote's explicit markup start.
.. [#] Auto footnote
.. [#] And another
.. [#silly] Silly lable.
.. [#label] Label that's silly.

Citations
=========

Citations are much like labeled footnotes, but without the hash, and the lable
is actually [visible]_ inline. You can also then plainly link to the visible_
citation.

.. [visible] A visible citation. Way to go.

Hyperlink Targets
=================

Define a link completely inline to
`patternspandemic <http://patternspandemic.github.io>`_. Or separate the
`link lable`_ from the target. Oh yeah, you can totally link to the
`linkages paragraph`_ above. Did you know that titling such as `Footnotes`_ are
usable targets as well?

.. _link lable: http://github.com

***********************
The Chapter on Sections
***********************

H2 - So let's see what we've got here. The title above is considered a chapter.

Appeasing Section
=================

h3 - You already saw above that sections use =.

Sub-Sections
------------

H4 - Use the - character.

Sub-Sub-Sections
^^^^^^^^^^^^^^^^

H5 - The ^ character.

Paragraphs
""""""""""

H6 - Eh, I guess a way to section out a paragraph more clearly? Moving along.

******************************
Anyway, Things I've Yet To Try
******************************

- reST Directives
- reST Substitutions (like inline directives)
- reST Comments
