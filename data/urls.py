from django.conf.urls import url

from .views import ( display_file, download_file, tree_visualization,
                     export_to_itol, display_msa, display_raw, display_params,
                     get_example, add_file_to_session, remove_file_from_session)

urlpatterns = [
    #url(r'^upload/$', ImportPastedContentView.as_view(), name='upload'),

    url(r'^display/(?P<file_id>[\w-]+)$', display_file, name="display_file"),
    url(r'^displayraw/(?P<file_id>[\w-]+)$', display_raw, name="display_raw"),
    url(r'^displaytree/(?P<file_id>[\w-]+)$', tree_visualization, name="display_tree"),
    url(r'^displaymsa/(?P<file_id>[\w-]+)$', display_msa, name="display_msa"),
    url(r'^example/$', get_example, name="get_example"),
    # url(r'^example/(?P<ext_file>[\w-]+)', get_example , name="get_example"),
    url(r'^params/(?P<file_id>[\w-]+)$', display_params, name="display_params"),
    url(r'^download/(?P<file_id>[\w-]+)$', download_file, name="download_file"),
    url(r'^export_to_itol/(?P<file_id>[\w-]+)$', export_to_itol, name="export_to_itol"),
    url(r'^add/(?P<file_id>[\w-]+)$', add_file_to_session, name="add_file_to_session"),
    url(r'^remove/(?P<file_id>[\w-]+)$', remove_file_from_session, name="remove_file_from_session"),

]
