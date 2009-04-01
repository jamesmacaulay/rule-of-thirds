import tests.fixtures
from Photographer import *

for (imageID, imageLines) in tests.fixtures.results.items():
  print "imageID: " + imageID
  objects = {}
  for line in imageLines:
    roundObj = PeekaboomRound(line)
    if objects.has_key(roundObj.label):
      objects[roundObj.label] = objects[roundObj.label].merge(roundObj)
    else:
      objects[roundObj.label] = roundObj
  objectEvaluations = {}
  for pkbRound in objects.values():
    if len(pkbRound.blobs()) > 0:
      objectEvaluations[pkbRound.label] = Photographer(pkbRound).ruleOfThirds()
      print ("  "," *")[pkbRound.label in tests.fixtures.imageIDs[imageID]] + pkbRound.label + ": " + str(objectEvaluations[pkbRound.label])
  evalTotal = 0.0
  for (key, value) in objectEvaluations.items():
    if key in tests.fixtures.imageIDs[imageID]:
      evalTotal += value
  evalAvg = evalTotal / 3
  print "  average for this image's primary objects: " + str(evalAvg)
  evalTotal = 0.0
  for (key, value) in objectEvaluations.items():
    evalTotal += value
  evalAvg = evalTotal / len(objectEvaluations.items())
  print "  average for all of this image's objects:  " + str(evalAvg) + "\n"