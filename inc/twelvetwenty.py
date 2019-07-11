# All of the libraries used in this Python class
import requests

# "Constants" to configure the class
API_VERSION = "v2"
INITIAL_PATH = "https://{}.admin.sandbox-12twenty.com/api"
CLIENT_PATH = "client"
AUTHENTICATION_TOKEN_PATH = "generateAuthenticationToken"
DOCUMENTATION_PATH = "documentation"
STUDENTS_PATH = "students"
LOOKUPS_PATH = "lookups"
NO_SUBDOMAIN_ERROR_MESSAGE = "A sub-domain has not been set"
NOT_AUTHENTICATED_ERROR_MESSAGE = "The API is not authenticated"

"""
    Class: TwelveTwenty
    Purpose: To create a programmable way to interface with the 12Twenty API
"""
class TwelveTwenty:
    """
        Private Methods
    """

    # Constructor used to initialize the object
    def __init__(self, subdomain=None, debug=False):
        self.__debug = debug
        self.__subdomain = subdomain
        self.__is_authenticated = False
        self.__auth_token = None

    # Method used to get the FQDN for the API
    def __get_initial_path(self):
        return INITIAL_PATH.format(self.__subdomain)

    # Method used to return the auth token in the correct format
    def __get_authorization_headers(self):
        return {"Authorization": "{} {}".format("Bearer", self.__auth_token)}

    # Descriptor used to provide a sub-domain check before a method call (i.e. @__has_subdomain)
    def __has_subdomain(function):
        def wrapper(self, *args, **kwargs):
            if not self.__subdomain:
                raise Exception(NO_SUBDOMAIN_ERROR_MESSAGE)

            return function(self, *args, **kwargs)

        return wrapper

    # Descriptor used to provide an authentication check before a method call (i.e. @__is_authenticated)
    def __is_authenticated(function):
        def wrapper(self, *args, **kwargs):
            if not self.__is_authenticated:
                raise Exception(NOT_AUTHENTICATED_ERROR_MESSAGE)

            return function(self, *args, **kwargs)

        return wrapper

    """
        Public Methods
    """

    # Method used to set the sub-domain held in the object
    def set_subdomain(self, subdomain):
        self.__subdomain = subdomain
        self.__is_authenticated = False

    # Method used to get the sub-domain held in the object
    def get_subdomain(self):
        return self.__subdomain

    # Method used to check if the user is authenticated with the API
    def is_authenticated(self):
        return self.__is_authenticated

    # Method used to authenticate with the API
    @__has_subdomain
    def authenticate(self, key):
        uri = "{}/{}/{}".format(self.__get_initial_path(), CLIENT_PATH, AUTHENTICATION_TOKEN_PATH)

        try:
            r = requests.get(uri, params={'key': key})

            r.raise_for_status()

        except Exception as e:
            raise Exception(e, r.text)

        else:
            if r.status_code is requests.codes.ok:
                self.__auth_token = r.text
                self.__is_authenticated = True

                return True

            else:
                return None

    # Method used to return the documentation URL for the current sub-domain
    @__has_subdomain
    def get_documentation_url(self):
        return "{}/{}/{}".format(self.__get_initial_path(), API_VERSION, DOCUMENTATION_PATH)

    # Method used to create a student object in the API (from a Python dictionary object)
    @__is_authenticated
    def create_student(self, student):
        uri = "{}/{}/{}".format(self.__get_initial_path(), API_VERSION, STUDENTS_PATH)

        try:
            r = requests.post(uri, headers=self.__get_authorization_headers(), json=student)

            r.raise_for_status()

        except Exception as e:
            raise Exception(e, r.text)

        else:
            if r.status_code is requests.codes.ok:
                return r.json()

            else:
                return None

    # Method used to update a student object in the API (based on ID and from a Python dictionary object)
    @__is_authenticated
    def update_student(self, id, student):
        uri = "{}/{}/{}/{}".format(self.__get_initial_path(), API_VERSION, STUDENTS_PATH, id)

        try:
            r = requests.patch(uri, headers=self.__get_authorization_headers(), json=student)

            r.raise_for_status()

        except Exception as e:
            raise Exception(e, r.text)

        else:
            if r.status_code is requests.codes.ok:
                return r.json()

            else:
                return None

    # Method used to obtain the lookup IDs available from the API
    @__is_authenticated
    def get_lookups(self):
        uri = "{}/{}/{}".format(self.__get_initial_path(), API_VERSION, LOOKUPS_PATH)

        try:
            r = requests.get(uri, headers=self.__get_authorization_headers())

            r.raise_for_status()

        except Exception as e:
            raise Exception(e, r.text)

        else:
            if r.status_code is requests.codes.ok:
                return r.json()

            else:
                return None

    # Method used to obtain the options from a specific lookup (by ID)
    @__is_authenticated
    def get_lookup(self, id):
        uri = "{}/{}/{}/{}/options".format(self.__get_initial_path(), API_VERSION, LOOKUPS_PATH, id)

        try:
            r = requests.get(uri, headers=self.__get_authorization_headers())

            r.raise_for_status()

        except Exception as e:
            raise Exception(e, r.text)

        else:
            if r.status_code is requests.codes.ok:
                return r.json()

            else:
                return None
