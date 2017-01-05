# phonobyte

`phonobyte` encodes binary data to phonetically pronounceable three letter
words. The words have been chosen to be clearly understandable when spoken.
`phonobyte`, while not by any means the smallest binary to text encoing tool,
compares reasonably well with other popular methods despite being designed to
encode to pronounceable words:

| method    | input    | output   | chars per byte | average increase |
|-----------|----------|----------|----------------|------------------|
| hex       | \x11\x22 | 1122     | 2              | 100%             |
| base64    | \x11\x22 | ESI=     | 1.333          | 133%             |
| base32    | \x11\x22 | CERA==== | 1.625          | 162.5%           |
| phonobyte | \x11\x22 | dug gut  | 3              | 300%             |


Practical uses for `phonobyte` include to transmitting hashes, short
cryptography keys, etc. in a way that is easy to read and be spoken aloud by
humans.

# Installation

Install from pip:

```bash
$ pip install phonobyte
```

That's it. The library has no dependancies. `phonobyte` supports both
Python2 and Python3. It also comes with a  test suite. You can invoke the tests
by cloning this repository and running:

```bash
$ python setup.py test
```

# Usage

Basic usage:

```python
from phonobyte import encode, decode
test_data = b'test'
encoded_data = encode(test_data)
# prints: 'lab don nub lab'
print(encoded_data)
decoded_data = decode(encoded_data)
# prints: b'test'
print(decoded_data)
```

# Lookup table

Each word in the table has been carefully vetted to be a valid word in the
English dictionary, not be offensive and be clearly pronounceable with as
little scope for interpretation errors as possible. The table was then
randomised. The lookup table used to convert data is as follows:

| byte | word | byte | word | byte | word | byte | word |
|------|------|------|------|------|------|------|------|
| 00   | jab  | 01   | tip  | 02   | led  | 03   | rut  |
| 04   | dak  | 05   | jig  | 06   | rud  | 07   | pub  |
| 08   | not  | 09   | kid  | 0A   | bid  | 0B   | gup  |
| 0C   | lep  | 0D   | juk  | 0E   | jib  | 0F   | sid  |
| 10   | fon  | 11   | dug  | 12   | lap  | 13   | sog  |
| 14   | bug  | 15   | ret  | 16   | net  | 17   | fip  |
| 18   | gad  | 19   | peg  | 1A   | gap  | 1B   | fet  |
| 1C   | rog  | 1D   | lob  | 1E   | lin  | 1F   | pip  |
| 20   | fud  | 21   | lag  | 22   | gut  | 23   | reb  |
| 24   | din  | 25   | sun  | 26   | jun  | 27   | dig  |
| 28   | rag  | 29   | neg  | 2A   | bin  | 2B   | ben  |
| 2C   | gob  | 2D   | run  | 2E   | fab  | 2F   | lit  |
| 30   | ked  | 31   | rug  | 32   | lod  | 33   | rib  |
| 34   | rip  | 35   | sod  | 36   | ped  | 37   | dip  |
| 38   | leg  | 39   | sib  | 3A   | sad  | 3B   | sat  |
| 3C   | pak  | 3D   | jet  | 3E   | bun  | 3F   | gon  |
| 40   | geg  | 41   | bit  | 42   | gud  | 43   | rig  |
| 44   | dek  | 45   | pot  | 46   | pug  | 47   | ken  |
| 48   | gub  | 49   | rid  | 4A   | pen  | 4B   | nep  |
| 4C   | gib  | 4D   | jot  | 4E   | pup  | 4F   | tid  |
| 50   | sin  | 51   | kin  | 52   | job  | 53   | ted  |
| 54   | fun  | 55   | fop  | 56   | dan  | 57   | nip  |
| 58   | but  | 59   | tun  | 5A   | put  | 5B   | jog  |
| 5C   | jit  | 5D   | lad  | 5E   | pig  | 5F   | got  |
| 60   | tot  | 61   | gak  | 62   | sot  | 63   | rin  |
| 64   | lid  | 65   | don  | 66   | den  | 67   | pod  |
| 68   | rit  | 69   | gat  | 6A   | ket  | 6B   | sab  |
| 6C   | rat  | 6D   | bub  | 6E   | dod  | 6F   | dep  |
| 70   | dup  | 71   | tod  | 72   | lat  | 73   | nub  |
| 74   | lab  | 75   | pan  | 76   | rap  | 77   | tib  |
| 78   | tan  | 79   | bed  | 7A   | seg  | 7B   | lib  |
| 7C   | kop  | 7D   | fog  | 7E   | tig  | 7F   | sob  |
| 80   | pet  | 81   | lop  | 82   | bet  | 83   | bog  |
| 84   | nog  | 85   | gun  | 86   | lud  | 87   | sit  |
| 88   | dib  | 89   | dap  | 8A   | ban  | 8B   | kob  |
| 8C   | nan  | 8D   | pat  | 8E   | pib  | 8F   | lip  |
| 90   | fan  | 91   | big  | 92   | get  | 93   | bob  |
| 94   | rad  | 95   | ran  | 96   | san  | 97   | rot  |
| 98   | bad  | 99   | nop  | 9A   | nid  | 9B   | jut  |
| 9C   | nod  | 9D   | bap  | 9E   | fad  | 9F   | ten  |
| A0   | gid  | A1   | dop  | A2   | dit  | A3   | fid  |
| A4   | tap  | A5   | bib  | A6   | dog  | A7   | lek  |
| A8   | tog  | A9   | deg  | AA   | fob  | AB   | deb  |
| AC   | beg  | AD   | kan  | AE   | sug  | AF   | tup  |
| B0   | ton  | B1   | gag  | B2   | dot  | B3   | lot  |
| B4   | keg  | B5   | pap  | B6   | ren  | B7   | fit  |
| B8   | kip  | B9   | tub  | BA   | tin  | BB   | pad  |
| BC   | bip  | BD   | pun  | BE   | tug  | BF   | nap  |
| C0   | sag  | C1   | dob  | C2   | gig  | C3   | sup  |
| C4   | tag  | C5   | fub  | C6   | reg  | C7   | top  |
| C8   | jag  | C9   | nib  | CA   | sig  | CB   | kit  |
| CC   | dag  | CD   | set  | CE   | dud  | CF   | bab  |
| D0   | sud  | D1   | sub  | D2   | dub  | D3   | nit  |
| D4   | fed  | D5   | nat  | D6   | tad  | D7   | dab  |
| D8   | fen  | D9   | nun  | DA   | lug  | DB   | kut  |
| DC   | rep  | DD   | fib  | DE   | nab  | DF   | nag  |
| E0   | bok  | E1   | gab  | E2   | bot  | E3   | bud  |
| E4   | dad  | E5   | sap  | E6   | tat  | E7   | did  |
| E8   | gog  | E9   | dat  | EA   | rub  | EB   | pud  |
| EC   | bop  | ED   | lig  | EE   | dut  | EF   | pep  |
| F0   | fug  | F1   | bod  | F2   | sed  | F3   | sen  |
| F4   | teg  | F5   | pit  | F6   | fin  | F7   | dun  |
| F8   | rob  | F9   | let  | FA   | neb  | FB   | tut  |
| FC   | sop  | FD   | gan  | FE   | fig  | FF   | tab  |

# API

There are only two main methods to use in this library. All errors will raise
a `phonobyte.PhonoByteError` exception. The main methods are listed below with
their defaults:

`phonobyte.encode(data, return_string=True)`

**Arguments:**

 * `data` the binary input data to encode
 * `return_string` if set to `True` return a string, if set to `False` return
    a list

**Returns:**

 * A string of space separated words if `return_string` is `True`, otherwise a
   list of words

`phonobyte.decode(words)`

**Arguments:**

 * `words` a string of space separated words or a list of words

**Returns:**

 * Binary data

# Licensing

The `phonobyte` specification itself is open for anyone to implement. This
Python reference implementation are licensed under the LGPLv3.

# Contributing

All properly formatted and sensible pull requests, issues and comments are
welcome.
