from openalpr import Alpr
import sys


def get_plate_alpr(img_path):
    openalprConf = r"F:\Kerja\PT AGIT\Bootcamp\AGIT Bootcamp Task\OJT\openalpr64-sdk-2.8.101\openalpr.conf"
    openalprRuntimeData = r"F:\Kerja\PT AGIT\Bootcamp\AGIT Bootcamp Task\OJT\openalpr64-sdk-2.8.101\runtime_data"
    alpr = Alpr("id", openalprConf, openalprRuntimeData)
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)
    results = alpr.recognize_file(img_path)
    # alpr.unload()

    return results
