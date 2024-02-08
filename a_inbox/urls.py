from django.urls import path
from . views import inbox_view, search_users


# plot_view, add_plot_view, delete_plot_view, edit_plot_view, my_plots_view, like_plot, like_comment, search_plots_view, search_categories_view, campsite_plots_view, wild_plots_view, official_plots_view, search_countries_view, country_view, comment_sent, delete_comment, reply_sent, delete_reply, questions_view, report_plot_view, check_reports_view

urlpatterns = [
    path("", inbox_view, name="inbox"),
    path('c/<conversation_id>/', inbox_view, name='inbox'),
    path('search_users', search_users, name='inbox-search-user'),
]