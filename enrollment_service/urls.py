from django.urls import path
from .views import EnrollmentByCourseView, EnrollmentView, StripeView,PayPalView,APICancelView,APISuccessView

urlpatterns = [
    path('', EnrollmentView.as_view(), name='enrol'),
    path('pay/', StripeView.as_view(), name='pay'),
    path('<str:course_id>/', EnrollmentByCourseView.as_view(),
         name='enrollment-by-course'),
    path('paypal/', PayPalView.as_view(), name='paypal'),
    path('paypal/cancel', APICancelView.as_view(), name='api_payment_cancel'),
    path('paypal/sucess/', APISuccessView.as_view(), name='api_payment_success'),
]


