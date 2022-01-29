import os
import glob
from PyPDF2 import PdfFileMerger
import logging

import locator
from locator import *

file_path = locator.path


def file_merger():
    try:
        logging.basicConfig (filename="file_locator.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s:%('
                                                                                      'message)s')

        os.chdir (file_path)
        pdf_files = []
        for file in glob.glob ("*.pdf"):
            pdf_files.append (file)

        if len (pdf_files) > 1:
            merger = PdfFileMerger ()
            for pdf in pdf_files:
                merger.append (pdf)

            merger.write ("final2.pdf")
            merger.close ()
            logging.info ("Hell yeah you have merged the files!!")
        else:
            print ("You just have one pdf file in the mentioned path")
            logging.info ("Enter a path where there are more than one pdf file!!")

    except Exception as e:
        logging.error ("Files merged successfully!")
        logging.debug ("Please check the entered path")
        logging.exception ("Exception has occurred: " + str (e))
