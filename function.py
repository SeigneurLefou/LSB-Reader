from PIL import Image
import os
import numpy as np
def txtToBin(txt):
    return ''.join(format(ord(c), '08b') for c in txt)
def octet(nb):
    return format(nb, '08b')
def binaryInputTxt(fileName) -> str:
    with open(f"input/{fileName}", "r") as file:
        content = file.read()
    binaryContent = txtToBin(content)
    return binaryContent
def arrangeTheBinaryWrapWrapped(anyBinaryWrapWrapped, weight=1):
    while len(anyBinaryWrapWrapped) < 3:
        anyBinaryWrapWrapped.append("0" * weight)
    anyBinaryWrapWrapped = [octet.ljust(weight, '0') for octet in anyBinaryWrapWrapped]
    return anyBinaryWrapWrapped
def changeLSBImageWithTxtOctet(inputPixel, binaryWrap, weight=1):
    outputPixel = list(inputPixel)
    binaryWrapWrapped = arrangeTheBinaryWrapWrapped([binaryWrap[i:i+weight] for i in range(0, len(binaryWrap), weight)], weight)
    for i in range(3):
        outputPixel[i] = int(octet(inputPixel[i])[:-weight] + binaryWrapWrapped[i], 2)
    return tuple(outputPixel)
def inculdeTxtInImage(inputImgName, inputTxtName, outputName="outputImage", weight=1, showOutput = False):
    weight = min(weight, 8)
    try:
        inputBinaryTxt = binaryInputTxt(inputTxtName)
    except:
        raise FileNotFoundError(f"There is no text file named \"{inputTxtName}\"")
    binaryTxtWrap = [inputBinaryTxt[i:i+3*weight] for i in range(0, len(inputBinaryTxt), 3*weight)]
    try:
        inputImg = Image.open(f"input/{inputImgName}").convert('RGB')
    except:
        raise FileNotFoundError(f"There is no image named \"{outputName}\"")
    width, height = inputImg.size
    outputImg = inputImg.copy()
    outputPixels = outputImg.load()
    pointer = 0
    for y in range(height):
        for x in range(width):
            if pointer < len(binaryTxtWrap):
                inputPixel = inputImg.getpixel((x, y))
                outputPixel = changeLSBImageWithTxtOctet(inputPixel, binaryTxtWrap[pointer], weight)
                outputPixels[x,y] = outputPixel
                pointer += 1
            else:
                if not os.path.exists('output'):
                    os.makedirs('output')
                outputImg.save(f"output/{outputName}.png")
                if showOutput:
                    outputImg.show()
                return True
    return False
def readTxtSinceImage(inputImgName, outputTxtName = "outputTxt", weight=1):
    weight = min(weight, 8)
    try:
        inputImg = Image.open(f"input/{inputImgName}").convert('RGB')
        colors = np.array(inputImg).flatten()
    except:
        raise FileNotFoundError(f"There is no image file named \"{inputImgName}\"")
    width, height = inputImg.size
    txtBinary = ""
    outputTxt = ""
    txtBinary = ''.join(octet(cl)[-weight:] for cl in colors)
    txtBinaryWrap = [txtBinary[i:i+8] for i in range(0, len(txtBinary), 8)]
    outputTxt = ''.join(chr(int("0b" + oct, 2)) for oct in txtBinaryWrap)
    outputTxt = ''.join(c for c in outputTxt if ord(c) < 128)
    if not os.path.exists('output'):
        os.makedirs('output')
    with open(f'output/{outputTxtName}.txt', 'w') as file:
        file.write(outputTxt)
    print(outputTxt)
    return outputTxt