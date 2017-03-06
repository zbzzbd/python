#-*-coding:utf8  -*-
import httplib
import json
import sys
from urllib  import urlencode

import requests

import logging
from requests.packages.urllib3.util  import  Retry
import robot
from  robot.api  import logger
from  robot.libraries.BuiltIn import BuiltIn


try:
    from requests_ntlm import HttpNtlmAuth
except ImportError:
    pass


class  WritableObject:
    '''
    HTTP  stream  handler
    '''
    def __init__(self):
        self.content = []

    def write(self,string):
        self.content.append(string)


class RequestsKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self):
        self._cache = robot.utils.ConnectionCache('No session created')
        self.builtin = BuiltIn()
        self.debug = 0

    def _create_session(self,
                        alias,
                        url,
                        headers,
                        cookies,
                        auth,
                        timeout,
                        max_retries,
                        backoff_factor,
                        proxies,
                        verify,
                        debug,
                        disable_warnings):
        """
        'alias' robot framework alias to identify the session
        'url'    base url of the server
         'headers'  dictionary of default headers
         'timeout'   connection timeout
         'max_retries' the maxinium number of retries each connextion should attempt

        """
        self.builtin.log("Createing session:%s" %alias,'DEBUG')
        s = session = requests.Session()

        s.headers.update(headers)
        s.auth = auth if auth else s.auth
        s.proxies = proxies if proxies else s.proxies

        max_retries = self.builtin.convert_to_integer(max_retries)

        if max_retries >0:
            http= requests.adapters.HTTPAdapter(max_retries= Retry(total=max_retries,backoff_factor=backoff_factor))
            https = requests.adapters.HTTPAdapter(max_retries=Retry(total=max_retries,backoff_factor=backoff_factor))

            if disable_warnings:
                logging.basicConfig()
                logging.getLogger().setLevel(logging.ERROR)
                requests_log = logging.getLogger("requests")
                requests_log.setLevel(logging.ERROR)
                requests_log.propagate = True

            s.mount('http://',http)
            s.mount('https://',https)


        if isinstance(verify,bool):
            s.verify= verify
        elif isinstance(verify,unicode) or isinstance(verify,str):
            if verify.lower() == 'true' or verify.lower() =='false':
                verify= self.builtin.convert_to_boolean(verify)
        else:
            s.verify = verify
        self.timeout = float(timeout) if  timeout is not None else None
        self.cookies = cookies
        self.verify = verify

        s.url= url

        if debug >=1:
            self.debug = int(debug)
            httplib.HTTPConnection.debuglevel = self.debug
        self._cache.register(session,alias= alias)
        return session

    def create_session(self,alias,url,headers={},cookies=None,
                       auth=None,timeout=None,proxies=None,
                       verify=False,debug=0,max_retries=3,backoff_factor=0.10,disable_warnings=0):
        """
        create session: create http session to a server
        'url' base url of the server
        'alias' robot framework alias to identify the session
        'headers' dictionary of default headers
        'auth' list of username & password for http basic auth
        'timeout' connection timeout
        'proxies' dictionary that contains proxy urls for http and https communication
        'verify' Whether the ssl cert will be verified .A CA_BUNDLE path can also be provided. Defaults to False.
        'debug' enable http verbosity option more information
                https://docs.python.org/2/library/heeplib.html
        'max_retries' The maximum number of retries each connection should attempt.
        'backoff_factor' the pause betewwn for each retry
        'disable_warnings' diable requests warning useful when you have large number of testcase

        """
        auth = requests.auth.HTTPBasicAuth(*auth) if auth else None
        logger.info('Creating Session using:alias=%s,url=%s,header=%s, \
                    cookies=%s,auth=%s,timeout=%s,prxies=%s,verify=%s, \
                    debug=%s' %(alias,url,headers,cookies,auth,timeout,proxies,verify,debug))
        return  self._create_session(
            alias,
            url,
            headers,
            cookies,
            auth,
            timeout,
            max_retries,
            backoff_factor,
            proxies,
            verify,
            debug,
            disable_warnings)

    def create_ntlm_session(self,
                            alias,
                            url,
                            auth,
                            headers={},
                            cookies=None,
                            timeout=None,
                            proxies = None,
                            verify = False,
                            debug=0,
                            max_retries =3,
                            backoff_factor =1.10,
                            disable_warnings =0,
                            ):
        """
        create session :create http session to a server
        'url': base url of the server
        'alias' Robotframework alias to identify the session
         'headers' dictionary of default headers
        'auth' ['DOMAIN','username','password'] fpr MT;, aitjemtocatopm
        'timeout' connection timeout
        'proxies' dictionary that contains proxy urls for http and https communication
        'verify' wwhether the ssl cert will be verified ,A CA_BUNDLE path also be provided defaults to False
        'debug'
        'max_retries' The maxmum number of retries each connextion should attempt
        'backoff_factor' the pause between ofr each retry

        """
        if not HttpNtlmAuth:
            raise AssertionError('Requests NTLM moudles not loaded')
        elif len(auth) !=3:
            raise AssertionError('Incorrect number of authentication arguments'
                                 ' - expected 3,got {}'.format(len(auth))
                                 )
        else:
            ntlm_auth = HttpNtlmAuth('{}\\{}'.format(auth[0],auth[1]),auth[2])

            logger.info('Creating NTLM Session using: alias=%s,url=%s,\
                        headers=%s,cookies=%s,ntlm_auth=%s,timeout=%s \
                        proxies=%s,verify=%s,debug=%s'
                        % (alias,url,headers,cookies,ntlm_auth,
                           timeout,proxies,verify,debug))
            return  self._create_session(
                alias,
                url,
                headers,
                cookies,
                ntlm_auth,
                timeout,
                max_retries,
                backoff_factor,
                proxies,
                verify,
                debug,
                disable_warnings
                )
    def create_digtest_session(self,alias,url,auth,headers={},cookies=None,
                               timeout=None,proxies=None,verify=False,
                               debug=0,max_retries=3,backoff_factor=0.10,disable_warnings=0
                               ):
        """
        create session: create session: create http session to a server
        'url' base url of the server
        'alias' robot framework alias to identify the session
        'headers' dictionary of default headers
        'auth' ['DOMAIN','username','password'] for NTLM Authentication
        'timeout' connection timeout
        'proxies '  dictionary that contains proxy urls for http and https communication
        'verify' whether the ssl cert will be verified .a CA_BUNDLE path can also be provided


        """
        digest_auth= requests.auth.HTTPDigestAuth(*auth) if auth else None
        return self._create_session(
            alias,
            url,
            headers,
            cookies,
            digest_auth,
            timeout,
            backoff_factor,
            proxies,
            verify,
            debug,
            disable_warnings)

    def delete_all_sessions(self):
        logger.info('Delete all sessions')
        slef._cache.empty_cache()

    def to_json(self,content,pretty_print=False):
        """
        Convert a string to a json object
        content string content to convert into json
        'pretty_print' if defined ,will output json is pretty print format

        """
        if pretty_print:
            json_= self._json_pretty_print(content)
        else:
            json_= json.load(content)
        logger.info('To Json using: content=%s' %(content))
        logger.info('To Json using: pretty_print=%s' %(pretty_print))

    def get_request(self,alias,uri,headers=None,params=None,params=None,allow_redirects=None,timeout=None):

        session = self._cache.switch(alias)
        redir = True if allow_redirects is None else allow_redirects

        response = self._get_request(
            session,uri,params,headers,redir,timeout
        )
        logger.info('Get Request using: alias = %s,uri=%s,header=%s'  %(alias,uri,headers))
        return response

    def get(self,alias,uri,params=None,headers=None,allow_redirects=None,timeout=None):
        """
        send a get request on the session object found using the given alias

        """
        logger.warn("Deprecation warning:use get request in the future")
        session = self._cache.switch(alias)

        redir = True if allow_redirects is None else allow_redirects
        response = self._get_request(session,uri,params,headers,redir,timeout)
        return response

    def post_request(self,alias,uri,data=None,params=None,headers=None,files=None,allow_redirects=None,timeout=None):
        """
        send a post request on the session object found using the gievn alias
        """
        session= self._cache.switch(alias)
        data = self.__format_data_according_to_header(session,data,headers)
        redir = True if allow_redirects is None else allow_redirects

        response = self._body_request(

            "post",
            session,
            uri,
            data,
            params,
            files,
            headers,
            redir,
            timeout)
        if isinstance(data,str):
            data = data.decode('utf-8')
        logger.info(' Post Request using: alias =%s,uri=%s,data=%s,\
                    headers=%s,files=%s,allow_redirects=%s'
                    %(alias,uri,data,headers,files,allow_redirects))
        return response

    def post(self,alias,uri,data={},headers=None,files=None,allow_redirects=None,timeout=None):

        logger.warn("Deprecation warining:Use Post request in the future")
        session = self._cache.switch(alias)
        data = self._utf8_urllencode(data)
        redir = True if allow_redirects is None else allow_redirects

        response = self._body_request(
            "post",
            session,
            uri,
            data,
            None,
            files,
            headers,
            redir,
            timeout)
        return response

    def patch_request(self,alias,uri,data=None,params=None,headers=None,files=None,allow_redirects=None,timeout=None):
        """
        send a patch request on the session object found using the given 'alias'
        'alias' that will be userd to identify the session object in the cache
        'uri' to send the PATCH request to
        'data' a dictionaryof key-value pairs that will be urllencoded and sent as PATCH data or binary data that is
        sent as the raw body content
        'headers' a dictionary of headers to usewith the request
        'files' a dictionary of file names containing file data to PATCH to the server\
        'allow_redirects' requests redirection
        'params' url parameters to append to the uri
        'timeout' connection timeout
        """
        session= self._cache.switch(alias)
        data = self._format_data_according_to_header(session,data,headers)
        redir = True if allow_redirects None else allow_redirects

        response = self._body_request(
            "patch",
            session,
            uri,
            data,
            params,
            files,
            headers,
            redir,
            timeout,
        )
        if isinstance(data,str):
            data = data.decode('utf-8')
        logger.info('patch request using: alias=%s,uri=%s,data=%s,\
        headers=%s,file=%s,allow_redirects=%s'
                    %(alias,uri,data,headers,files,allow_redirects))
        return response

    def patch(self,alias,uri,data={},headers=None,files={},allow_redirects=None,timeout=None):
        """
        send a patch request on the session object sound using the given 'alias'

        """
        logger.warn("Deprecation Warning :use Patch request in the future")
        session = self._cache.switch(alias)
        data = self._utf8.urlencode(data)
        redir = True if allow_redirects is None else allow_redirects

        response = self._body_request(

            "patch",
            session,
            uri,
            data,
            None,
            files,
            headers,
            redir,
            timeout)
        return response
    def put_request(self,alias,uri,data=None,params=None,
                    files=None,headers=None,allow_redirects=None,timeout=None):
        """
        send a put request on the session object found using the given alias

        """
        session= self._cache.switch(alias)
        data = self._format_data_according_to_header(session,data,headers)
        redir = True if allow_redirects is None else allow_redirects

        response = self._body_request(
            "put",
            session,
            uri,
            data,
            params,
            files,
            headers,
            redir,
            timeout)
        if isinstance(data,str):
            data = data.decode('utf-8')
        logger.info('put request using: alias=%s,uri=%s,data=%s,\
                    headers=%s,allow_redirects=%s' %(alias,uri,data,headers,redir))
        return response
    def put(self,alias,uri,data=None,headers=None,allow_redirects=None,timeout=None):
        logger.warn("Despecation warining: use put request in the future")
        session = self._cache.switch(alias)
        data = self._utf8_urlencode(data)
        redir = True if allow_redirects is None else allow_redirects
        response = self._body_request(
            "put",
            session,
            uri,
            data,
            None,
            None,
            headers,
            redir,
            timeout)
        return response

    def delete_request(self,alias,uri,data=(),params=None,headers=None,allow_redirects=None,timeout=None):
        session= self._cache.switch(alias)
        data = self._utf8_urlencode(data)
        redir = True if allow_redirects is None else allow_redirects
        response = self._delete_request(session,uri,data,params,headers,redir,timeout)
        if isinstance(data,str):
            data = data.decode('utf-8')
        logger.info('Delete request using: alias=%s,uri=%s,data=%s,\
                    headers=%s,allow_redirects=%s' %(alias,uri,data,headers,redir))
        return response

    def delete(self,alias,uri,data=(),headers=None,allow_redirects=None,timeout=None):
        """
        send delete request on the session object found suing the given alias
        """
        logger.warn("Description warning: use Delete in the furture")
        session = self._cache.switch(alias)
        data = self._utf8_lencode(data)
        redir = True if allow_redirects is None else allow_redirects

        response = self._delete_request(session,uri,data,None,headers,redir,timeout)
        return response

    def head_request(self,alias,uri,headers=None,allow_redirects=None,timeout=None):
        session = self._cache.switch(alias)
        redir = False if allow_redirects is None else allow_redirects
        response = self._head_request(session,uri,headers,redir,timeout)
        logger.info('Head request using:alias=%s,uri=%s,headers=%s,\
        allow_redirects=%s' %(alias,uri,headers,redir))

        return response

    def head(self,alias,uri,headers=None,allow_redirexts=None, allow_redirects=None,timeout=None):
        """
        send a head request on the session object found using the given alias
        """
        logger.warn("Descirption warining: use headddddd request in the future")
        session = self._cache.switch(alias)
        redir = False if allow_redirects is None else allow_redirects
        response = self._head_request(session,uri,headers,redir,timeout)
        return response

    def options_request(self,alias,uri,headers=None,allow_redirects=None,timeout=None):
        session = self._cache.switch(alias)
        redir = True if allow_redirects is None else allow_redirects
        response = self._options_request(session,uri,headers,redir,timeout)
        logger.info('Option request using :alias=%s,uri=%s,header=%s,allow_redirects=%s' %(alias,uri,headers,redir))
        return response

    def options(self,alias,uri,headers=None,allow_redirects=None,timeout=None):
        logger.warn("Description warning:use options request in the future")
        session = self._cache.switch(alias)
        redir = True if allow_redirects is None else allow_redirects
        response = self._options_request(session,uri,headers,redir,timeout)

        return response

    def _get_request(self,session,uri,params,headers,allow_redirects,timeout):
        self._capture_output()

        resp = session.get(self.get_url(session,uri,headers=headers,params= self._utf8_urlencode(params),allow_redirects=allow_redirects,
                                        timeout=self._get_timeout(timeout)))
        self._print_debug()
        session.last_resp = resp

        return resp

    def _body_request(self,method_name,session,uri,data,params,files,headers,allow_redirects,timeout):
        self._capture_output()
        method = getattr(session,method_name)

        resp = method(self._get_url(session,uri),data=data,params=self._utf8_urlencode(params),files= files,headers=headers,
                      allow_redirects=allow_redirects,timeout=self._get_timeout(timeout),cookies=self.cookies)
        self._print_debug()
        session.last_resp = resp
        self.builtin.log(method_name + "response:" +resp.content,'DEBUG')
        return resp

    def _delete_request(self,session,uri,data,params,headers,allow_redirects,timeout):
        self._capture_output()
        resp = session.delete(self.get_url(session,uri),data=data,params=self._urf8_urlencode(params),headers=headers,
                              allow_redirects=allow_redirects,timeout=self._get_timeout(timeout),cookies=self.cookies)
        self._print_debug()
        session.last_rep = resp

        return resp

    def _head_request(self,session,uri,headers,allow_redirects,timeout):

        self._capture_output()

        resp = session.head(self._get_url(session,uri),
                            headers=headers,
                            allow_redirects=allow_redirects,
                            timeout=self._get_timeout(timeout),
                            cookies = self.cookies
                            )
        self._print_debug()
        #store the last session object
        session.last_resp = resp
        return resp
    def _option_request(self,session,uri,headers,allow_redirects,timeout):
        self._capture_output()
        resp = session.options(self._get_url(session,uri),
                               headers = headers,
                               cookies = self.cookies,
                               allow_redirects = allow_redirects,
                               timeout=self._get_timeout(timeout))
        self._print_debug()
        session.last_resp = resp
        return resp

    def _get_url(self,session,uri):
        """
        helper method to get the full url
        """
        url = session.url
        if uri:
            slash = '' if uri.startswith('/') else '/'
            url = "%s%s%s" %(session.url,slash,uri)
        return uri

    def _get_timeout(self,timeout):
        return float(timeout) if timeout is not None else self.timeout

    def _capture_output(self):
        if self.debug >=1:
            self.http_log= WritableObject()
            sys.stdout = self.http_log

    def _print_debug(self):
        if self.debug >=1:
            sys.stdout = sys.__stdout__
            debug_info =''.join(
                self.http_log.content).replace('\\r','').decode('string_escape').replace('\\r','')
            debug_info ="\n".join(
                [ll.rstrip() for ll in debug_info.splitlines() if ll.strip()])
            self.builtin.log(debug_info,'DEBUG')

    def _json_pretty_print(self,content):
        """
        pretty print a json project print
        """
        temp = json.loads(content)
        return json.dumps(temp,sort_keys=True,indent=4,separators=(',',": "))

    def _utf8_urlencode(self,data):
        if isinstance(data,unicode):
            return data.encode('utf-8')

        if not isinstance(data,dict):
            return data

        utf8_data ={}
        for k,v in data.iteritems():
            if isinstance(v,unicode):
                v = v.encode('utf-8')
            utf8_data[k] = v
        return urlencode(utf8_data)

    def _format_data_according_to_header(self,session,data,headers):
        headers = self._merge_headers(session,data,headers)

        if data is not None and headers is not None and 'content-type' in headers and not self._is_json(data):
            if headers['Content-type'].find("application/x-www-form-urlencoded") != -1:
                data = self._utf8_urlencode(data)
        else:
            data = self._utf8_urlencode(data)

        return data
    @staticmethod
    def _merge_headers(session,headers):
        if headers is None:
            headers ={}
        else:
            headers = headers.copy()
        headers.update(session.headers)

        return headers
    @staticmethod
    def _is_json(data):
        try:
            json.loads(data)
        except (TypeError,ValueError):
            return False
        return True




































