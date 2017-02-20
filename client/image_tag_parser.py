from HTMLParser import HTMLParser


class ImageTagParser(HTMLParser):
    image_tag_id = 'image-data'

    def __init__(self):
        HTMLParser.__init__(self)
        self.url = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img' and attrs.get('id') == self.image_tag_id:
            self.url = attrs.get('src')
