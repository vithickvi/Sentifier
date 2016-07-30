from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from senti import views
from django.conf.urls import include
admin.autodiscover()

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^results/', TemplateView.as_view(template_name='results.html')),
    url(r'^results1/', TemplateView.as_view(template_name='results1.html')),
    # url(r'^control/', TemplateView.as_view(template_name='control.html')),
    url(r'^control/', views.control),
	url(r'^fetchresults/',views.process),
	url(r'^fetchresults1/',views.process1),
	url(r'^fetchtrends/',views.trends),
	url(r'^refresh/',views.refreshtrends),
	url(r'^retrive/',views.retrivetweets),

]
