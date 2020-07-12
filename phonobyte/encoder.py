'''

    phonobyte, binary data to phonetically pronounceable words encoder
    Copyright (C) 2020 meeb@meeb.org

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''


try:
    text_type = unicode
    py = 2
except NameError:
    text_type = str
    py = 3


phono = ('jab', 'tip', 'led', 'rut', 'dak', 'jig', 'rud', 'pub', 'not', 'kid',
         'bid', 'gup', 'lep', 'juk', 'jib', 'sid', 'fon', 'dug', 'lap', 'sog',
         'bug', 'ret', 'net', 'fip', 'gad', 'peg', 'gap', 'fet', 'rog', 'lob',
         'lin', 'pip', 'fud', 'lag', 'gut', 'reb', 'din', 'sun', 'jun', 'dig',
         'rag', 'neg', 'bin', 'ben', 'gob', 'run', 'fab', 'lit', 'ked', 'rug',
         'lod', 'rib', 'rip', 'sod', 'ped', 'dip', 'leg', 'sib', 'sad', 'sat',
         'pak', 'jet', 'bun', 'gon', 'geg', 'bit', 'gud', 'rig', 'dek', 'pot',
         'pug', 'ken', 'gub', 'rid', 'pen', 'nep', 'gib', 'jot', 'pup', 'tid',
         'sin', 'kin', 'job', 'ted', 'fun', 'fop', 'dan', 'nip', 'but', 'tun',
         'put', 'jog', 'jit', 'lad', 'pig', 'got', 'tot', 'gak', 'sot', 'rin',
         'lid', 'don', 'den', 'pod', 'rit', 'gat', 'ket', 'sab', 'rat', 'bub',
         'dod', 'dep', 'dup', 'tod', 'lat', 'nub', 'lab', 'pan', 'rap', 'tib',
         'tan', 'bed', 'seg', 'lib', 'kop', 'fog', 'tig', 'sob', 'pet', 'lop',
         'bet', 'bog', 'nog', 'gun', 'lud', 'sit', 'dib', 'dap', 'ban', 'kob',
         'nan', 'pat', 'pib', 'lip', 'fan', 'big', 'get', 'bob', 'rad', 'ran',
         'san', 'rot', 'bad', 'nop', 'nid', 'jut', 'nod', 'bap', 'fad', 'ten',
         'gid', 'dop', 'dit', 'fid', 'tap', 'bib', 'dog', 'lek', 'tog', 'deg',
         'fob', 'deb', 'beg', 'kan', 'sug', 'tup', 'ton', 'gag', 'dot', 'lot',
         'keg', 'pap', 'ren', 'fit', 'kip', 'tub', 'tin', 'pad', 'bip', 'pun',
         'tug', 'nap', 'sag', 'dob', 'gig', 'sup', 'tag', 'fub', 'reg', 'top',
         'jag', 'nib', 'sig', 'kit', 'dag', 'set', 'dud', 'bab', 'sud', 'sub',
         'dub', 'nit', 'fed', 'nat', 'tad', 'dab', 'fen', 'nun', 'lug', 'kut',
         'rep', 'fib', 'nab', 'nag', 'bok', 'gab', 'bot', 'bud', 'dad', 'sap',
         'tat', 'did', 'gog', 'dat', 'rub', 'pud', 'bop', 'lig', 'dut', 'pep',
         'fug', 'bod', 'sed', 'sen', 'teg', 'pit', 'fin', 'dun', 'rob', 'let',
         'neb', 'tut', 'sop', 'gan', 'fig', 'tab')


soft_replacements = {'c': 'k'}


words_to_bytes = {}
for i, word in enumerate(phono):
    if py == 2:
        words_to_bytes[word] = chr(i)
    else:
        words_to_bytes[word] = chr(i).encode('latin-1')


class PhonoByteError(Exception):

    pass


def encode(data, return_string=True):
    if isinstance(data, bytes):
        data = bytearray(data)
    if not isinstance(data, bytearray):
        err = 'Data must be in bytes - got: {}'
        raise PhonoByteError(err.format(type(data)))
    buffer = []
    for char in data:
        buffer.append(phono[char])
    return ' '.join(buffer) if return_string else buffer


def decode(words):
    if isinstance(words, (str, text_type)):
        words = words.split()
    if not isinstance(words, (list, tuple)):
        err = 'Words must be a string, list or tuple - got: {}'
        raise PhonoByteError(err.format(type(words)))
    buffer = b''
    for word in words:
        try:
            buffer += words_to_bytes[word.replace('c', 'k')]
        except KeyError:
            for k, v in soft_replacements.items():
                try:
                    buffer += words_to_bytes[word.replace(k, v)]
                except KeyError:
                    err = 'Invalid word in text: {}'
                    raise PhonoByteError(err.format(word))
    return buffer
