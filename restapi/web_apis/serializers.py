# serialization is the process of converting a data structure or object into a format 
# that can be stored in a file or memory buffer, 
# or transmitted across a network connection link to be reconstructed 
# later in the same or another computer environment.
# in that case we'll conver our Model into a JSON object.

from rest_framework import serializers

from . import models

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Hero
        fields = ('id', 'real_name', 'hero_name')
        