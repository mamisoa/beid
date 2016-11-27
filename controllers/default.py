# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def beid():
    import os
    from beid import scan_readers, read_infos, triggered_decorator
    from pprint import pprint
    from time import sleep
    try:
        os.remove(os.path.join(request.folder, 'static', 'phototemp.jpg'))
        statut = "deleted before update"
    except OSError:
        statut = "not deleted before update"
        pass
    r = scan_readers()[0]
    mod = 'hello'
    try:
        # sleep(2)
        infos = read_infos(r, read_photo=True)
        with open(os.path.join(request.folder, 'static', 'phototemp.jpg'),'wb') as f:
            f.write(infos['photo'])
            f.close()
    except Exception, e:
        mod = "Cannot read card"
        infos = "Cannot get photo"
        f= "photo not generated"
    return locals()

def form_beid():
    return locals()
