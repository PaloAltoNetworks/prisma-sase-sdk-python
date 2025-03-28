#!/usr/bin/env python
"""
Prisma SASE Python Interactive SDK Helper functions

**Author:** Palo Alto Networks

**Copyright:** © 2025 Palo Alto Networks. All rights reserved

**License:** MIT
"""
import getpass
import webbrowser
import json
import logging
import time
import sys

__author__ = "Prisma SASE Developer Support <prisma-sase-developers@paloaltonetworks.com>"
__email__ = "prisma-sase-developers@paloaltonetworks.com"
__copyright__ = "Copyright © 2025 Palo Alto Networks. All rights reserved"
__license__ = """
    MIT License

    **Copyright:** © 2025 Palo Alto Networks. All rights reserved

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

# Set logging to function name
api_logger = logging.getLogger(__name__)
"""`logging.getlogger` object to enable debug printing via `prisma_sase.API.set_debug`"""

PYTHON36_FEATURES = False
""" Boolean: This flag is automatically set based on detected Python version. if 3.6.1+, enables additional features."""

# python 2 to 3 support
try:
    compat_input = raw_input
except NameError:
    compat_input = input

# python 2 and 3 handling
if sys.version_info >= (3, 6,):
    # Python 3.6 or higher
    PYTHON36_FEATURES = True
    text_type = str
    binary_type = bytes
elif sys.version_info >= (3, ):
    # Python 3.x, not supported but try - but no asyncio/websockets.
    PYTHON36_FEATURES = False
    text_type = str
    binary_type = bytes
else:
    # Python 2.x, supported - but no asyncio/websockets.
    PYTHON36_FEATURES = False
    text_type = unicode
    binary_type = str


class Interactive(object):
    """
    Prisma SASE API - Interactive helper functions

    Object to help with interactive complex functions instead of raw API accesses
    """

    # placeholder for parent class namespace
    _parent_class = None

    def login(self, email=None, password=None, saml_auto_browser=True,
              saml_wait_loops=20, saml_wait_delay=5, client_login=True, client=None,
              prompt=None):
        """
        Interactive login using the `prisma_sase.API` object. This function is more robust and handles SAML and MSP accounts.
        Expects interactive capability. if this is not available, use `prisma_sase.API.post.login` directly.

        **Parameters:**:

          - **email**: Optional. Email to log in for, will prompt if not entered.
          - **password**: Optional. Password to log in with, will prompt if not entered. Ignored for SAML v2.0 users.
          - **saml_auto_browser**: Optional. Attempt to automatically open a browser tab/window for SAML v2.0 users.
                                   Default True.
          - **saml_wait_loop**: Optional. Number of times to wait `saml_wait_delay` in seconds. Default: 20
          - **saml_wait_delay**: Optional. Time (seconds) to wait for SAML 2.0 Authentication each loop. Default: 5
          - **client_login**: Optional. Boolean, If session is an ESP/MSP, attempt to auto-login to client. Default: True
          - **client**: Optional. String or None. Client Canonical Name, Client Name, or Client ID to log in to.
                        If None, will prompt with menu. Default: None
          - **prompt**: Optional. text. If one of `default`, `minimal`, or `detailed`, will do as below.
            - `default` displays "controller login: " and "controller password: "
            - `minimal` displays "login: " and "Password: "
            - `detailed` displays "<controller hostname> login: " and "<controller hostname> password: "
            - Any other value will display "<entered value> login: " and <entered value> password: "

        **Returns:** Bool. In addition the function will mutate the `prisma_sase.API` constructor items as needed.
        """
        api_logger.info('login function:')

        # set prompt for email/password.

        if prompt is None or not isinstance(prompt, text_type):
            prompt = "default"

        if prompt.lower() == "default":
            login_prompt = "controller login: "
            password_prompt = "controller password: "
        elif prompt.lower() == "minimal":
            login_prompt = "login: "
            password_prompt = "Password: "
        elif prompt.lower() == "detailed":
            login_prompt = "{0} login: ".format(self._parent_class.controller)
            password_prompt = "{0} password: ".format(self._parent_class.controller)
        else:
            # custom prompt
            login_prompt = "{0} login: ".format(prompt)
            password_prompt = "{0} password: ".format(prompt)

        # if email not given in function, or if first login fails, prompt.

        if email is None:
            # If user is not set, pull from cache. If not in cache, prompt.
            if self._parent_class.email:
                email = self._parent_class.email
            else:
                email = compat_input(login_prompt)

        if password is None:
            # if pass not given on function, or if first login fails, prompt.
            if self._parent_class._password:
                password = self._parent_class._password
            else:
                password = getpass.getpass(password_prompt)

        self._parent_class.use_jwt = True
        # Try and login
        # For SAML 2.0 support, set the Referer URL prior to logging in.
        # add referer header to the session.
        self._parent_class.add_headers({'Referer': "{}/v2.0/api/login".format(self._parent_class.controller)})

        # call the login API.
        response = self._parent_class.post.login({"email": email, "password": password})

        if response.sdk_status:
            # Check for SAML 2.0 login or different region
            if not response.sdk_content.get('x_auth_token'):
                # SAML attributes
                urlpath = response.sdk_content.get("urlpath", "")
                request_id = response.sdk_content.get("requestId", "")
                login_region = response.sdk_content.get("login_region", "")
                if urlpath and request_id:
                    # SAML 2.0
                    # try to open web browser automatically
                    if saml_auto_browser:
                        # attempt to open web browser.
                        opened_webbrowser = webbrowser.open(urlpath, new=2, autoraise=False)
                    else:
                        opened_webbrowser = False

                    # if was able to open a browser, print reduced prompt.
                    if opened_webbrowser:
                        print("SAML 2.0: Opened the following SSO login page in new browser tab/window:\n\n{0}\n"
                              "".format(urlpath))
                    else:
                        print('SAML 2.0: To finish login open the following link in a browser\n\n{0}\n'
                              ''.format(urlpath))
                    # wait for SSO to finish.
                    found_auth_token = False
                    for i in range(saml_wait_loops):
                        print('Waiting for {0} seconds for authentication...'.format((20 - i) * 5))
                        saml_response = self.check_sso_login(email, request_id)
                        if saml_response.sdk_status and saml_response.sdk_content.get('x_auth_token'):
                            found_auth_token = True
                            break
                        # wait before retry.
                        time.sleep(saml_wait_delay)
                    if not found_auth_token:
                        print("Login time expired! Please re-login.\n")
                        # log response when debug
                        try:
                            api_logger.debug("LOGIN_FAIL_RESPONSE = %s", json.dumps(response, indent=4))
                        except (TypeError, ValueError):
                            # not JSON response, don't pretty print log.
                            api_logger.debug("LOGIN_FAIL_RESPONSE = %s", str(response))
                        # print login error
                        print('Login failed, please try again', response)
                        # Flush command-line entered login info if failure.
                        self._parent_class.email = None
                        self._parent_class.password = None
                        return False
                elif login_region:
                    # were we told to ignore regions?
                    if not self._parent_class.ignore_region:
                        # We are on the wrong region. We need to change regions and resubmit login request.
                        self._parent_class.update_region_to_controller(login_region)
                        # recall the login function with the new region. Return the result.
                        return self.login(email=email, password=password, saml_auto_browser=saml_auto_browser,
                                          saml_wait_loops=saml_wait_loops, saml_wait_delay=saml_wait_delay,
                                          client_login=client_login, client=client)
                    else:
                        # ignore region set, just continue without re-parsing.
                        api_logger.debug('Ignoring all region info due to ignore_region.')

            api_logger.info('Login API response OK.')
            # if we got here, we either got an x_auth_token in the original login, or
            # we got an auth_token cookie set via SAML. Figure out which.
            auth_token = response.sdk_content.get('x_auth_token')
            if auth_token:
                # token in the original login (not saml) means region parsing has not been done.
                # do now, and recheck if cookie needs set.
                auth_region = self._parent_class.parse_region(response)
                self._parent_class.update_region_to_controller(auth_region)
                self._parent_class.reparse_login_cookie_after_region_update(response)
            # debug info if needed
            api_logger.debug("AUTH_TOKEN=%s", response.sdk_content.get('x_auth_token'))

            # Step 2: Get operator profile for tenant ID and other info. Verify we have tenant_id.
            if self.update_profile_vars() and self._parent_class.tenant_id:

                # add tenant values to API() object
                if self.tenant_update_vars():

                    # Step 3: Check for ESP/MSP. If client login is enabled, handle client login.
                    if self._parent_class.is_esp and client_login:
                        return self.client_login(client=client)
                    # successful!
                    # clear password out of memory
                    self._parent_class._password = None
                    # remove referer header prior to continuing.
                    self._parent_class.remove_header('Referer')
                    return True

                else:
                    print("Tenant detail retrieval failed.")
                    # clear password out of memory
                    self._parent_class.email = None
                    self._parent_class._password = None

                    api_logger.info("EMAIL = %s", self._parent_class.email)
                    api_logger.info("USER_ID = %s", self._parent_class.operator_id)
                    api_logger.info("USER ROLES = %s", json.dumps(self._parent_class.roles))
                    api_logger.info("TENANT_ID = %s", self._parent_class.tenant_id)
                    api_logger.info("TENANT_NAME = %s", self._parent_class.tenant_name)
                    api_logger.info("TOKEN_SESSION = %s", self._parent_class.token_session)

                    # remove referer header prior to continuing.
                    self._parent_class.remove_header('Referer')
                    return False

            else:
                print("Warning: Prisma SD-WAN profile retrieval failure. Please check if the service account "
                      "has the right privileges or Prisma SD-WAN is activated.")
                # Profile detail retrieval failed
                self._parent_class.email = None
                self._parent_class._password = None
                self._parent_class.remove_header('Referer')
                return False

        else:
            # log response when debug
            api_logger.debug("LOGIN_FAIL_RESPONSE = %s", json.dumps(response.sdk_content, indent=4))
            # print login error
            error_text = self._parent_class.pull_content_error(response)
            if error_text:
                print("Login failed: {0}".format(error_text))
            else:
                print('Login failed, please try again:', response.sdk_content)
            # Flush command-line entered login info if failure.
            self._parent_class.email = None
            self._parent_class.password = None

            # remove referer header prior to continuing.
            self._parent_class.remove_header('Referer')
        return False

    def login_secret(self, client_id=None, client_secret=None, tsg_id=None, grant_type=None,
                     scope=None, prompt=None):
        """
        Interactive login using the `prisma_sase.API` object. This function is more robust and handles SAML and MSP accounts.
        Expects interactive capability. if this is not available, use `prisma_sase.API.post.login` directly.

        **Parameters:**:

          - **client_id**: Required. Client ID to generate jwt token, will prompt if not entered.
          - **client_secret**: Required. Client Secret to generate jwt token, will prompt if not entered.
          - **prompt**: Optional. text. If one of `default`, `minimal`, or `detailed`, will do as below.
            - `default` displays "controller login: " and "controller password: "
            - `minimal` displays "login: " and "Password: "
            - `detailed` displays "<controller hostname> login: " and "<controller hostname> password: "
            - Any other value will display "<entered value> login: " and <entered value> password: "
         - **grant_type**: Optional. Grant Type for generating JWT. Default is 'client_credentials'.
         - **scope**: Optional. Authentication scope. Default is 'tsg_id:<tsg_id> email profile'.

        **Returns:** Bool. In addition the function will mutate the `prisma_sase.API` constructor items as needed.
        """
        api_logger.info('login function:')

        # set prompt for email/password.

        if prompt is None or not isinstance(prompt, text_type):
            prompt = "default"

        if prompt.lower() == "default":
            client_id_prompt = "Prisma SASE Client ID: "
            client_secret_prompt = "Prisma SASE Client Secret: "
            tsg_id_prompt = "Prisma SASE TSG ID: "
            grant_type_prompt = "Prisma SASE Authentication Grant Type: "
            scope_prompt = "Prisma SASE Authentication Scope: "
        elif prompt.lower() == "minimal":
            client_id_prompt = "Client ID: "
            client_secret_prompt = "Client Secret: "
            tsg_id_prompt = "TSG ID: "
            grant_type_prompt = "Grant Type: "
            scope_prompt = "Scope: "
        elif prompt.lower() == "detailed":
            client_id_prompt = "{0} Client ID: ".format(self._parent_class.controller)
            client_secret_prompt = "{0} Client Secret: ".format(self._parent_class.controller)
            tsg_id_prompt = "{0} TSG ID: ".format(self._parent_class.controller)
            grant_type_prompt = "{0} Authentication Grant Type: ".format(self._parent_class.controller)
            scope_prompt = "{0} Authentication Scope: ".format(self._parent_class.controller)
        else:
            # custom prompt
            client_id_prompt = "{0} Client ID: ".format(prompt)
            client_secret_prompt = "{0} Client Secret: ".format(prompt)
            tsg_id_prompt = "{0} TSG ID: ".format(prompt)
            grant_type_prompt = "{0} Grant Type: ".format(prompt)
            scope_prompt = "{0} Scope: ".format(prompt)

        # if email not given in function, or if first login fails, prompt.

        if client_id is None:
            # If client_id is not set, pull from cache. If not in cache, prompt.
            if self._parent_class.client_id:
                client_id = self._parent_class.client_id
            else:
                client_id = compat_input(client_id_prompt)

        if client_secret is None:
            # if client_secret not given on function, or if first login fails, prompt.
            if self._parent_class.client_secret:
                client_secret = self._parent_class.client_secret
            else:
                client_secret = getpass.getpass(client_secret_prompt)

        if tsg_id is None:
            # if tsg_id not given on function, or if first login fails, prompt.
            if self._parent_class.tsg_id:
                tsg_id = self._parent_class.tsg_id

        if grant_type is None:
            # if grant_type not given.
            grant_type = 'client_credentials'

        if scope is None:
            # if grant_type not given.
            if tsg_id is None or tsg_id == '':
                scope = 'email profile'
            else:
                scope = 'tsg_id:{0} email profile'.format(tsg_id)

        self._parent_class.client_id = client_id
        self._parent_class.client_secret = client_secret
        self._parent_class.tsg_id = tsg_id
        self._parent_class.grant_type = grant_type
        self._parent_class.scope = scope

        response = self._parent_class._generate_jwt()
        self._parent_class.use_jwt = False

        if response:
            # Step 2: Get operator profile for tenant ID and other info.
            if self.update_profile_vars() and self._parent_class.tenant_id:

                # add tenant values to API() object
                if self.tenant_update_vars():

                    # clear password out of memory
                    self._parent_class._password = None
                    api_logger.info("EMAIL = %s", self._parent_class.email)
                    api_logger.info("USER_ID = %s", self._parent_class.operator_id)
                    api_logger.info("USER ROLES = %s", json.dumps(self._parent_class.roles))
                    api_logger.info("TENANT_ID = %s", self._parent_class.tenant_id)
                    api_logger.info("TENANT_NAME = %s", self._parent_class.tenant_name)
                    api_logger.info("TOKEN_SESSION = %s", self._parent_class.token_session)
                    return True

                else:
                    print("Tenant detail retrieval failed.")
                    # clear password out of memory
                    self._parent_class.client_id = None
                    self._parent_class.client_secret = None
                    return False

            else:
                print("Warning: Prisma SD-WAN profile retrieval failure. Please check if the service account "
                      "has the right privileges or Prisma SD-WAN is activated.")
                # Profile detail retrieval failed
                self._parent_class.client_id = None
                self._parent_class.client_secret = None
                return False

        else:
            # Flush command-line entered login info if failure.
            self._parent_class.client_id = None
            self._parent_class.client_secret = None

        return False

    def service_account(self, data=None, action='get'):
        """
        helper method to create a new service account assuming you already have one created using UI.

        **Parameters:**:

        - data: payload data in dict format for if the action if 'post'. Data needs to contain following attributes.
          - **contact_email**: Required. Contact email for the new service account to be created.
          - **name**: Required. Account name for the new service account to be created.
          - **role**: Required. Account role for the new service account to be created.
          - **description: Optional. If not provided default description string will be used.

        - action: 'get' or 'post' that user needs to perform.

        **Returns:** Bool. In addition the function will mutate the `prisma_sase.API` constructor items as needed.
        """
        api_logger.info('new service account function:')
        account_data = None

        if action == 'post':
            if data and 'contact_email' in data and 'name' in data and 'role' in data:
                # Create service account.
                if 'description' not in data:
                    data['description'] = 'Service Account for {0}'.format(data['name'])

                account_data = {'contact_email': '{}'.format(data['contact_email']),
                                'description': '{}'.format(data['description']),
                                'name': '{}'.format(data['name'])}
            else:
                api_logger.error("Data payload needs to be provided for post action.")
                print("Please provide data and mandatory attributes (contact_email, name and role) for service account creation..")
                return False

        service_account_url = self._parent_class.controller + '/iam/v1/service_accounts'
        # call the login API.
        account_response = self._parent_class.rest_call(service_account_url, action,
                                          data=account_data, jsonify_data=False,
                                          content_json=False)

        if account_response.sdk_status:

            if action == 'post':

                api_logger.info('Creating Service Account response OK..')

                sa_client_id = account_response.sdk_content.get('client_id')
                sa_client_secret = account_response.sdk_content.get('client_secret')
                sa_contact_email = account_response.sdk_content.get('contact_email')
                sa_description = account_response.sdk_content.get('description')
                sa_name = account_response.sdk_content.get('client_secret')
                sa_tsg_id = account_response.sdk_content.get('tsg_id')
                sa_req_id = account_response.sdk_content.get('id')

                print("Service Account deatils:")
                print("Client ID: {0}".format(sa_client_id))
                print("Client Secret: {0}".format(sa_client_secret))
                print("TSG ID: {0}".format(sa_tsg_id))
                print("Account Name: {0}".format(sa_name))

                api_logger.debug("Assigning policy")

                policy_data = {'principal': '{}'.format(data['contact_email']),
                                'resource': 'prn:{0}::::'.format(sa_tsg_id),
                                'role': '{}'.format(data['role'])}

                assign_policy_url = self._parent_class.controller + '/iam/v1/access_policies'
                # call the login API.
                policy_response = self._parent_class.rest_call(assign_policy_url, "post",
                                                  data=policy_data, jsonify_data=False,
                                                  content_json=False)

                if policy_response.sdk_status:
                    api_logger.debug("Assigned role {0} to account {1}".format(data['role'], data['name']))
                    print("Service account creation completed successfully")
                    return account_response
                else:
                    api_logger.debug("SERVICE_ACCOUNT_ASSIGN_POLICY_FAILURE = %s", json.dumps(policy_response.sdk_content, indent=4))
                    error_text = self._parent_class.pull_content_error(policy_response)
                    if error_text:
                        print("assigning policy failed: {0}".format(error_text))
                    else:
                        print('assigning policy, please try again:', policy_response.sdk_content)

                    return account_response

            elif action == 'get':

                api_logger.info('GET Service Account response OK..')

                return account_response


            # Step 2: Get operator profile for tenant ID and other info.
            else:
            # log response when debug
                api_logger.debug("SERVICE_ACCOUNT_CREATION_FAIL_RESPONSE = %s", json.dumps(account_response.sdk_content, indent=4))
                # print login error
                error_text = self._parent_class.pull_content_error(account_response)
                if error_text:
                    print("service account creation failed: {0}".format(error_text))
                else:
                    print('service account creation, please try again:', account_response.sdk_content)

                return account_response

    def client_login(self, client=None):
        """
        If logged into an ESP/MSP, now login to a client.

        **Parameters:**:

          - **client**: Optional. ESP/MSP managed Client Canonical Name, Client Name, or Client ID
                        (matched in this order)

        **Returns:** Boolean Success.
        """
        api_logger.info('client_login function:')

        if self._parent_class.token_session is True:
            # AUTH_TOKENs are not allowed to do client login/logout.
            print("Static AUTH_TOKENs are not allowed to perform client login/logout operations.")
            return False

        # sanity check if ESP
        if self._parent_class.is_esp:
            # ESP/MSP! Pass any client info through to client choice.
            choose_status, chosen_client_id, chosen_client_region = self.client_choice(client=client)

            if choose_status:
                # attempt to login as client
                clogin_resp = self._parent_class.post.clients_login(chosen_client_id, {})

                if clogin_resp.sdk_status:
                    # see if we need to change regions.
                    redirect_region = clogin_resp.sdk_content.get('redirect_region')
                    redirect_x_auth_token = clogin_resp.sdk_content.get('redirect_x_auth_token')
                    redirect_urlpath = clogin_resp.sdk_content.get('redirect_urlpath')

                    if redirect_region is not None and redirect_x_auth_token is not None:
                        api_logger.debug('CLIENT REGION SWITCH: %s -> %s', self._parent_class.controller_region,
                                         redirect_region)
                        # Need to change regions.
                        self._parent_class.update_region_to_controller(redirect_region)

                        # Now set a temporary X-Auth-Token header, overwriting previous if there.
                        # if using a static AUTH_TOKEN, client login will switch to dynamic via
                        # Cookies.
                        self._parent_class.add_headers({'X-Auth-Token': redirect_x_auth_token})

                    # login successful, update profile

                    # Profile call will set new login cookies if switching regions.
                    c_profile = self.update_profile_vars()
                    if redirect_region is not None and redirect_x_auth_token is not None:
                        # if region switch, we need to clear the X-Auth-Token header, as it was a temporary value
                        # and now we are using cookies for ephemeral AUTH_TOKENs.
                        self._parent_class.remove_header('X-Auth-Token')

                    # Update tenant info.
                    t_profile = self.tenant_update_vars()

                    if c_profile and t_profile:
                        # successful full client login.
                        self._parent_class._password = None
                        # remove referer header prior to continuing.
                        self._parent_class.remove_header('Referer')
                        return True

                    else:
                        if t_profile:
                            print("ESP Client Tenant detail retrieval failed. ESP may no longer be valid.")
                        # clear password out of memory
                        self._parent_class.email = None
                        self._parent_class._password = None
                        # remove referer header prior to continuing.
                        self._parent_class.remove_header('Referer')
                        return False

                else:
                    print("ESP Client Login failed. ESP session active.")
                    # clear password out of memory
                    self._parent_class.email = None
                    self._parent_class._password = None
                    # remove referer header prior to continuing.
                    self._parent_class.remove_header('Referer')
                    return False

            else:
                print("ESP Client Choice failed or canceled. ESP session active.")
                # clear password out of memory
                self._parent_class.email = None
                self._parent_class._password = None
                # remove referer header prior to continuing.
                self._parent_class.remove_header('Referer')
                return False
        else:
            # Not ESP
            print("ESP Client login failed. Current session is not an ESP/MSP.")
            # clear password out of memory
            self._parent_class.email = None
            self._parent_class._password = None
            # remove referer header prior to continuing.
            self._parent_class.remove_header('Referer')
            return False

    def client_logout(self, client_login=True, client=None):
        """
        If logged into a client, go back to ESP/MSP.

        **Parameters:**:

          - **client_login**: Optional. Boolean, If session is an ESP/MSP, attempt to auto-login to client. Default: True
          - **client**: Optional. String or None. Client Canonical Name, Client Name, or Client ID to log in to.
                        If None, will prompt with menu. Default: None

        **Returns:** Boolean Success.
        """
        api_logger.info('client_logout function:')

        if self._parent_class.token_session is True:
            # AUTH_TOKENs are not allowed to do client login/logout.
            print("Static AUTH_TOKENs are not allowed to perform client login/logout operations.")
            return False

        # make the client_logout call.
        clogout_resp = self._parent_class.post.clients_logout({})

        if clogout_resp.sdk_status:
            # see if we need to change regions.
            redirect_region = clogout_resp.sdk_content.get('redirect_region')
            redirect_x_auth_token = clogout_resp.sdk_content.get('redirect_x_auth_token')
            redirect_urlpath = clogout_resp.sdk_content.get('redirect_urlpath')

            if redirect_region is not None and redirect_x_auth_token is not None:
                api_logger.debug('CLIENT REGION SWITCH: %s -> %s', self._parent_class.controller_region,
                                 redirect_region)
                # Need to change regions.
                self._parent_class.update_region_to_controller(redirect_region)

                # Now set a temporary X-Auth-Token header, overwriting previous if there.
                # if using a static AUTH_TOKEN, client logout will switch to dynamic via
                # Cookies.
                self._parent_class.add_headers({'X-Auth-Token': redirect_x_auth_token})
            else:
                # If client login works, and we aren't going cross region - we need to flush the X-Auth-Token header
                # here. This is because it's invalid once we move to a client; we're now using cookies.
                # If we are going cross-region, cookie stays until after the profile call.
                self._parent_class.remove_header('X-Auth-Token')

            # login successful, update profile

            # Profile call will set new login cookies if switching regions.
            c_profile = self.update_profile_vars()
            if redirect_region is not None and redirect_x_auth_token is not None:
                # if region switch, we need to clear the X-Auth-Token header, as it was a temporary value
                # and now we are using cookies for ephemeral AUTH_TOKENs.
                self._parent_class.remove_header('X-Auth-Token')

            # Update tenant info.
            t_profile = self.tenant_update_vars()

            if c_profile and t_profile:
                # successful full client login.
                self._parent_class._password = None
                # remove referer header prior to continuing.
                self._parent_class.remove_header('Referer')

                # check if client_login set. If so, relogin to next client.
                if client_login:
                    return self.client_login(client=client)
                else:
                    return True

            else:
                if t_profile:
                    print("ESP Tenant detail retrieval failed. Session may no longer be valid.")
                # clear password out of memory
                self._parent_class.email = None
                self._parent_class._password = None
                # remove referer header prior to continuing.
                self._parent_class.remove_header('Referer')
                return False

        else:
            print("ESP Client Logout failed. Client session may or may not still be active.")
            # clear password out of memory
            self._parent_class.email = None
            self._parent_class._password = None
            # remove referer header prior to continuing.
            self._parent_class.remove_header('Referer')
            return False

    def tenant_update_vars(self):
        """
        Function to update the `prisma_sase.API` object with tenant login info. Run after login or client login.

        **Returns:** Boolean on success/failure,
        """
        api_logger.info('tenant_update_vars function:')
        tenant_resp = self._parent_class.get.tenants()
        status = tenant_resp.sdk_status
        tenant_dict = tenant_resp.sdk_content

        if status:

            api_logger.debug("new tenant_dict: %s", tenant_dict)

            telemetry_region = tenant_dict.get('telemetry_region')
            self._parent_class.panw_region = self._parent_class.telemetry_panw_mapping.get(telemetry_region)
            self._parent_class.add_headers({'X-PANW-Region': self._parent_class.panw_region})

            # Get Tenant info.
            self._parent_class.tenant_name = tenant_dict.get('name', self._parent_class.tenant_id)
            # is ESP/MSP?
            self._parent_class.is_esp = tenant_dict.get('is_esp')
            # grab tenant address for location.
            address_lookup = tenant_dict.get('address', None)
            if address_lookup:
                for key in address_lookup.keys():
                    if address_lookup[key] is None:
                        address_lookup[key] = ""

                tenant_address = "{}, {}, {}, {}, {}, {}".format(address_lookup["street"], address_lookup["street2"],
                                                  address_lookup["city"], address_lookup["state"],
                                                  address_lookup["post_code"], address_lookup["country"])
            else:
                tenant_address = "Unknown"
            self._parent_class.address = tenant_address
            return True
        else:
            # update failed
            return False

    def update_profile_vars(self):
        """
        Function to update the `prisma_sase.API` object with profile info. Run after login or client login.

        **Returns:** Boolean on success/failure,
        """
        api_logger.info('update_profile_vars function:')

        profile = self._parent_class.get.profile()

        if profile.sdk_status:

            # if successful, save tenant id and email info to cli state.
            self._parent_class.tenant_id = profile.sdk_content.get('tenant_id')
            self._parent_class.email = profile.sdk_content.get('email')
            self._parent_class.operator_id = profile.sdk_content.get('id')
            # for backwards compatible _user_id after promoting operator_id to public.
            self._parent_class._user_id = self._parent_class.operator_id
            self._parent_class.roles = profile.sdk_content.get('roles', [])
            self._parent_class.token_session = profile.sdk_content.get('token_session')
            if self._parent_class.controller_region is None:
                self._parent_class.controller_region = profile.sdk_content.get('region')

            return True

        else:
            api_logger.info('Profile retrieval failed.')
            # clear password out of memory
            self._parent_class._password = None
            return False

    def session_allowed_clients(self):
        """
        Get the current ESP session allowed clients info.

        **Returns:** Tuple of (Boolean Success status,
                               Client Name to ID dict, Client Canonical Name to ID dict, Client ID to Region dict.)
        """
        api_logger.info('session_allowed_clients function:')

        # sanity check if ESP
        if self._parent_class.is_esp:
            # Make API requests
            clients = self._parent_class.get.tenant_clients()
            clients_perms = self._parent_class.get.esp_operator_permissions(self._parent_class.operator_id)

            client_status = clients.sdk_status
            clients_dict = clients.sdk_content
            c_perms_status = clients_perms.sdk_status
            c_perms_dict = clients_perms.sdk_content

            # Build MSP/ESP id-name dict, get list of allowed tenants.
            if client_status and c_perms_status:
                # Client maps, name to ID, Canonical Name to ID, and ID to Region.
                tenant_client_id2n = {}
                tenant_client_canonical_id2n = {}
                client_n2id = {}
                client_canonical_n2id = {}
                client_id2r = {}
                for client_entry in clients_dict.get('items', []):
                    if type(client_entry) is dict:
                        # create client ID to name map table.
                        client_id = client_entry.get('id', "err")
                        client_name = client_entry.get('name', "")
                        client_canonical_name = client_entry.get('canonical_name', "")
                        # update tenant client canonical name/name tables. Current session may not have access to
                        # all of these. Will filter to specific client accessible ones later before return.
                        tenant_client_canonical_id2n[client_id] = client_canonical_name
                        tenant_client_id2n[client_id] = client_name

                # Using Tenant client list, build dicts for this session.
                for client_perm in c_perms_dict.get('items', []):
                    if type(client_perm) is dict:
                        client_id = client_perm.get('client_id')
                        client_region = client_perm.get('region')
                        # update client id to region map
                        client_id2r[client_id] = client_region
                        # build session specific name maps.
                        client_n2id[tenant_client_id2n.get(client_id, client_id)] = client_id
                        client_canonical_n2id[tenant_client_canonical_id2n.get(client_id, client_id)] = client_id
                # return results.
                return True, client_n2id, client_canonical_n2id, client_id2r

            else:
                # Could not get a specific API response..
                api_logger.debug("API request failure. "
                                 "Response status - tenant_clients: %s, esp_operator_permissions: %s.",
                                 client_status,
                                 c_perms_status)
                return False, {}, {}, {}
        else:
            # not ESP/MSP. Fail.
            api_logger.debug("Not ESP/MSP, cannot get allowed clients")
            return False, {}, {}, {}

    def client_choice(self, client=None):
        """
        Get info for ESP/MSP managed clients this session has access to. If passed a valid Client Canonical Name,
        Client Name, or Client ID - return the info for that client. Otherwise, present a menu and let the user
        choose.

        **Parameters:**:

          - **client**: ESP/MSP managed Client Canonical Name, Client Name, or Client ID (matched in this order)

        **Returns:** Tuple with (Boolean success, selected client ID, selected client Region).
        """
        api_logger.info('client_choice function:')

        # Get client session access info
        session_status, client_n2id, client_canonical_n2id, client_id2r = self.session_allowed_clients()

        if session_status:
            # got client info. Lets go.
            if client:
                # got name/id specified in function. Use that to return client choice to login function.
                # lets see what we can find. first check canonical.
                client_id = client_canonical_n2id.get(client)

                # did it match? If not, check client name.
                if client_id is None:
                    api_logger.debug("ESP/MSP Specified client '%s' no match in Client Canonical Names", client)
                    client_id = client_n2id.get(client)

                    # Again, match check. If not, ID is last shot.
                    if client_id is None:
                        api_logger.debug("ESP/MSP Specified client '%s' no match in Client Names", client)
                        # use client id to region dict keys to check if valid ID.
                        if client in client_id2r.keys():
                            # matched valid client ID. Set client_id direct to client.
                            client_id = client
                        else:
                            # client doesn't match anything. Fail.
                            api_logger.debug("ESP/MSP Specified client '%s' not found in Client IDs.", client)
                            return False, None, None

                # if we got here, client_id should have been found. Return.
                return True, client_id, client_id2r.get(client_id)

            else:
                # no name. Use menu.
                menu_list = []
                # need a id->Name dict to create the menu list. Reverse the existing n2id dict.
                client_id2n = {v: k for k, v in client_n2id.items()}

                # iterate the canonical name dict to create the client menu
                for client_canonical_name, client_id in client_canonical_n2id.items():
                    client_name = client_id2n.get(client_id, client_id)
                    client_region = client_id2r.get(client_id)
                    # Create the menu entry tuple
                    menu_list.append(
                        ("{0} ({1})".format(client_name, client_canonical_name), client_id, client_region)
                    )

                # empty menu/no clients?
                if not menu_list:
                    # no clients
                    print("No ESP/MSP clients allowed for user.")
                    return False, None, None

                # ask user to select client
                status, chosen_client_result = self.quick_menu("ESP/MSP Detected. Select a client to use:",
                                                               "{0}) {1} Region: {3}", menu_list)

                if status:
                    # Chosen client ID is the 2nd item in the tuple, client_region is 3rd item
                    return True, chosen_client_result[1], chosen_client_result[2]
                else:
                    # failed - likely canceled.
                    return False, None, None
        else:
            print("ESP/MSP detail retrieval failed.")
            return False, None, None

    @staticmethod
    def quick_menu(banner, list_line_format, choice_list):
        """
        Function to display a quick menu for user input

        **Parameters:**

          - **banner:** Text to display before menu
          - **list_line_format:** Print'ing string with format spots for index + tuple values
          - **choice_list:** List of tuple values that you want returned if selected (and printed)

        **Returns:** Boolean Status, Tuple that was selected.
        """
        api_logger.info('quick_menu function:')

        # Setup menu
        invalid = True
        menu_int = -1

        # loop until valid
        while invalid:
            print(banner)

            for item_index, item_value in enumerate(choice_list):
                print(list_line_format.format(item_index + 1, *item_value))

            menu_choice = compat_input("\nChoose a Number or (Q)uit: ")

            if str(menu_choice).lower() in ['q']:
                # exit
                print("Canceling Menu..")
                # best effort logout
                return False, None

            # verify number entered
            try:
                menu_int = int(menu_choice)
                sanity = True
            except ValueError:
                # not a number
                print("ERROR: ", menu_choice)
                sanity = False

            # validate number chosen
            if sanity and 1 <= menu_int <= len(choice_list):
                invalid = False
            else:
                print("Invalid input, needs to be between 1 and {0}.\n".format(len(choice_list)))

        # return the choice_list tuple that matches the entry.
        return True, choice_list[int(menu_int) - 1]

    def check_sso_login(self, operator_email, request_id):
        """
        Login to the Prisma SASE API, and see if SAML SSO has occurred.
        This function is used to check and see if SAML SSO has succeeded while waiting.

        **Parameters:**

          - **operator_email:** String with the username to log in with
          - **request_id:** String containing the SAML 2.0 Request ID from previous login attempt.

        **Returns:** Tuple (Boolean success, Token on success, JSON response on error.)
        """
        api_logger.info('check_sso_login function:')

        data = {
            "email": operator_email,
            "requestId": request_id
        }

        # If debug is set..
        api_logger.info('check_sso_login function:')

        response = self._parent_class.post.login(data=data)

        # If valid response, but no token.
        if not response.sdk_content.get('x_auth_token'):
            # no valid login yet.
            return response

        # update with token and region
        auth_region = self._parent_class.parse_region(response)
        self._parent_class.update_region_to_controller(auth_region)
        self._parent_class.reparse_login_cookie_after_region_update(response)

        return response

    def logout(self, force=False):
        """
        Interactive logout - ensures uid/tid cleared so `prisma_sase.API` object/ requests.Session can be re-used.

        **Parameters:**:

          - **force**: Bool, force logout API call, even when using a static AUTH_TOKEN.

        **Returns:** Bool of whether the operation succeeded.
        """
        api_logger.info('logout function:')

        # Extract requests session for manipulation.
        session = self._parent_class.expose_session()

        # if force = True, or token_session = None/False, call logout API.
        if force or not self._parent_class.token_session:
            # Call Logout
            result = self._parent_class.get.logout()
            if result.sdk_status:
                # clear info from session.
                self._parent_class.tenant_id = None
                self._parent_class.tenant_name = None
                self._parent_class.is_esp = None
                self._parent_class.client_id = None
                self._parent_class.address_string = None
                self._parent_class.email = None
                self._parent_class.operator_id = None
                # for backwards compatible _user_id after promoting operator_id to public.
                self._parent_class._user_id = self._parent_class.operator_id
                self._parent_class._password = None
                self._parent_class.roles = None
                self._parent_class.token_session = None
                # Cookies are removed via LOGOUT API call. if X-Auth-Token set, clear.
                if session.headers.get('X-Auth-Token'):
                    self._parent_class.remove_header('X-Auth-Token')

            return result.sdk_status

        else:
            # Token Session and not forced.
            api_logger.debug('TOKEN SESSION, LOGOUT API NOT CALLED.')
            # clear info from session.
            self._parent_class.tenant_id = None
            self._parent_class.tenant_name = None
            self._parent_class.is_esp = None
            self._parent_class.client_id = None
            self._parent_class.address_string = None
            self._parent_class.email = None
            self._parent_class.operator_id = None
            # for backwards compatible _user_id after promoting operator_id to public.
            self._parent_class._user_id = self._parent_class.operator_id
            self._parent_class._password = None
            self._parent_class.roles = None
            self._parent_class.token_session = None
            # if X-Auth-Token set, clear.
            if session.headers.get('X-Auth-Token'):
                self._parent_class.remove_header('X-Auth-Token')

            return True

    @staticmethod
    def jd(api_response):
        """
        JD (JSON Dump) function. Meant for quick pretty-printing of Prisma SASE Response objects.

        Example: `jd(sdk_sess.get.sites())`

        **Returns:** No Return, directly prints all output.
        """
        try:
            # attempt to print the sdk_content. should always be a Dict if it exists.
            print(json.dumps(api_response.sdk_content, indent=4))
        except (TypeError, ValueError, AttributeError):
            # sdk_content did not exist, or was not JSON serializable. Try pretty printing the base obj.
            try:
                print(json.dumps(api_response, indent=4))
            except (TypeError, ValueError, AttributeError):
                # Same issue, just raw print the passed data. Let any exceptions happen here.
                print(api_response)
        return

    @staticmethod
    def quick_confirm(prompt, default_value):
        """
        Function to display a quick confirmation for user input

        **Parameters:**

          - **prompt:** Text to display before confirm
          - **default_value:** Default value for no entry

        **Returns:** 'y', 'n', or Default value.
        """
        valid = False
        value = default_value.lower()
        while not valid:
            input_val = compat_input(prompt + "[{0}]: ".format(default_value))

            if input_val == "":
                value = default_value.lower()
                valid = True
            else:
                try:
                    if input_val.lower() in ['y', 'n']:
                        value = input_val.lower()
                        valid = True
                    else:
                        print("ERROR: enter 'Y' or 'N'.")
                        valid = False

                except ValueError:
                    print("ERROR: enter 'Y' or 'N'.")
                    valid = False

        return value

    @staticmethod
    def quick_int_input(prompt, default_value, min_val=1, max_val=30):
        """
        Function to display a quick question for integer user input

        **Parameters:**

          - **prompt:** Text / question to display
          - **default_value:** Default value for no entry
          - **min_val:** Lowest allowed integer
          - **max_val:** Highest allowed integer

        **Returns:** integer or default_value.
        """
        valid = False
        num_val = default_value
        while not valid:
            input_val = compat_input(prompt + "[{0}]: ".format(default_value))

            if input_val == "":
                num_val = default_value
                valid = True
            else:
                try:
                    num_val = int(input_val)
                    if min_val <= num_val <= max_val:
                        valid = True
                    else:
                        print("ERROR: must be between {0} and {1}.".format(min, max))
                        valid = False

                except ValueError:
                    print("ERROR: must be a number.")
                    valid = False

        return num_val

    @staticmethod
    def quick_str_input(prompt, default_value):
        """
        Function to display a quick question for text input.

        **Parameters:**

          - **prompt:** Text / question to display
          - **default_value:** Default value for no entry

        **Returns:** text_type() or default_value.
        """
        valid = False
        str_val = default_value
        while not valid:
            input_val = compat_input(prompt + "[{0}]: ".format(default_value))

            if input_val == "":
                str_val = default_value
                valid = True
            else:
                try:
                    str_val = text_type(input_val)
                    valid = True

                except ValueError:
                    print("ERROR: must be text.")
                    valid = False

        return str_val

    interactive_client_choice = client_choice
    """ Backwards-compatibility alias of `interactive_client_choice` to `client_choice`"""

    interactive_tenant_update_vars = tenant_update_vars
    """ Backwards-compatibility alias of `interactive_tenant_update_vars` to `tenant_update_vars`"""

    interactive_update_profile_vars = update_profile_vars
    """ Backwards-compatibility alias of `interactive_update_profile_vars` to `update_profile_vars`"""
