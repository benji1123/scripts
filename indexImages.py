'''
/*********************************************************/
 Ben Li | 2024-02-24 | Vancouver, BC, Canada
 Generate an index.js file for a directory of images
/*********************************************************/

Command:
 $ python indexImages.py -d <imageFolder>

If you want to use local-images in a React project, you can add an index.js file in the images folder:

    my-app/
    ├─ src/
    │  ├─ images/
    │  │  ├─ bird.jpg
    │  │  ├─ plane.jpg
    │  │  ├─ index.js   <===   add this!

Then you can import your images:
 import { bird, plane } from './images/index'
'''

from argparse import ArgumentParser
import os
import sys

VALID_EXT = ('.jpg', '.jpeg', '.png')
NEWLINE = '\n'
TAB = '  '

imports = [NEWLINE]
exports = ['export {']


def main():
    parser = ArgumentParser()
    parser.add_argument("-d", "--dir")
    args = parser.parse_args()

    if not args.dir:
        print('\nprovide <dir> argument: python indexImages.py -d ./images')
        sys.exit(1)


    addImportsExports(args.dir)
    printIndexJs(imports, exports)

'''traverse image folder and add collect import/export statements'''
def addImportsExports(dir: str):
    for filename in os.listdir(dir):
        path = os.path.join(dir, filename)
        if os.path.isfile(path) and path.endswith(VALID_EXT):
            imports.append(getImportStatement(path))
            exports.append(getExportStatement(path))
        elif os.path.isdir(path):
            addImportsExports(path)

def getImportStatement(path: str):
    resource = getFilenameNoExt(path)
    return f'import {resource} from "{path}"'

def getExportStatement(path: str):
    resource = getFilenameNoExt(path)
    return f'{TAB}{resource},'

def printIndexJs(imports: [str], exports: [str]):
    imports.append('\n')
    print(NEWLINE.join(imports))

    exports.append('}')
    print(NEWLINE.join(exports))

def getFilenameNoExt(path: str):
    name = os.path.basename(path)
    return removeNonAlphanumeric(os.path.splitext(name)[0])

def removeNonAlphanumeric(s: str):
        return "".join(x for x in s if x.isalnum())

main()
