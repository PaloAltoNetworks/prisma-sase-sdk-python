#!/usr/bin/env python
"""
Prisma SASE API -> list sites, example proof of concept.

**Author:** Palo Alto Networks

**Copyright:** © 2023 Palo Alto Networks. All rights reserved

**License:** MIT
"""
__author__ = "Prisma SASE Developer Support <prisma-sase-developers@paloaltonetworks.com>"
__email__ = "prisma-sase-developers@paloaltonetworks.com"
__copyright__ = "Copyright © 2023 Palo Alto Networks. All rights reserved"
__license__ = """
    MIT License

    Copyright © 2023 Palo Alto Networks. All rights reserved

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
# standard modules
import argparse
import logging

# Prisma SASE Python SDK
import prisma_sase

# alias JSON pretty printer (jd), and JSON Detailed pretty printer (jd_detailed) from prisma_sase SDK.
jd = prisma_sase.jd
jd_detailed = prisma_sase.jd_detailed


# Global Vars
SDK_VERSION = prisma_sase.version
SCRIPT_NAME = 'Prisma SASE Python SDK demo'

# Set logging to use function name
logger = logging.getLogger(__name__)


############################################################################
# Begin Script, parse arguments.
############################################################################

# Parse arguments
parser = argparse.ArgumentParser(description="{0}.".format(SCRIPT_NAME))

# Allow Controller modification and debug level sets.
controller_group = parser.add_argument_group('API', 'These options change how this program connects to the API.')
controller_group.add_argument("--controller", "-C",
                              help="Controller URI, ex. https://api.sase.paloaltonetworks.com",
                              default=None)

controller_group.add_argument("--insecure", "-I", help="Disable SSL certificate and hostname verification",
                              dest='verify', action='store_false', default=True)

login_group = parser.add_argument_group('Login', 'These options allow skipping of interactive login')
login_group.add_argument("--client_id", "-CID", help="Use this client_id obtained on service account creation.",
                         default=None)
login_group.add_argument("--client_secret", "-CS", help="Use this client_secret obtained on service account creation.",
                         default=None)
login_group.add_argument("--tsg_id", "-TID", help="Use this tsg_id obtained on service account creation.",
                         default=None)

debug_group = parser.add_argument_group('Debug', 'These options enable debugging output')
debug_group.add_argument("--debug", "-D", help="Verbose Debug info, levels 0-2", type=int,
                         default=0)

args = vars(parser.parse_args())

if args['debug'] == 1:
    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
    logger.setLevel(logging.INFO)
elif args['debug'] >= 2:
    logging.basicConfig(level=logging.DEBUG,
                        format="%(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
    logger.setLevel(logging.DEBUG)
else:
    # Remove all handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    # set logging level to default
    logger.setLevel(logging.WARNING)

############################################################################
# Instantiate API
############################################################################


sdk = prisma_sase.API(controller=args["controller"], ssl_verify=args["verify"])

# set debug
sdk.set_debug(args["debug"])


############################################################################
# Draw Interactive login banner, run interactive login including args above.
############################################################################

print("{0} v{1} ({2})\n".format(SCRIPT_NAME, SDK_VERSION, sdk.controller))

# interactive or cmd-line specified initial login

while sdk.tenant_name is None:
    sdk.interactive.login_secret(client_id=args["client_id"], client_secret=args["client_secret"], tsg_id=args["tsg_id"])


############################################################################
# End Login handling, begin script..
############################################################################

# Get list of sites.
response = sdk.get.sites()

# status is a boolean based on success/failure. If success, print raw dictionary
if response.sdk_status:
    # Can Print as formatted JSON using json module using commented code below.
    # raw_sites_dict = response.sdk_content
    # print(json.dumps(raw_sites_dict, indent=4))
    # But Prisma SASE has a built-in pretty printer, can just use that on native response as a shortcut.
    # Output is the same as code above.
    jd(response)

# else, let user know something didn't work.
else:
    print("ERROR: ")
    # the jd_detailed builtin pretty-printer will dump all request/response info, and also attempt to hide sensitive
    # cookies/headers (AUTH_TOKEN, X-Auth-Token, etc.) to be safe for log messages/etc.
    jd_detailed(response)

# end of script, run logout to clear session.
print(sdk.get.logout().sdk_content)
