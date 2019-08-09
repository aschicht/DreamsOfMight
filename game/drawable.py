import collections

RenderData = collections.namedtuple('RenderData', ['representation', 'foreground_light_color', 'foreground_dark_color', 'background_light_color', 'background_dark_color'])


class Drawable:

    def render(self, **kargs):
        pass