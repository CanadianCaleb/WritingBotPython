
import random

import math

def split(word) :
    return[char for char in word]

from os import system, name

def clear() :
    if name == "nt" :
        _ = system('cls')
    else :
        _ = system('clear')

clear()
print('Creating list')
humanWritingtxt = open('humanWriting.txt')
humanWriting = list(humanWritingtxt)
humanWriting = ''.join(humanWriting)
print('List created')
print('Cleaning up files')

charWriting = split(humanWriting)

humanWriting = charWriting

for i in range(0, len(charWriting)) : # CREATES Characters from the words
    if i < len(charWriting) :
        if ord(charWriting[i]) == ord('\n') :
            charWriting.remove(charWriting[i])

tempWriting = ""

for i in range(0, len(charWriting)) :

    charWriting[i] = charWriting[i].lower()
    if ord(charWriting[i]) not in range(32, 65) and ord(charWriting[i]) not in range(91, 97) and ord(charWriting[i]) not in range(123, 127) :
        tempWriting += charWriting[i]
    if (i < len(charWriting) - 1) :
        if (ord(charWriting[i+1]) != 32 and ord(charWriting[i]) == 32) :
            tempWriting += " "
    if ord(charWriting[i]) == 35 :
        tempWriting += "#"

tempTempWriting = tempWriting.split(" ")
tempWriting = ""

for i in range(0, len(tempTempWriting)) :
  if (len(tempTempWriting[i]) > 0 and len(tempTempWriting[i]) < 16) :
    if (list(tempTempWriting[i])[0] != "#" and list(tempTempWriting[i])[0] != "@") :
        if (len(list(tempTempWriting[i])) < 3) :
            tempWriting += tempTempWriting[i] + " "
        elif (list(tempTempWriting[i])[0] != "h" and list(tempTempWriting[i])[1] != "t" and list(tempTempWriting[i])[2] != "t") :
            tempWriting += tempTempWriting[i] + " "

humanWriting = (''.join(charWriting)).split('/') # Splits through /

wordWriting = []

for i in range(0, len(humanWriting)) : # Splits into words
    wordWriting.append(humanWriting[i].split(' '))

wordCache = []
words = []

wordList = (''.join(tempWriting)).split(" ")

for i in range(0, len(wordList)) :
    print("Generating Cache Frame: " + str(round(10000*(i+1)/len(wordList))/100) + "%", end = "\r")
    if (wordList[i] not in words) : words.append(wordList[i])

print("                                                                           ", end = "\r")
print("Generated Cache Frame")

for i in range(0, len(words)) :
    print("Generating Cache Connections: " + str(round(10000*(i+1)/len(words))/100) + "%", end = "\r")
    wordCache.append([0 for x in range(0, len(words))])

print("                                                                           ", end = "\r")
print("Generated Cache Connections")

for i in range(0, len(words)) :
    print("Generating Cache Analysis: " + str(round(10000*(i+1)/len(words))/100) + "%", end = "\r")
    for j in range(1, len(wordList)) :
        if (wordList[j-1] == words[i]) : wordCache[i][words.index(wordList[j])] += 9
        if (wordList[j-2] == words[i]) : wordCache[i][words.index(wordList[j])] += 3
        if (wordList[j-3] == words[i]) : wordCache[i][words.index(wordList[j])] += 1

print("                                                                           ", end = "\r")
print("Generated Cache Analysis")

for i in range(0, len(wordCache)) :
    print("Generating Cache Regularization: " + str(round(10000*(i+1)/len(wordCache))/100) + "%", end = "\r")

    for j in range(0, len(wordCache)) :
      wordCache[i][j] = round(math.sqrt(wordCache[i][j])*wordCache[i][j])

print("                                                                           ", end = "\r")
print("Generated Cache Regularization")

for it in range(0, 40) :
  sentenceLength = random.randint(20,20)

  randomStart = random.choice(words)

  output = ""
  credibility = 0
  for i in range(0, sentenceLength) :
      if i == 0 :
          output += randomStart + " "
      else :
          temp = wordCache[words.index(output.split(" ")[-2])]
          tempSum = sum(temp)
          thing = 0

          tempPos = 0
          if (tempSum > 0) : rand = random.randint(0, tempSum - 1)
          else : rand = 0

          for j in range(0, len(temp)) :
              if (rand >= tempPos and rand < tempPos + temp[j] and thing != 1) :
                  output += words[j] + " "
                  thing = 1
                  credibility += temp[j]
              else :
                  tempPos += temp[j]
  
  output = output.split(" ")

  for j in range(0,sentenceLength) :
    if (j < sentenceLength - 3) :
      if (output[j] == output[j+2] and output[j+1] == output[j+3]) :
        wordCache[words.index(output[j])][words.index(output[j+1])] = round(0.7 * wordCache[words.index(output[j])][words.index(output[j+1])])
        wordCache[words.index(output[j+1])][words.index(output[j])] = round(0.7 * wordCache[words.index(output[j+1])][words.index(output[j])])
    
    if (j < sentenceLength - 2) :
      if (output[j] == output[j+1]) :
        wordCache[words.index(output[j])][words.index(output[j])] = round(0.5 * wordCache[words.index(output[j])][words.index(output[j+1])])

outCache = []
credCache = []
cutoff = 0

for it in range(0, 500) :
  sentenceLength = random.randint(20,20)

  randomStart = random.choice(words)

  output = ""
  credibility = 0
  for i in range(0, sentenceLength) :
      if i == 0 :
          output += randomStart + " "
      else :
          temp = wordCache[words.index(output.split(" ")[-2])]
          tempSum = sum(temp)
          thing = 0

          tempPos = 0
          if (tempSum > 0) : rand = random.randint(0, tempSum - 1)
          else : rand = 0

          for j in range(0, len(temp)) :
              if (rand >= tempPos and rand < tempPos + temp[j] and thing != 1) :
                  output += words[j] + " "
                  thing = 1
                  credibility += temp[j]
              else :
                  tempPos += temp[j]
          output = split(output)
          output[0] = output[0].upper() 
          output = ''.join(output)
  if credibility > cutoff :
    outCache.append(output)
    credCache.append(credibility)
    print(output, "\n", credibility/max(credCache))
    cutoff = 0.75 * max(credCache)

print(outCache[credCache.index(max(credCache))], max(credCache))
