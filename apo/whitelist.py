from MysqldbHelper import *
from django.http import HttpResponse
from zidian import *

def getresult(request):
    check_box_list = request.REQUEST.getlist("check_box_list")
    return check_box_list

def updatewhitelist(request):
    UID = request.GET['whitelistuid']
    whiteMember = request.GET.getlist('whiteMember')
    print whiteMember
    if len(whiteMember)>0:
        db = DB(**cgg_test_db)
        str = ','.join(whiteMember)
        update = "UPDATE white_list_member set screen_keys = '%s' where user_id = '%s'" % (str,UID)
        print update
        db.update(update)
        return HttpResponse({'succes'})
    return HttpResponse({'false'})


def selectwhitelist(request):
        UID = request.GET['whitelistuid']
        db = DB(**cgg_test_db)
        sql = "select * from white_list_member where user_id = '%s'" % (UID)
        fc = db.query(sql)
        list = []
        for row in fc:
            member = row[4]
            list.append("whitelist=%s" % \
                        (member))
        if len(list):
            return HttpResponse(list)
        else:
            return HttpResponse('result is null')