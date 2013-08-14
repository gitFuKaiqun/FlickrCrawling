"""

Author: Kaiqun
Apr 23, 2013

"""

import json
import httplib
import hashlib

secret = '78e69e4401035bbc'
api_sig = ''

CommandDict = {}
CommandDict.update({'api_key': '6e2f0e33f562523efdffe597d931a0d7'})
CommandDict.update({'auth_token': '72157632762484786-2e4303a889eb2d15'})
CommandDict.update({'method': 'flickr.photos.getRecent'})
CommandDict.update({'format': 'json'})
# CommandDict.update({'photo_id': '841267'})

def Flickr():
    conn = httplib.HTTPConnection("api.flickr.com")
    Result = stringOperator(CommandDict)
    conn.request("GET", "/services/rest/?" + Result)
    OutPutRslt = open('FlickrOut.txt', 'w')
    Response = conn.getresponse().read()
    # print Response[14:-1]
    JsonObjResponse = json.loads(Response[14:-1])

    # http://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg

    for one in JsonObjResponse['photos']['photo']:
        Farm_id = str(one['farm'])
        Server_id = one['server']
        Id = one['id']
        Secret = one['secret']
    #    OutPutRslt.write('http://farm' + Farm_id + '.staticflickr.com/' + Server_id + '/' + Id + '_' + Secret + '.jpg' + '----------> ' + one['title'].encode("GBK", 'ignore') + '\n')
        print '<img src="http://farm' + Farm_id + '.staticflickr.com/' + Server_id + '/' + Id + '_' + Secret + '.jpg"/>' + '----------> ' + one['title'].encode("GBK", 'ignore') + '<br>'

def stringOperator(cmdDic):
    cmdList = []
    for key in cmdDic.keys():
        cmdList.append("%s%s" % (key, cmdDic[key]))
    cmdList.sort()
    FinalCMD = secret
    for one in cmdList:
        FinalCMD = FinalCMD + one
    Encypher = hashlib.md5()
    Encypher.update(FinalCMD)
    api_sig = Encypher.hexdigest()
    CommandDict.update({'api_sig': api_sig})
    SepFinal = [key + '=' + cmdDic[key] for key in cmdDic.keys()]
    linkStr = '&'
    return linkStr.join(SepFinal)

if  __name__ == '__main__':
    Flickr()
