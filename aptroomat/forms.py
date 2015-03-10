from django.contrib.gis import forms

class WorldBorderForm(forms.Form):

    world = forms.MultiPolygonField(
        widget = forms.OSMWidget(
            attrs = {
                'map_width': 1024,
                'map_height': 600,
            }
        )
    )
