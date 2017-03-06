from RequestKeywords import RequestsKeywords
from version import VERSION

class  RequestsLibrary(RequestsKeywords):


    """
    RequestsLibrary is a  http client keyword library that uses the requests module from kenneth Reitz

    examples:
    crate  session  google  http://www.google.com
    create session  github  http://github.com/api/v2/json
    ${resp}   get  google   /
    should be equal  as strings    ${resp.status_code}  200
    ${response}  get  github    /user/search/bulkan

    ${jsondata}   to Json  ${resp.content}
    dictionary should contain value  ${jsondata['users'][0]}   bulkan saven evciemn

    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'