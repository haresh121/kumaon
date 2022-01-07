from unidecode import unidecode
import ftfy

def fix_bad_token(sent: str, _tags=None):
    '''
    Returns string with _tags replaced.
    '''
    if not _tags:
        _tags = ["<\/title>", "<title>", "<description>", "<\/description>"]
    for tag in _tags:
        sent.replace(tag, '')
    return sent.strip(' ')

def filter_bad_tag(sent, _tags=None):
    '''
    Returns True is none of _tags in string else False.
    '''
    if not _tags:
        _tags = ['<url>', '<talkid>', '<keywords>']

    return not any( [tag in sent for tag in _tags] )
    # return {'remove_line': any([tag in sent for tag in _tags])}

def fix_bad_accent(sent: str):
    '''
    Returns string with accent character corrected for some non-EN 
    languages like DE, FR.
    '''
    return unidecode(ftfy.fix_text(sent))

def filter_long_short(sent, _min=1, _max=128):
    '''
    Returns True of len of sent (either Iterable or str split on whitespace) 
    lies in [_min,_max] else False.
    '''
    sent = sent.split(' ') if isinstance(sent,str) else sent # is assumed iterable
    if _min <= len(sent) <= _max:
        return True
    return False

def filter_invalid_sent(s):
    '''
    Returns True if s does have any Null values in it, else False.
    '''
    val = []
    for i in s:
        if s[i] == None:
            val.append(False)
        else:
            val.append(True)
    return all(val)