import json

from fair_wizard.automation.common.model import HandlerContext
from handler import handler

result = handler(
    event={
        'accessToken': '414a260d-e442-49a3-a9d7-c3100c21616a',
        'expiresIn': 631138518,
        'idToken': {
            'aud': ['APP-STIPW2WK430U8QYM'],
            'exp': 1726131990,
            'iat': 1726045590,
            'iss': 'https://orcid.org',
            'sub': '0000-0003-0103-8468',
            'nonce': 'FtEIbRdfFc7z2bNjCTaZKDcWNeUKUelvs13K21VL',
            'otherClaims': {
                'at_hash': '5EFNCiiH0bIxdBF_KV8M0g',
                'aud': 'APP-STIPW2WK430U8QYM',
                'auth_time': 1726045311,
                'exp': 1726131990,
                'family_name': 'Knaisl',
                'given_name': 'Vojtěch',
                'email': 'vojtech.knaisl@example.com',
                'iat': 1726045590,
                'iss': 'https://orcid.org',
                'jti': 'a2d40a70-dc85-4104-a5e7-216597f7ff45',
                'nonce': 'FtEIbRdfFc7z2bNjCTaZKDcWNeUKUelvs13K21VL',
                'sub': '0000-0003-0103-8468',
            },
        },
        'idTokenJwt': 'eyJraWQiOiJwcm9kdWN0aW9uLW9yY2lkLW9yZy03aGRtZHN3YXJvc2czZ2p1am84YWd3dGF6Z2twMW9qcyIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiNUVGTkNpaUgwYkl4ZEJGX0tWOE0wZyIsImF1ZCI6IkFQUC1TVElQVzJXSzQzMFU4UVlNIiwic3ViIjoiMDAwMC0wMDAzLTAxMDMtODQ2OCIsImF1dGhfdGltZSI6MTcyNjA0NTMxMSwiaXNzIjoiaHR0cHM6XC9cL29yY2lkLm9yZyIsImV4cCI6MTcyNjEzMTk5MCwiZ2l2ZW5fbmFtZSI6IlZvanTEm2NoIiwiaWF0IjoxNzI2MDQ1NTkwLCJub25jZSI6IkZ0RUliUmRmRmM3ejJiTmpDVGFaS0RjV05lVUtVZWx2czEzSzIxVkwiLCJmYW1pbHlfbmFtZSI6IktuYWlzbCIsImp0aSI6ImEyZDQwYTcwLWRjODUtNDEwNC1hNWU3LTIxNjU5N2Y3ZmY0NSJ9.FKUXTPNO6s_NYQzDvuyl2fwX17mdt2gufVZGjO4pocljV0zb4MFvYNoQHMa10IbnAUkRMCt7Vma_knOTl2ST4Z9qBCmTkh3LSnz1NxzIhYOWYAZ5uljvE-8Agk4WMcD0Cf7Ni2BuFLg5sKE2eEuJleH8j9527pUxOiXAMg4yg8ukzJbVX0ypQj_t3bRE-KGIGlOr3Yvo59NCn5IvtRwgogUr4C3u2vIurYcgkjdpuh_bxZbXoZVoHHJ3sIiwzEZmgkolU6Edc9xf_AtMWtYc3a4K4cDS3aiwuskgSCAUM7_qwzjfIfcq7Wav4qp2-QhqjV12Jnrrl1z2ZD6jsfZUiA',
        'refreshToken': '3a7aad25-0482-4c2c-8fdd-1600b644c80f',
        'tokenType': 'bearer',
    },
    context=HandlerContext(),
)

print(json.dumps(result, indent=2))
