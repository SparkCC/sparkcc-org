from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def get_header(value):
    """
    Gets the header for a piece of content by:

    #. Attempting to split the content on variations of the `<!--more-->` tag.
    #. Attempting to split the content on the first paragraph similar to the
        method in :func:`mezzanine.models.MetaData.description_from_content`.
    #. Giving up and returning the entire piece of content
    """

    more_tags = [
        '<!--more-->',
        '<!--More-->',
        '<!--MORE-->',
    ]

    for each in more_tags:
        more_split = value.split(each)
        if len(more_split) > 1:
            return more_split[0]

    ends = [
        "</p>",
        "<br />",
        "<br/>",
        "<br>",
        "</ul>",
    ]

    for each in ends:
        end_split = value.split(each)
        if len(end_split) > 1:
            return end_split[0] + each

    return value
