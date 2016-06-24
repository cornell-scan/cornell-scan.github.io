# [SCAN seminar][scan] web page

## General design

For content management, I am using [Jekyll][jekyll] a plain-text
static site generator.  The chief goal of using Jekyll is to
separate the content from presentation, making it simpler to apply
general stylistic changes in the future.

The main repository for the sources is on GitHub, but updates to
the GitHub repository automatically trigger a remote script to
rebuild the web pages and push them to the server.

## Talk information

Talk posts are stored in the `_posts` subdirectory, and are named according
to the usual Jekyll convention (`YYYY-MM-DD-topic.extension`).
The [YAML][yaml] header should include title and speaker information:

    ---
    title: A very important talk
    speaker:
      name: David Bindel
      affil: CS, Cornell
      url: http://www.cs.cornell.edu/~bindel
    ---

The abstract may either be written in the text below the header or
(if the speaker insists) it may be indicated in a separate
`abstract_url` field in the header information.

To indicate that there is a break, there should be a talk post
with the header information field `break`, e.g.

    ---
    break: Spring Break
    ---

## Semester schedule

Talk schedules are automatically populated from the `_posts` subdirectory
based on the date.  Talks between January and June are assumed to be
associated with the spring schedule; talks from August to December are in
the fall schedule.

The schedule pages have names of the form (for example) `index-s17.md`,
and the header information

    ---
    layout: schedule
    semester: Spring
    year: 2017
    ---

where the semester should be `Spring` or `Fall`.  The text that follows
introduces the seminar and gives the current meeting logistics.  Add the
header field `nav: current` to indicate that this is the schedule for the
current semester.  The current semester's schedule page should also be
used as `index.md`.

## Style

The current site style is built on [Bootstrap][bootstrap], a small set of
responsive CSS modules from Yahoo.  In this setting, "responsive"
means that the site should adapt gracefully to different screen sizes
and window sizes.  The new design hues closely to the Bootstrap example
pages.

[scan]: http://cse.cornell.edu/scan
[jekyll]: http://jekyllrb.com/
[yaml]: [yaml]: http://jekyllrb.com/docs/frontmatter/
[bootstrap]: http://getbootstrap.com/
