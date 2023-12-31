
from django.contrib import admin
from django.urls import path

from agroapp import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
    path('logincheck', views.logincheck, name='logincheck'),
    path('freg',views.freg,name='freg'),
    path('ureg',views.ureg,name='ureg'),
    path('addshp',views.addshp,name='addshp'),
    path('addstf',views.addstf,name='addstf'),
    path('hmpg',views.hmpg,name='hmpg'),
    path('sndrply/<int:id>',views.sndrply,name='sndrply'),
    path('sendedreply',views.sendedreply,name='sendedreply'),
    path('viewstf',views.viewstf,name='viewstf'),
    path('viewcmpnt',views.viewcmpnt,name='viewcmpnt'),
    path('viewshops',views.viewshops,name='viewshops'),
    path('viewusers',views.viewusers,name='viewusers'),
    path('aplschms', views.aplschms, name='aplschms'),
    path('hompg', views.hompg, name='hompg'),
    path('inrtprdct', views.inrtprdct, name='inrtprdct'),
    path('viwschms', views.viwschms, name='viwschms'),
    path('edit_subsidyprdct', views.edit_subsidyprdct, name='edit_subsidyprdct'),
    path('dltsprdct/<int:id>', views.dltsprdct, name='dltsprdct'),
    path('edit_sprdct/<int:id>', views.edit_sprdct, name='edit_sprdct'),
    # path('addsproduct', views.addsproduct, name='addsproduct'),
    path('dltprdct/<int:id>', views.dltprdct, name='dltprdct'),
    path('edit_fprdct', views.edit_fprdct, name='edit_fprdct'),
    path('edit_prdct/<int:id>', views.edit_prdct, name='edit_prdct'),
    path('manageproduct', views.manageproduct, name='manageproduct'),
    path('snddbtvwrply', views.snddbtvwrply, name='snddbtvwrply'),
    path('ordr_s_product', views.ordr_s_product, name='ordr_s_product'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('S_order_status/<int:id>', views.S_order_status, name='S_order_status'),
    path('addnewproduct', views.addnewproduct, name='addnewproduct'),
    path('snddbt', views.snddbt, name='snddbt'),
    path('srchsnddbtvwrply',views.srchsnddbtvwrply,name='srchsnddbtvwrply'),
    # path('viwfrtzr', views.viwfrtzr, name='viwfrtzr'),
    path('ordr_accept', views.ordr_accept, name='ordr_accept'),
    path('ordr_reject', views.ordr_reject, name='ordr_reject'),
    path('viwordr', views.viwordr, name='viwordr'),
    path('viwordr_details/<int:id>', views.viwordr_details, name='viwordr_details'),
    path('ordr_status', views.ordr_status, name='ordr_status'),
    # path('viwsbsdy', views.viwsbsdy, name='viwsbsdy'),
    path('addschms', views.addschms, name='addschms'),
    path('homepg', views.homepg, name='homepg'),
    path('rply', views.rply, name='rply'),
    # path('updtodrsts', views.updtodrsts, name='updtodrsts'),
    path('addschemes', views.addschemes, name='addschemes'),
    path('sendedreplytodoubt', views.sendedreplytodoubt, name='sendedreplytodoubt'),
    path('sendrply/<int:id>', views.sendrply, name='sendrply'),
    path('ordrrqst/<int:id>', views.ordrrqst, name='ordrrqst'),
    path('updtschms', views.updtschms, name='updtschms'),
    path('viwdbtrply', views.viwdbtrply, name='viwdbtrply'),
    path('add_manage_s_prdt', views.add_manage_s_prdt, name='add_manage_s_prdt'),
    path('add_s_prdt', views.add_s_prdt, name='add_s_prdt'),
    path('s_prdct_order', views.s_prdct_order, name='s_prdct_order'),
    path('ordrsprdctcode', views.ordrsprdctcode, name='ordrsprdctcode'),
    path('viwprdct/<int:id>', views.viwprdct, name='viwprdct'),
    path('view_s_product', views.view_s_product, name='view_s_product'),
    path('orderfromcart', views.orderfromcart, name='orderfromcart'),
    path('viwschmverfy', views.viwschmverfy, name='viwschmverfy'),
    path('viewfarmerinfo', views.viewfarmerinfo, name='viewfarmerinfo'),
    # path('viwsllgprdct', views.viwsllgprdct, name='viwsllgprdct'),
    path('edit_fertlzr/<int:id>', views.edit_fertlzr, name='edit_fertlzr'),
    path('edit_ftlzr', views.edit_ftlzr, name='edit_ftlzr'),
    path('dlt_frtzr/<int:id>', views.dlt_frtzr, name='dlt_frtzr'),
    path('addferlzr', views.addferlzr, name='addferlzr'),
    path('fertilizer_info', views.fertilizer_info, name='fertilizer_info'),
    path('search_ftlzr', views.search_ftlzr, name='search_ftlzr'),
    path('addsbsidy', views.addsbsidy, name='addsbsidy'),
    path('search_subsidy', views.search_subsidy, name='search_subsidy'),
    path('hmpage', views.hmpage, name='hmpage'),
    path('edit_subsidy/<int:id>', views.edit_subsidy, name='edit_subsidy'),
    path('dlt_subsidy/<int:id>', views.dlt_subsidy, name='dlt_subsidy'),
    path('acceptorder/<int:id>', views.acceptorder, name='acceptorder'),
    path('rejectorder/<int:id>', views.rejectorder, name='rejectorder'),
    path('add_subsidy', views.add_subsidy, name='add_subsidy'),
    path('edit_sbsdy', views.edit_sbsdy, name='edit_sbsdy'),
    path('sbsidy', views.sbsidy, name='sbsidy'),
    path('updtinfoferlzr', views.updtinfoferlzr, name='updtinfoferlzr'),
    path('addviwprdctratng', views.addviwprdctratng, name='addviwprdctratng'),
    path('addprdctratng', views.addprdctratng, name='addprdctratng'),
    path('addedstaff', views.addedstaff, name='addedstaff'),
    path('addedshop', views.addedshop, name='addedshop'),
    path('search_cmpnt', views.search_cmpnt, name='search_cmpnt'),
    # path('search_viewfertilizer', views.search_viewfertilizer, name='search_viewfertilizer'),
    path('farmer_reg', views.farmer_reg, name='farmer_reg'),
    path('user_reg', views.user_reg, name='user_reg'),

    path('hompage', views.hompage, name='hompage'),

    path('ordrdtls/<int:id>', views.ordrdtls, name='ordrdtls'),
    # path('ordrprdctCARD/<int:id>', views.ordrprdctCARD, name='ordrprdctCARD'),

    path('ordr_s_product/<int:id>', views.ordr_s_product, name='ordr_s_product'),
    path('deleteorder/<int:id>/<str:qty>', views.deleteorder, name='deleteorder'),
    path('S_order_history/<int:id>', views.S_order_history, name='S_order_history'),
    path('view_s_order', views.view_s_order, name='view_s_order'),
    path('cancel_s_order/<int:id>/<str:qty>', views.cancel_s_order, name='cancel_s_order'),
    path('view_s_cart', views.view_s_cart, name='view_s_cart'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),

    path('ordrprdct', views.ordrprdct, name='ordrprdct'),
    path('viewmycart', views.viewmycart, name='viewmycart'),
    path('uncheck', views.uncheck, name='uncheck'),
    path('S_orderstatus', views.S_orderstatus, name='S_orderstatus'),
    path('sndcmplntviwrply', views.sndcmplntviwrply, name='sndcmplntviwrply'),
    path('sndcmpnt', views.sndcmpnt, name='sndcmpnt'),
    path('snd_cmpnt', views.snd_cmpnt, name='snd_cmpnt'),
    path('snd_dobt', views.snd_dobt, name='snd_dobt'),
    path('viewhistory', views.viewhistory, name='viewhistory'),
    path('view_item_ordr_status/<int:id>', views.view_item_ordr_status, name='view_item_ordr_status'),
    path('viwrviw', views.viwrviw, name='viwrviw'),
    path('ordrprdctcode', views.ordrprdctcode, name='ordrprdctcode'),
    path('search_stf', views.search_stf, name='search_stf'),
    path('search_user', views.search_user, name='search_user'),
    path('dltshp/<int:id>', views.dltshp, name='dltshp'),
    path('dltstf/<int:id>', views.dltstf, name='dltstf'),
    path('orderfromcart/<int:id>', views.orderfromcart, name='orderfromcart'),
    path('edit_shop/<int:id>', views.edit_shop, name='edit_shop'),
    path('edit_shp', views.edit_shp, name='edit_shp'),
    path('edit_staff/<int:id>', views.edit_staff, name='edit_staff'),
    path('edit_stf', views.edit_stf, name='edit_stf'),
    path('search_shp', views.search_shp, name='search_shp'),
    path('srchfarmerinfo', views.srchfarmerinfo, name='srchfarmerinfo'),
    path('srchordr_products', views.srchordr_products, name='srchordr_products'),
    path('srchsbsdy_products', views.srchsbsdy_products, name='srchsbsdy_products'),
    path('addsubsidy_product', views.addsubsidy_product, name='addsubsidy_product'),
    path('srchsbsdy_prodcts', views.srchsbsdy_prodcts, name='srchsbsdy_prodcts'),
    path('ordr_subsdy_product', views.ordr_subsdy_product, name='ordr_subsdy_product'),
    path('sorderfromcart/<int:id>', views.sorderfromcart, name='sorderfromcart'),
    path('s_prdct_order1/<int:id>',views.s_prdct_order1,name='s_prdct_order1'),
    path('accept_s_order/<int:id>',views.accept_s_order,name='accept_s_order'),
    path('reject_s_order/<int:id>',views.reject_s_order,name='reject_s_order'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('add_schms',views.add_schms,name='add_schms'),
    path('edit_schemes/<int:id>',views.edit_schemes,name='edit_schemes'),
    path('viwdbtrplysearch',views.viwdbtrplysearch,name='viwdbtrplysearch'),
    path('dlt_schms/<int:id>',views.dlt_schms,name='dlt_schms'),
    path('edit_schemescode',views.edit_schemescode,name='edit_schemescode'),
    path('logout',views.logout,name='logout'),


]
