from django.conf.urls import url, include

from .views import editTables, upload_tables, reservation, reserve_tables, table_status

urlpatterns = [

    # # url(r'^register/$', registration, name="registration"),
    # url(r'^register/post$', register_in_site_post, name = "post_registration"),
    # # url(r'^character/(?P<id>[\w-]+)/$', character, name="character"),
    # # url(r'^login/$', login_site, name="login"),
    # url(r'^logout/$', logout_in_site, name="logout"),
    # url(r'^login/post$', login_in_site, name="login_post"),
    # #  url(r'^registercharacter/$', registration_character, name="registration_character"),
    # # url(r'^registercharacter/post$', register_character_post, name = "register_character_post"),
    # url(r'^$', index, name = 'index'),
    # url(r'^Games/$', allgames, name = 'allgames'),
    url(r'^editTables/$', editTables, name = 'editTables'),
    url(r'^reservation/$', reservation, name = 'reservation'),
    # url(r'^Games/gomoku/$', gomoku, name = 'gomoku'),
    # url(r'^Games/lines/$', lines, name = 'lines'),
    # url(r'^Games/gomoku/plus_gomoku_game/$', plus_gomoku_game, name = 'plus_gomoku_game'),
    url(r'^editTables/upload_tables$', upload_tables, name = 'upload_tables'),
    url(r'^reservation/reserve_tables$', reserve_tables, name = 'reserve_tables'),
    url(r'^reservation/table_status/$', table_status, name = 'table_status'),

]