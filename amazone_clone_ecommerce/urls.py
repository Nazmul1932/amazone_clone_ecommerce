from django.urls import path
from ecommerce_app import views, AdminViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', views.adminLogin, name="admin-login"),
    path('demo', views.demoPage),
    path('demoPage', views.demoPageTemplate),
    path('admin-login-process', views.adminLoginProcess, name='admin-login-process'),
    path('admin-logout-process', views.adminLogoutProcess, name='admin-logout-process'),

    # Admin
    path('admin-home', AdminViews.adminHome, name="admin-home"),

    path('category_list', AdminViews.CategoriesListView.as_view(), name="category_list"),
    path('category_create', AdminViews.CategoryCreateView.as_view(), name="category_create"),
    path('category_update/<slug:pk>', AdminViews.CategoriesUpdate.as_view(), name="category_update"),

    path('sub_category_list', AdminViews.SubCategoriesListView.as_view(), name="sub_category_list"),
    path('sub_category_create', AdminViews.SubCategoriesCreate.as_view(), name="sub_category_create"),
    path('sub_category_update/<slug:pk>', AdminViews.SubCategoriesUpdate.as_view(), name="sub_category_update"),

    path('merchant_create', AdminViews.MerchantUserCreateView.as_view(), name="merchant_create"),
    path('merchant_list', AdminViews.MerchantUserListView.as_view(),name="merchant_list"),
    path('merchant_update/<slug:pk>',AdminViews.MerchantUserUpdateView.as_view(),name="merchant_update"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
