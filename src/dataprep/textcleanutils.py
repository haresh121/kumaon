from unidecode import unidecode
import ftfy

def bad_token_remove(sent: str, _tags=None):
    if not _tags:
        _tags = ["<\/title>", "<title>", "<description>", "<\/description>"]

    for tag in _tags:
        sent.replace(tag, '')

    return {'clean_text': sent.strip(' ')}

def bad_line_filter(sent, _tags=None):
    if not _tags:
        _tags = ['<url>', '<talkid>', '<keywords>']

    return {'remove_line': any([tag in sent for tag in _tags])}

def bad_accent_replace(sent):
    return {'fixed_text': unidecode(ftfy.fix_text(sent))}

def bad_length_remove(sent, _min=1, _max=128):
    if _min <= len(sent.split(" ")) <= _max:
        return {'remove_len': False}
    return {'remove_len': True}


op_dict = {
    'bad_token_remove': bad_token_remove,
    'bad_line_filter': bad_line_filter,
    'bad_accent_replace': bad_accent_replace,
    'bad_length_remove': bad_length_remove
}