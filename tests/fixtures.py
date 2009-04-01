import os

roundData = "(n)((0a0a5415f77f3cc0177278c9a4401661)(ocean))(21.16.1.2.7.2005)(297 212)(p 16035888797995720969136800 b 477870931283701680717739166)(((2562 b)((b)(110 98)))((2749 b)((b)(100 99)))((2937 b)((b)(94 104)))((3294 b)((b)(76 107)))((3476 b)((b)(63 108)))((3800 b)((b)(47 108)))((3992 b)((b)(39 115)))((4332 b)((b)(29 131)))((4499 b)((b)(20 131)))((4905 b)((b)(37 99)))((5096 b)((b)(18 103)))((5286 b)((b)(8 103)))((5645 b)((b)(7 91)))((5820 b)((b)(38 90)))((6164 b)((b)(72 91)))((6371 b)((b)(79 88)))((6683 b)((b)(56 85)))((6890 b)((b)(48 79)))((7244 b)((b)(39 66)))((7418 b)((b)(38 62)))((8633 b)((b)(115 51)))((8803 p)((g)(shark)))((8810 b)((b)(115 61)))((9174 b)((b)(115 75)))((9348 b)((b)(117 76)))((9739 b)((b)(133 72)))((10537 b)((q)(2)))((11169 p)((g)(sharks)))((11219 b)((b)(163 72)))((11409 b)((b)(149 74)))((11624 b)((b)(141 76)))((11825 b)((b)(150 86)))((12129 b)((b)(155 75)))((13416 p)((g)(whale)))((14855 p)((g)(fish)))((16002 b)((x)()))((19501 p)((x)())))"

verticalGridLine = "(n)((0a0a5415f77f3cc0177278c9a4401661)(verticalGridLine))(21.16.1.2.7.2005)(300 300)(p 16035888797995720969136800 b 477870931283701680717739166)(((1 b)((b)(100 0)))((2 b)((b)(100 300)))((3 b)((b)(100 200))))"

threePoints = "(n)((0a4e29ff30052c2ab7896d9b82732600)(of))(48.16.2.15.7.2005)(297 212)(b 160870743258536873564091931 p 769864899894499866471017997)(((1643 b)((b)(144 21)))((1908 b)((b)(152 19)))((2748 b)((p)(142 18)))((3377 p)((g)(of))))"

results = {}
__pkbDir = os.path.join('results')
imageIDs = {"0a2d49f7887f2efb04fd66a74ecd0857": ['www', 'informing', 'about'],
"0a0ddc9321171986268339dd743ceb16": ['beer', 'stripes', 'hat'],
"0a4bbc29780870e6fb04a220d4e51aca": ['boat', 'tent', 'man'],
"00a1ae2f78248a1e45ddea384fcf00c0": ['man', 'sheep', 'flower'],
"0a4dcfa22e7bbc76d8ab9df9c7eac802": ['dank', 'solder', 'cord'],
"0a0a5415f77f3cc0177278c9a4401661": ['ocean', 'sun', 'sharks'],
"0a2c57e1832e588b5f8f8f74aa28cbfa": ['trees', 'barn', 'ground'],
"0a3fe67dfd95718e966676b4d0e86f26": ['board', 'people', 'table'],
"0a4ee16a51eefcf055df320779c933c3": ['man', 'tree', 'mountain'],
"000a4e16941669737f537d759f10ae8a": ['circle', 'soon', 'coming'],
"0a4a9d430881d427051763155dc6e012": ['select', 'card', 'details'],
"0a0f44216768c5d0b3754f032a2d22ef": ['helmet', 'tyre', 'door'],
"0a0d787ea3337cf2f2ab3b3dbcd7563d": ['hat', 'mountain', 'man'],
"0a4e29ff30052c2ab7896d9b82732600": ['sequencing', 'of', 'cloning'],
"0a4a4f0b7152a955d2c0a0c17253be8e": ['table', 'chair', 'stove'],
"0a2cedef87bec3e2c6689060d3e60975": ['strap', 'backpack', 'zipper'],
"0a4ffff02e288008a2cafe68ddaddb58": ['come', 'to', 'the'],
"0a3d2c31faa6e4ea97b4cc3aaaca3256": ['clouds', 'sky', 'mountain'],
"0a1b267be01fc932f5a98f76211c0e97": ['people', 'art', 'umbrella'],
"0a0dea2f7dd115bff340fb7b35c6916a": ['tree', 'water', 'sun']}
  
for imageID in imageIDs.keys():
  results[imageID] = []
  fileData = open(os.path.join(__pkbDir, (imageID + '.pkb')), 'r')
  for line in fileData:
    results[imageID].append(line)
