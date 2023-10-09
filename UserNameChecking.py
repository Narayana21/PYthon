# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores [a – z], [A – Z], [0 – 9], [_-].
# The website name can only have letters and digits [a – z], [A – Z], [0 – 9].
# The extension can only contain letters [a – z], [A – Z].
# The maximum length of the extension is 3.
# s=['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

s='brian-23@hackerrank.com'
def fun(s):
    username,url=s.split('@')
    website,extension=url.split('.')
    length=len(extension)
    if(length==3):
        if(website.isalpha() and website.isdigit()):
            if(username.isalpha() and username.isdigit()):
                dash=username.find('-')
                underscore=username.find('_')
                if(dash!=-1 and underscore!=-1):
                    return True
            else:
                return False
        else:
            return False
    else:
        return False



fun(s)