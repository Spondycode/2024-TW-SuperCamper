from django.urls import path
from . import views
from .views import *

# plot_view, add_plot_view, delete_plot_view, edit_plot_view, my_plots_view, like_plot, like_comment, search_plots_view, search_categories_view, campsite_plots_view, wild_plots_view, official_plots_view, search_countries_view, country_view, comment_sent, delete_comment, reply_sent, delete_reply, questions_view, report_plot_view, check_reports_view

urlpatterns = [
    path("", views.home, name="home"),
    path("show_plot/<plot_id>/", plot_view, name="show-plot"),
    path("add_plot/", add_plot_view, name="add-plot"),
    path("delete_plot/<pk>/", delete_plot_view, name="delete-plot"),
    path("edit_plot/<pk>/", edit_plot_view, name="edit-plot"),
    path("my_plots/", my_plots_view, name="my-plots"),
    path("myplots/", my_plots_view, name="my-plots"),
    path("plot/like/<pk>/", like_plot, name="like-plot"),
    path("comment/like/<pk>/", like_comment, name="like-comment"),
    path("search_plots/", search_plots_view, name="search-plots"),
    path("search_categories/", search_categories_view, name="search-categories"),
    path("campsite_plots/", campsite_plots_view, name="campsite-plots"),
    path("wild_plots/", wild_plots_view, name="wild-plots"),
    path("official_plots/", official_plots_view, name="official-plots"),
    path("search_countries/", search_countries_view, name="search-countries"),
    path("country/<plot_country>/", country_view, name="country"),
    path("commentsent/<pk>/", comment_sent, name="comment-sent"),
    path("delete_comment/<pk>/", delete_comment, name="delete-comment"),
    path("replysent/<pk>/", reply_sent, name="reply-sent"),
    path("delete_reply/<pk>/", delete_reply, name="delete-reply"),
    path("questions/", questions_view, name="questions"),
    path("report_plot/<pk>/", report_plot_view, name="report-plot"),
    path("check_reports/", check_reports_view, name="check-reports"),
    path("about/", about_view, name="about"),
    
]