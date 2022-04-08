# serialization is the process of converting a data structure or object into a format 
# that can be stored in a file or memory buffer, 
# or transmitted across a network connection link to be reconstructed 
# later in the same or another computer environment.
# in that case we'll conver our Model into a JSON object.

from rest_framework import serializers

from . import models

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    class Meta:
        model = models.Hero
        fields = '__all__'
        
class VillainsSerializer(serializers.HyperlinkedModelSerializer):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    class Meta:
        model = models.Villain
        fields = '__all__'
        
class ArchenemySerializer(serializers.HyperlinkedModelSerializer):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    id = serializers.IntegerField(read_only=True)
    hero = serializers.StringRelatedField()
    villain = serializers.StringRelatedField()
    
    class Meta:
        model = models.Archenemy
        fields = '__all__'
        