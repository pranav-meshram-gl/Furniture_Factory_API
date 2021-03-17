from rest_framework.serializers import ModelSerializer, ValidationError
from factory_app.models import TableLeg, Table, Leg, Feet

class FeetSerializer(ModelSerializer):
    class Meta:
        model = Feet
        fields = '__all__'

    def validate(self, data):
        radius = data.get('radius')
        width = data.get('width')
        length = data.get('length')

        """ Validations for foot: """
        #If radius is given it should not have length or width.
        if radius and (width or length):
            raise ValidationError("A foot with a radius must not have length or width. Please try again.")

        #If length is given then width must also be given.
        if length and not width:
            raise ValidationError("A foot with a length must also have a width. Please try again.")

        #If width is given then length must also be given.
        if width and not length:
            raise ValidationError("A foot with a width must also have a length. Please try again.")

        return data



class LegSerializer(ModelSerializer):
    class Meta:
        model = Leg
        fields = '__all__'



class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'



class TableLegSerializer(ModelSerializer):
    class Meta:
        model = TableLeg
        fields = '__all__'