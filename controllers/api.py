def rows2json (tablename,rows):
    import datetime
    import json
    def date_handler(obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime(str(T('%Y-%m-%d %T'))) #(str(T('%d/%m/%Y %T')))
        elif isinstance(obj, datetime.date):
            return obj.strftime(str(T('%Y-%m-%d'))) # (str(T('%d/%m/%Y')))
        else:
            return False
    rows = rows.as_list()
    concat = '{ "'+tablename+'": ['
    for row in rows:
        concat = concat + json.dumps(row, default=date_handler)+","
    concat = concat.strip(',')
    concat = concat + ']}'
    return concat

def valid_date(datestring):
    import datetime
    try:
        datetime.datetime.strptime(datestring, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def beid():
    import json
    from base64 import b64encode
    from beid import scan_readers, read_infos, triggered_decorator
    from time import sleep
    response.view= 'generic.json'
    r = scan_readers()[0]
    infos_json = {}
    try:
        # sleep(2)
        infos = read_infos(r, read_photo=True)
        infos['photo'] =  b64encode(infos['photo'])
        infos_json = json.dumps(infos)
    except Exception, e:
        infos = { 'results': 'cannot read card', 'erreur': e}
        # infos_json = {}
    return infos_json
