from rest_framework import serializers
from .models import SiteContent, ClassProgram, FAQCategory, FAQItem, Enquiry, Transformation

class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = '__all__'

class ClassProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassProgram
        fields = '__all__'

class FAQItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQItem
        fields = '__all__'

class FAQCategorySerializer(serializers.ModelSerializer):
    items = FAQItemSerializer(many=True, read_only=True)

    class Meta:
        model = FAQCategory
        fields = ['id', 'name', 'order', 'items']

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'

class TransformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformation
        fields = '__all__'
