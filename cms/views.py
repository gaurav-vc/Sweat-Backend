from rest_framework import viewsets, permissions
from .models import SiteContent, ClassProgram, FAQCategory, FAQItem, Enquiry, Transformation
from .serializers import SiteContentSerializer, ClassProgramSerializer, FAQCategorySerializer, FAQItemSerializer, EnquirySerializer, TransformationSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class EnquiryPermission(permissions.BasePermission):
    """
    Allow anyone to POST (create an enquiry).
    Only allow admins to GET, PUT, DELETE.
    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_staff

class SiteContentViewSet(viewsets.ModelViewSet):
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'key'

class ClassProgramViewSet(viewsets.ModelViewSet):
    queryset = ClassProgram.objects.all()
    serializer_class = ClassProgramSerializer
    permission_classes = [IsAdminOrReadOnly]

class FAQCategoryViewSet(viewsets.ModelViewSet):
    queryset = FAQCategory.objects.all().order_by('order')
    serializer_class = FAQCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class FAQItemViewSet(viewsets.ModelViewSet):
    queryset = FAQItem.objects.all().order_by('order')
    serializer_class = FAQItemSerializer
    permission_classes = [IsAdminOrReadOnly]

class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all().order_by('-created_at')
    serializer_class = EnquirySerializer
    permission_classes = [EnquiryPermission]

class TransformationViewSet(viewsets.ModelViewSet):
    queryset = Transformation.objects.all().order_by('order', '-created_at')
    serializer_class = TransformationSerializer
    permission_classes = [IsAdminOrReadOnly]
