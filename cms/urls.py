from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteContentViewSet, ClassProgramViewSet, FAQCategoryViewSet, FAQItemViewSet, EnquiryViewSet, TransformationViewSet

router = DefaultRouter()
router.register(r'site-content', SiteContentViewSet)
router.register(r'class-programs', ClassProgramViewSet)
router.register(r'faq-categories', FAQCategoryViewSet)
router.register(r'faq-items', FAQItemViewSet)
router.register(r'enquiries', EnquiryViewSet)
router.register(r'transformations', TransformationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
