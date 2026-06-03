import datalibraries
import filerenaming
import machinelearning
import scheduler
import webscraping
from datapreprocessing import datapreprocessing
from emailautomate import send_email_report

if __name__ == '__main__':
    #Modify files
    # directory = r'.\resources\img'
    # filerenaming.rename_files_in_directory(directory)

    #Webscrapping
    # webscraping.fetch_links('https://www.marca.com/')
    # webscraping.retrieve_tags('https://www.eldia.es/', 'h1')

    # Datalibraries
    # datalibraries.numpy_test()
    # datalibraries.pandas_test()
    # datalibraries.sklearn_test()

    # Machine Learning
    # machinelearning.machine_learning()

    # Data Preprocessing
    datapreprocessing()

    # Automate
    # send_email_report()
