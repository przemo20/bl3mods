#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import sys
import argparse
from bl3data.bl3data import BL3Data

UINameDictionary_DialogEnumValue = {}
UINameDictionary_DNT = {}

# Now process
data = BL3Data()

PathList_DialogEnumValue = list(data.find('', 'DialogEnumValue'))
PathList_DNT = list(data.find('', 'DNT'))


### DialogEnumValue files ###

print('> DialogEnumValue <')
for a in sorted(PathList_DialogEnumValue):
    DialogEnumValueData = data.get_exports(a, "DialogEnumValue")
    for b in DialogEnumValueData:
        try:
            UINamePath = b["UIName"][1]
            # print(UINamePath)
            SpeakerUIName = data.get_exports(UINamePath, "GbxUIName")[0]["DisplayName"]["string"]
            UINameDictionary_DialogEnumValue.setdefault(b["_jwp_object_name"], SpeakerUIName)  # .append(SpeakerUIName)
        except KeyError as e:
            # print(f"*** {e.args[0]} key for {a} is missing! ***")
            pass

for x in sorted(UINameDictionary_DialogEnumValue):
    # print("{}: {}".format(x, UINameDictionary_DialogEnumValue[x]))
    print("\'{}\': \'{}\',".format(x, UINameDictionary_DialogEnumValue[x].replace('\'', '\\\'')))


print()
print('---------------------------')
print()


### DialogNameTag (DNT) files ###

print('> DialogNameTag <')
for a in sorted(PathList_DNT):  # sorted(NameTagList)
    DialogNameTagData = data.get_data(a)
    NameTagEnumValue = None
    SpeakerUIName = None
    try:
        for b in DialogNameTagData:
            if b["export_type"] == "DialogNameTag":
                NameTagEnumValue = b["NameTagEnumValue"][0]
                # print(NameTagEnumValue)
        for c in DialogNameTagData:
            if c["export_type"] == "CharacterEchoData":
                SpeakerUINamePath = c["SpeakerUIName"][1]
                # print(SpeakerUINamePath)
                SpeakerUIName = data.get_exports(SpeakerUINamePath, "GbxUIName")[0]["DisplayName"]["string"]
                # print(SpeakerUIName)
        if NameTagEnumValue != None and SpeakerUIName != None:
            flag = False
            for t in UINameDictionary_DNT:
                if t == NameTagEnumValue:
                    for h in UINameDictionary_DNT[t]:
                        if h == SpeakerUIName:
                            flag = True
            if flag == False:
                UINameDictionary_DNT.setdefault(NameTagEnumValue, []).append(SpeakerUIName)
    except:
        pass

for x in sorted(UINameDictionary_DNT):
    print("\'{}\': {},".format(x, UINameDictionary_DNT[x]))
    # print("\"{}\": \"{}\",".format(x, UINameDictionary_DNT[x]))
